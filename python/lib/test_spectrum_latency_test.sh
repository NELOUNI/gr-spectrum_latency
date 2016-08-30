#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/raid/nae/pybombs/src/gr-spectrum_latency/lib
export PATH=/raid/nae/pybombs/src/gr-spectrum_latency/python/lib:$PATH
export LD_LIBRARY_PATH=/raid/nae/pybombs/src/gr-spectrum_latency/python/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-spectrum_latency 
