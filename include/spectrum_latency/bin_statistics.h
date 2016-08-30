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


#ifndef INCLUDED_spectrum_latency_BIN_STATISTICS_H
#define INCLUDED_spectrum_latency_BIN_STATISTICS_H

#include <spectrum_latency/api.h>
#include <gnuradio/sync_decimator.h>

namespace gr {
  namespace spectrum_latency {

    /*!
     * \brief <+description of block+>
     * \ingroup spectrum_latency
     *
     */
    class SPECTRUM_LATENCY_API bin_statistics : virtual public gr::sync_decimator
    {
     public:
      typedef boost::shared_ptr<bin_statistics> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of spectrum_latency::bin_statistics.
       *
       * To avoid accidental use of raw pointers, spectrum_latency::bin_statistics's
       * constructor is in a private implementation
       * class. spectrum_latency::bin_statistics::make is the public interface for
       * creating new instances.
       */
      static sptr make(unsigned int vlen, unsigned int meas_period);
    };

  } // namespace spectrum_latency
} // namespace gr

#endif /* INCLUDED_spectrum_latency_BIN_STATISTICS_H */

