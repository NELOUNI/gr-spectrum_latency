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

#ifndef INCLUDED_msod_sensor_BIN_AGGREGATOR_IMPL_H
#define INCLUDED_msod_sensor_BIN_AGGREGATOR_IMPL_H

#include <msod_sensor/bin_aggregator.h>

namespace gr {
  namespace msod_sensor {

    class bin_aggregator_impl : public bin_aggregator
    {
     private:
      unsigned int d_input_vlen;
      unsigned int d_output_vlen;
      std::vector<unsigned int> d_output_bin_index;
      float d_samp_rate;
      float d_fft_size;
      float d_center_freq;
      float d_bandwidth;
      float d_channel_bw;
      int d_i_bin;
      bool d_avoid_LO;

     public:
      void set_bin_index(const std::vector<unsigned int> &output_bin_index);
      float bin_freq(int i_bin, float center_freq);
      bin_aggregator_impl(unsigned int input_vlen, unsigned int output_vlen, float samp_rate, float fft_size, float center_freq, float bandwidth, float channel_bw, const std::vector<unsigned int> &output_bin_index, bool avoid_LO);
      ~bin_aggregator_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace msod_sensor
} // namespace gr

#endif /* INCLUDED_msod_sensor_BIN_AGGREGATOR_IMPL_H */

