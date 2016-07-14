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

import numpy
from gnuradio import gr

import sys
import math

import time
import json
import socket
import ssl
import requests

import struct
import os
from timezone import getLocalUtcTimeStamp, formatTimeStampLong

class Struct(dict):
    def __init__(self, **kwargs):
        super(Struct, self).__init__(**kwargs)
        self.__dict__ = self

class sslsocket_sink(gr.sync_block):
    """
    docstring for block sslsocket_sink
    """
    def __init__(self, num_ch, dest_host, sensorLoc, sensorSys, sensor_id, sensor_key, center_freq, bandwidth, meas_duration, atten):
        gr.sync_block.__init__(self,
            name="sslsocket_sink",
            in_sig=[(bytes, num_ch)],
            out_sig=None)
        
        # Establish ssl socket connection to server
        self.num_ch = num_ch
        self.dest_host = dest_host
        self.sensorLoc = sensorLoc
        self.sensorSys = sensorSys
        self.sensor_id = sensor_id
        self.sensor_key = sensor_key
        self.center_freq = center_freq
        self.bandwidth = bandwidth
        self.meas_duration = meas_duration
        self.atten = atten
        
        r = requests.post('https://'+self.dest_host+':8443/sensordata/getStreamingPort/'+self.sensor_id, verify=False)
        print 'server response:', r.text
        response = r.json()
        print 'socket port =', response['port']
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = ssl.wrap_socket(sock, cert_reqs=ssl.CERT_NONE)
        self.sock.connect((self.dest_host, response['port']))
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
        self.send_obj(loc_msg)
        self.send_obj(sys_msg)
    
        # Form data header
        ts = long(round(getLocalUtcTimeStamp()))
        f_start = self.center_freq - self.bandwidth / 2.0
        f_stop = f_start + self.bandwidth
        mpar = Struct(fStart=f_start, fStop=f_stop, n=self.num_ch, td=-1, tm=self.meas_duration, Det='Average', Atten=self.atten)
        # Need to add a field for overflow indicator
        data = Struct(Ver='1.0.12', Type='Data', SensorID=self.sensor_id, SensorKey=self.sensor_key, t=ts, Sys2Detect='LTE', Sensitivity='Low', mType='FFT-Power', t1=ts, a=1, nM=-1, Ta=-1, OL='NaN', wnI=-77.0, Comment='Using hard-coded (not detected) system noise power for wnI', Processed='False', DataType = 'Binary - int8', ByteOrder='N/A', Compression='None', mPar=mpar)
    
        self.send_obj(data)
        date_str = formatTimeStampLong(ts, loc_msg['TimeZone'])
        print date_str, "fc =", self.center_freq/1e6, "MHz. Sending data to", self.dest_host
        
    def send(self, bytes):
        self.sock.send(bytes)

    def send_obj(self, obj):
        msg = json.dumps(obj)
        frmt = "=%ds" % len(msg)
        packed_msg = struct.pack(frmt, msg)
        ascii_hdr = "%d\r" % len(packed_msg)
        self.send(ascii_hdr)
        self.send(packed_msg)

    def read_json_from_file(self, fname):
        f = open(fname,'r')
        obj = json.load(f)
        f.close()
        return obj

    def work(self, input_items, output_items):
        in0 = input_items[0]
        num_input_items = len(in0)
	for i in range(num_input_items):
            self.sock.send(in0[i])
        return num_input_items
