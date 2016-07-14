/* -*- c++ -*- */
/*
 * Copyright 2004,2010,2013 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * GNU Radio is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * GNU Radio is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with GNU Radio; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "jsonfile_sink_impl.h"
#include <gnuradio/io_signature.h>
#include <cstdio>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdexcept>

#include <iostream>
#include <fstream>
#include <ctime>

#ifdef HAVE_IO_H
#include <io.h>
#endif

namespace gr {
  namespace msod_sensor {

    jsonfile_sink::sptr
    jsonfile_sink::make(unsigned int num_ch, const char* filename, const char* sensorLoc, const char* sensorSys, const char* sensor_id, const char* sensor_key, float center_freq, float bandwidth, float meas_duration, float atten, float samp_rate, bool avoid_LO)
    {
      return gnuradio::get_initial_sptr
        (new jsonfile_sink_impl(num_ch, filename, sensorLoc, sensorSys, sensor_id, sensor_key, center_freq, bandwidth, meas_duration, atten, samp_rate, avoid_LO));
    }
    jsonfile_sink_impl::jsonfile_sink_impl(unsigned int num_ch, const char* filename, const char* sensorLoc, const char* sensorSys, const char* sensor_id, const char* sensor_key, float center_freq, float bandwidth, float meas_duration, float atten, float samp_rate, bool avoid_LO)
  : gr::sync_block("jsonfile_sink",
                  gr::io_signature::make(1, 1, num_ch),
                  gr::io_signature::make(0, 0, 0)),
                  d_num_ch(num_ch), d_filename(filename), d_sensorLoc(sensorLoc), d_sensorSys(sensorSys), d_sensor_id(sensor_id), d_sensor_key(sensor_key), d_center_freq(center_freq), d_bandwidth(bandwidth), d_meas_duration(meas_duration), d_atten(atten), d_samp_rate(samp_rate), d_avoid_LO(avoid_LO)
    {
    json loc_msg = read_json_from_file(d_sensorLoc);
    json sys_msg = read_json_from_file(d_sensorSys);

    std::time_t ts = std::time(nullptr);
    loc_msg["t"] = ts;
    sys_msg["t"] = ts;
    loc_msg["SensorID"] = d_sensor_id;
    sys_msg["SensorID"] = d_sensor_id;

    post_msg(loc_msg);
    post_msg(sys_msg);
    float f_start = d_center_freq - d_bandwidth / 2.0;
    if (d_avoid_LO) {
    					//d_center_freq = d_center_freq + d_samp_rate/4.0;
    					float f_start = (d_center_freq - d_samp_rate/4.0) - d_bandwidth / 2.0;
    				}
    float f_stop  = f_start + d_bandwidth;

	// Need to add a field for overflow indicator
	json mPar = {
	{"fStart",	f_start},
	{"fStop",	f_stop},
	{"n",		d_num_ch},
	{"t",		-1},
	{"tm",		d_meas_duration},
	{"Det",		"Average"},
	{"Atten",	d_atten}
	};

	json data_hdr = {
	{"Ver"		, "1.0.12"},
	{"Type"		, "Data"},
	{"SensorID"	, d_sensor_id},
	{"SensorKey"	, d_sensor_key},
	{"t"		, ts},
	{"Sys2Detect"	, "LTE"},
	{"Sensitivity"	, "Low"},
	{"mType"	, "FFT-Power"},
	{"t1"		, ts},
	{"a"		, 1},
	{"nM"		, -1},
	{"Ta"		, -1},
	{"OL"		, "NaN"},
	{"wnI"		, -77.0},
	{"Comment"	, "Using hard-coded (not detected) system noise power for wnI"},
	{"Processed"	, "False"},
	{"DataType"	, "Binary - int8"},
	{"ByteOrder"	, "N/A"},
	{"Compression"	, "None"},
	{"mPar"	, mPar}
	};

	post_msg(data_hdr);
	mode_t mode = S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH;
	d_fd = open(d_filename, O_WRONLY | O_CREAT | O_APPEND, mode);
    };

    jsonfile_sink_impl::~jsonfile_sink_impl()
    {
      close(d_fd);
      float d_f_start = d_center_freq - d_bandwidth / 2.0;
      float d_f_stop  = d_f_start + d_bandwidth;
      time_t var = time(nullptr);
      const char* d_date_str = asctime(localtime(&var));
      printf ("%s fc = %f MHz. Writing data to file %s \n", d_date_str, ((d_f_start+d_f_stop)/2e6), d_filename);
    }

    json jsonfile_sink_impl::read_json_from_file(const char* filename){
    	fstream myfile;
    	myfile.open(filename);
    	string line, text;
    	while(std::getline(myfile, line))
    	   {   text += line + "\n";   }
        myfile.close();
        json js = json::parse(text);
        return js;
    }

    void jsonfile_sink_impl::post_msg(json obj){
    	string msg = obj.dump();
    	string ascii_hdr = to_string(msg.size()) + "\r";
        ofstream outfile;
        outfile.open(d_filename, ios::out | ios::app | ios::binary | ios::trunc);
        outfile << ascii_hdr << obj;
        outfile.close();
    }

    int  jsonfile_sink_impl::work(int noutput_items,
                                    gr_vector_const_void_star &input_items,
                                    gr_vector_void_star &output_items)
    {
      char *inbuf = (char*)input_items[0];
      unsigned long byte_size = noutput_items * d_num_ch * sizeof(char);
      while(byte_size > 0) {
        ssize_t r;
        r = write(d_fd, inbuf, byte_size);
        if(r == -1) {
         if(errno == EINTR)
           continue;
         else {
           perror("jsonfile_sink");
           return -1;    // indicate we're done
         }
        }
        else {
          byte_size -= r;
          inbuf += r;
        }
      }

      return noutput_items;
    }
  } /* namespace msod_sensor */
} /* namespace gr */
