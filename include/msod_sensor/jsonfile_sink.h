/* -*- c++ -*- */
/* 
 * Copyright 2014 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */


#ifndef INCLUDED_msod_sensor_JSONFILE_SINK_H
#define INCLUDED_msod_sensor_JSONFILE_SINK_H

#include <msod_sensor/api.h>
#include <gnuradio/sync_block.h>
#include "msod_sensor/json.hpp"
using nlohmann::json;
using namespace std;

namespace gr {
  namespace msod_sensor {

    /*!
     * \brief <+description of block+>
     * \ingroup msod_sensor
     *
     */
    class MSOD_SENSOR_API jsonfile_sink : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<jsonfile_sink> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of msod_sensor::jsonfile_sink.
       *
       * To avoid accidental use of raw pointers, msod_sensor::jsonfile_sink's
       * constructor is in a private implementation
       * class. msod_sensor::jsonfile_sink::make is the public interface for
       * creating new instances.
       */
      static sptr make(unsigned int num_ch, const char* filename, const char* sensorLoc, const char* sensorSys, const char* sensor_id, const char* sensor_key, float d_center_freq, float d_bandwidth, float meas_duration, float atten);
      virtual json read_json_from_file(const char* filename) = 0;
      virtual void post_msg(json obj) = 0;
      /*!
       * \brief Set file descriptor
       */
      //virtual void set_fd(int fd) = 0;
    };

  } // namespace msod_sensor
} // namespace gr

#endif /* INCLUDED_msod_sensor_JSONFILE_SINK_H */

