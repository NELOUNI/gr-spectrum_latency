
/*
 * This file was automatically generated using swig_doc.py.
 *
 * Any changes to it will be lost next time it is regenerated.
 */




%feature("docstring") gr::spectrum_latency::bin_aggregator "<+description of block+>"

%feature("docstring") gr::spectrum_latency::bin_aggregator::make "Return a shared_ptr to a new instance of spectrum_latency::bin_aggregator.

To avoid accidental use of raw pointers, spectrum_latency::bin_aggregator's constructor is in a private implementation class. spectrum_latency::bin_aggregator::make is the public interface for creating new instances.

Params: (input_vlen, output_vlen, samp_rate, fft_size, center_freq, bandwidth, channel_bw, output_bin_index)"

%feature("docstring") gr::spectrum_latency::bin_aggregator::set_bin_index "Set bin index array.

Params: (output_bin_index)"

%feature("docstring") gr::spectrum_latency::bin_aggregator::bin_freq "

Params: (i_bin, center_freq)"

%feature("docstring") gr::spectrum_latency::bin_statistics "<+description of block+>"

%feature("docstring") gr::spectrum_latency::bin_statistics::make "Return a shared_ptr to a new instance of spectrum_latency::bin_statistics.

To avoid accidental use of raw pointers, spectrum_latency::bin_statistics's constructor is in a private implementation class. spectrum_latency::bin_statistics::make is the public interface for creating new instances.

Params: (vlen, meas_period)"