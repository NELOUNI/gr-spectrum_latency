/* -*- c++ -*- */
/*
 * Copyright 2004,2013 Free Software Foundation, Inc.
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

#ifndef INCLUDED_msod_sensor_JSONFILE_SINK_IMPL_H
#define INCLUDED_msod_sensor_JSONFILE_SINK_IMPL_H

#include <msod_sensor/jsonfile_sink.h>

namespace gr {
  namespace msod_sensor {

    class jsonfile_sink_impl : public jsonfile_sink
    {
    private:
      unsigned int d_num_ch;
      const char* d_filename; //string d_filename;
      const char* d_sensorLoc;
      const char* d_sensorSys;
      const char* d_sensor_id;
      const char* d_sensor_key;
      float d_center_freq;
      float d_bandwidth;
      float d_meas_duration;
      float d_atten;
      int d_fd;
      float d_samp_rate;
      bool d_avoid_LO;

    public:
      //void set_fd(int fd) { d_fd = fd; }
      jsonfile_sink_impl(unsigned int num_ch, const char* filename, const char* sensorLoc, const char* sensorSys, const char* sensor_id, const char* sensor_key, float d_center_freq, float d_bandwidth, float meas_duration, float atten, float samp_rate, bool avoid_LO);
      ~jsonfile_sink_impl();
      json read_json_from_file(const char* filename);
      void post_msg(json obj);
      int work(int noutput_items,
               gr_vector_const_void_star &input_items,
               gr_vector_void_star &output_items);
    };
} // namespace msod_sensor
} // namespace gr

#endif /* INCLUDED_msod_sensor_JSONFILE_SINK_IMPL_H */
