#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#
from gnuradio import blocks
from gnuradio import filter
from gnuradio import fft
from gnuradio import uhd
from gnuradio import gr
from gnuradio.eng_option import eng_option
from optparse import OptionParser
import sys
import math
import threading
import array
import time
import json
from timezone import getLocalUtcTimeStamp, formatTimeStampLong

class Struct(dict):
    def __init__(self, **kwargs):
        super(Struct, self).__init__(**kwargs)
        self.__dict__ = self

class jsonfile_sink(gr.sync_block):
    """
    docstring for block jsonfile_sink
    """
    def __init__(self, num_ch, file_name, sensorLoc, sensorSys, sensor_id, sensor_key, center_freq, bandwidth, meas_duration, atten, samp_rate, avoid_LO):
        gr.sync_block.__init__(self,
            name="jsonfile_sink",
            in_sig=[(bytes, num_ch)],
            out_sig=None)

        # Establish ssl socket connection to server
        self.num_ch = num_ch

        # Open file for output stream
        self.file_name = file_name
    	self.f = open(self.file_name, 'wb')
	self.srvr = blocks.file_descriptor_sink(self.num_ch * gr.sizeof_char, self.f.fileno())

        self.sensorLoc = sensorLoc
        self.sensorSys = sensorSys
        self.sensor_id = sensor_id
        self.sensor_key = sensor_key
        self.center_freq = center_freq
        self.bandwidth = bandwidth
        self.meas_duration = meas_duration
        self.atten = atten
        self.samp_rate = samp_rate
        self.avoid = avoid_LO

    	
        print ("Sensor ID: ", self.sensor_id)
        # Send location and system info to server
        loc_msg = self.read_json_from_file(self.sensorLoc)
        sys_msg = self.read_json_from_file(self.sensorSys)
        ts = long(round(getLocalUtcTimeStamp()))
        print 'Serial no.', self.sensor_id
        loc_msg['t'] = ts
        loc_msg['SensorID'] = self.sensor_id
        sys_msg['t'] = ts
        sys_msg['SensorID'] = self.sensor_id
        self.post_msg(loc_msg)
        self.post_msg(sys_msg)

        # Form data header
        ts = long(round(getLocalUtcTimeStamp()))
        f_start = self.center_freq - self.bandwidth / 2.0
        if self.avoid:
            #self.center_freq = self.center_freq + self.samp_rate/4.0
            #print "Avoiding LO...\nShifting center Frequency to", self.center_freq
            f_start = (self.center_freq - self.samp_rate/4) - self.bandwidth/2.0
        f_stop = f_start + self.bandwidth
        if self.avoid:
            print "Avoiding LO, frequencies are shifted to: [",f_start/1e6, "MHz-",f_stop/1e6,"MHz ]"
        mpar = Struct(fStart=f_start, fStop=f_stop, n=self.num_ch, td=-1, tm=self.meas_duration, Det='Average', Atten=self.atten)
        # Need to add a field for overflow indicator
        data_hdr = Struct(Ver='1.0.12', Type='Data', SensorID=self.sensor_id, SensorKey=self.sensor_key, t=ts, Sys2Detect='LTE', Sensitivity='Low', mType='FFT-Power', t1=ts, a=1, nM=-1, Ta=-1, OL='NaN', wnI=-77.0, Comment='Using hard-coded (not detected) system noise power for wnI', Processed='False', DataType = 'Binary - int8', ByteOrder='N/A', Compression='None', mPar=mpar)

	self.post_msg(data_hdr)
    	self.f.flush()
        date_str = formatTimeStampLong(ts, loc_msg['TimeZone'])
    	print date_str, "fc =", self.center_freq/1e6, "MHz. Writing data to file", self.file_name

    def send(self, bytes):
        self.sock.send(bytes)

    def post_msg(self, obj):
        msg = json.dumps(obj)
	ascii_hdr = "%d\r" % len(msg)
	self.f.write(ascii_hdr + msg)

    def read_json_from_file(self, fname):
        g = open(fname,'r')
        obj = json.load(g)
        g.close()
        return obj

    def work(self, input_items, output_items):
        in0 = input_items[0]
        num_input_items = len(in0)
	for i in range(num_input_items):
            #self.file_name.write(in0[i])
            self.f.write(in0[i])
        return num_input_items
