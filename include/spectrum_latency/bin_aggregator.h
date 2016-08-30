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


#ifndef INCLUDED_spectrum_latency_BIN_AGGREGATOR_H
#define INCLUDED_spectrum_latency_BIN_AGGREGATOR_H

#include <spectrum_latency/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace spectrum_latency {

    /*!
     * \brief <+description of block+>
     * \ingroup spectrum_latency
     *
     */
    class SPECTRUM_LATENCY_API bin_aggregator : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<bin_aggregator> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of spectrum_latency::bin_aggregator.
       *
       * To avoid accidental use of raw pointers, spectrum_latency::bin_aggregator's
       * constructor is in a private implementation
       * class. spectrum_latency::bin_aggregator::make is the public interface for
       * creating new instances.
       */
      static sptr make(unsigned int input_vlen, unsigned int output_vlen, float samp_rate, float fft_size, float center_freq, float bandwidth, float channel_bw, const std::vector<unsigned int> &output_bin_index);

      /*!
       * \brief Set bin index array
       */
      virtual void set_bin_index(const std::vector <unsigned int> &output_bin_index) = 0;
      virtual float bin_freq(int i_bin, float center_freq) = 0;
    };

  } // namespace spectrum_latency
} // namespace gr

#endif /* INCLUDED_spectrum_latency_BIN_AGGREGATOR_H */

