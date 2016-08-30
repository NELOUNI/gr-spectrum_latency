#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/raid/nae/pybombs/src/gr-spectrum_latency/python
export PATH=/raid/nae/pybombs/src/gr-spectrum_latency/python/python:$PATH
export LD_LIBRARY_PATH=/raid/nae/pybombs/src/gr-spectrum_latency/python/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/raid/nae/pybombs/src/gr-spectrum_latency/python/swig:$PYTHONPATH
/usr/bin/python2 /raid/nae/pybombs/src/gr-spectrum_latency/python/qa_sslsocket_sink.py 
