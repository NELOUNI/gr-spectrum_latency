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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "bin_aggregator_impl.h"
#include <math.h>

namespace gr {
  namespace spectrum_latency {

    bin_aggregator::sptr
    bin_aggregator::make(unsigned int input_vlen, unsigned int output_vlen, float samp_rate, float fft_size, float center_freq, float bandwidth, float channel_bw, const std::vector<unsigned int> &output_bin_index)
    {
      return gnuradio::get_initial_sptr
        (new bin_aggregator_impl(input_vlen, output_vlen, samp_rate, fft_size, center_freq, bandwidth, channel_bw, output_bin_index));
    }

    /*
     * The private constructor
     */
    bin_aggregator_impl::bin_aggregator_impl(unsigned int input_vlen, unsigned int output_vlen, float samp_rate, float fft_size, float center_freq, float bandwidth, float channel_bw, const std::vector <unsigned int> &output_bin_index)
      : gr::sync_block("bin_aggregator",
              gr::io_signature::make(1, 1, input_vlen * sizeof(float)),
              gr::io_signature::make(1, 1, output_vlen * sizeof(float))),
	d_input_vlen(input_vlen), d_output_vlen(output_vlen),
	d_output_bin_index(output_bin_index),
	d_fft_size(fft_size),
	d_samp_rate(samp_rate),
    d_center_freq(center_freq),
    d_bandwidth(bandwidth),
    d_channel_bw(channel_bw),
    d_i_bin(0)
    {
    	float d_start_freq = d_center_freq - d_bandwidth / 2.0;
    	float d_stop_freq = d_start_freq + d_bandwidth;
	float hz_per_bin_ = d_samp_rate / d_fft_size;
	std::cout << "hz_per_bin = " << hz_per_bin_ << std::endl;
        for (int j=0; j < int(d_fft_size); j++)
		{
        	d_i_bin = j;
            float fj = bin_freq(d_i_bin, d_center_freq);
            if ((fj >= d_start_freq) && (fj < d_stop_freq))
			{
		std::cout << "f[" << j << "] = " << fj << std::endl;
                unsigned int channel_num = (floor((fj - d_start_freq) / d_channel_bw)) + 1;
		std::cout << "channel_num = " << channel_num << std::endl;
                d_output_bin_index[j] = channel_num;
		std::cout << "d_output_bin_index[" << j << "] = " << d_output_bin_index[j] << std::endl;
				}
		}
    }

    float bin_aggregator_impl::bin_freq(int bin_nbr, float center_freq)
    {
        float hz_per_bin = d_samp_rate / d_fft_size;
        //For odd fft_size, treats i_bin = (fft_size + 1) / 2 as the DC bin.
        float freq = center_freq + hz_per_bin * (bin_nbr - int(d_fft_size / 2) - (int(d_fft_size) % 2));
        return freq;
    }

    /*
     * Our virtual destructor.
     */
    bin_aggregator_impl::~bin_aggregator_impl()
    {
    }

    // Set the output_bin_index array.
    void
    bin_aggregator_impl::set_bin_index(
			  const std::vector<unsigned int> &output_bin_index)
    {
        memcpy(&d_output_bin_index[0], &output_bin_index[0], d_input_vlen * sizeof(unsigned int));
    }

    int
    bin_aggregator_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const float *in = (const float *) input_items[0];
        float *out = (float *) output_items[0];

	for (int n = 0; n < noutput_items; n++) {
	  for (int i = 0; i < d_output_vlen; i++)
	    out[n * d_output_vlen + i] = 0.0;
	  for (int i = 0; i < d_input_vlen; i++)
	    if ((d_output_bin_index[i] > 0) && (d_output_bin_index[i] <= d_output_vlen))
	      out[n * d_output_vlen + d_output_bin_index[i] - 1] += in[n * d_input_vlen + i];
	}

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace spectrum_latency */
} /* namespace gr */

