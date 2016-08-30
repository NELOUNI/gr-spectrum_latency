/* -*- c++ -*- */

#define SPECTRUM_LATENCY_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "spectrum_latency_swig_doc.i"

%{
#include "spectrum_latency/bin_aggregator.h"
#include "spectrum_latency/bin_statistics.h"
%}


%include "spectrum_latency/bin_aggregator.h"
GR_SWIG_BLOCK_MAGIC2(spectrum_latency, bin_aggregator);
%include "spectrum_latency/bin_statistics.h"
GR_SWIG_BLOCK_MAGIC2(spectrum_latency, bin_statistics);

