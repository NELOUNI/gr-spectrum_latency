/* -*- c++ -*- */

#define MSOD_SENSOR_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "msod_sensor_swig_doc.i"

%{
#include "msod_sensor/bin_statistics.h"
#include "msod_sensor/jsonfile_sink.h"
#include "msod_sensor/bin_aggregator.h"
#include "msod_sensor/bin_statistics.h"
#include "msod_sensor/jsonfile_sink.h"
#include "msod_sensor/bin_aggregator.h"
%}


%include "msod_sensor/bin_statistics.h"
GR_SWIG_BLOCK_MAGIC2(msod_sensor, bin_statistics);
%include "msod_sensor/bin_statistics.h"
GR_SWIG_BLOCK_MAGIC2(msod_sensor, bin_statistics);
%include "msod_sensor/jsonfile_sink.h"
GR_SWIG_BLOCK_MAGIC2(msod_sensor, jsonfile_sink);
%include "msod_sensor/bin_aggregator.h"
GR_SWIG_BLOCK_MAGIC2(msod_sensor, bin_aggregator);
