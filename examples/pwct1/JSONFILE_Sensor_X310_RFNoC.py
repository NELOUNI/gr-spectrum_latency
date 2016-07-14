#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Msod Sslsensor X310 Rfnoc
# Generated: Tue Dec  1 15:29:03 2015
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import ettus
import math
import msod_sensor
import sys


class MSOD_SSLSensor_X310_RFNoC(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Msod Sslsensor X310 Rfnoc")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Msod Sslsensor X310 Rfnoc")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "MSOD_SSLSensor_X310_RFNoC")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 12.5e6
        self.fft_size = fft_size = 1024
        self.num_ch = num_ch = 56
        self.hz_per_bin = hz_per_bin = samp_rate / fft_size
        self.bandwidth = bandwidth = 10.08e6
        self.meas_interval = meas_interval = 1e-3
        self.channel_bw = channel_bw = hz_per_bin * round(bandwidth / num_ch / hz_per_bin)
        self.device3 = variable_uhd_device3_0 = ettus.device3(uhd.device_addr_t( ",".join(("type=x300", "addr=usrp0")) ))
        self.rx_gain = rx_gain = 0
        self.meas_period = meas_period = max(1, int(round(meas_interval * samp_rate / fft_size)))
        self.impedance = impedance = 50.0
        self.dest_host = dest_host = "129.6.142.138"
        self.center_freq = center_freq = 724e6
        self.ActualBW = ActualBW = channel_bw * num_ch

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_options = (12.5e6, 15.36e6, 7.68e6, 3.84e6, 1.92e6, )
        self._samp_rate_labels = ("12.5e6", "15.36e6", "7.68e6", "3.84e6", "1.92e6", )
        self._samp_rate_group_box = Qt.QGroupBox("samp_rate")
        self._samp_rate_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._samp_rate_button_group = variable_chooser_button_group()
        self._samp_rate_group_box.setLayout(self._samp_rate_box)
        for i, label in enumerate(self._samp_rate_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._samp_rate_box.addWidget(radio_button)
        	self._samp_rate_button_group.addButton(radio_button, i)
        self._samp_rate_callback = lambda i: Qt.QMetaObject.invokeMethod(self._samp_rate_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._samp_rate_options.index(i)))
        self._samp_rate_callback(self.samp_rate)
        self._samp_rate_button_group.buttonClicked[int].connect(
        	lambda i: self.set_samp_rate(self._samp_rate_options[i]))
        self.top_layout.addWidget(self._samp_rate_group_box)
        self._rx_gain_range = Range(0, 31.5, 0.5, 0, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, "rx_gain", "counter_slider", float)
        self.top_layout.addWidget(self._rx_gain_win)
        self._num_ch_options = (56, 50, 25, 15, 8, )
        self._num_ch_labels = ("56", "50", "25", "15", "8", )
        self._num_ch_group_box = Qt.QGroupBox("num_ch")
        self._num_ch_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._num_ch_button_group = variable_chooser_button_group()
        self._num_ch_group_box.setLayout(self._num_ch_box)
        for i, label in enumerate(self._num_ch_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._num_ch_box.addWidget(radio_button)
        	self._num_ch_button_group.addButton(radio_button, i)
        self._num_ch_callback = lambda i: Qt.QMetaObject.invokeMethod(self._num_ch_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._num_ch_options.index(i)))
        self._num_ch_callback(self.num_ch)
        self._num_ch_button_group.buttonClicked[int].connect(
        	lambda i: self.set_num_ch(self._num_ch_options[i]))
        self.top_layout.addWidget(self._num_ch_group_box)
        self._fft_size_options = (625, 1024, 512, 256, 128, )
        self._fft_size_labels = ("625", "1024", "512", "256", "128", )
        self._fft_size_tool_bar = Qt.QToolBar(self)
        self._fft_size_tool_bar.addWidget(Qt.QLabel("fft_size"+": "))
        self._fft_size_combo_box = Qt.QComboBox()
        self._fft_size_tool_bar.addWidget(self._fft_size_combo_box)
        for label in self._fft_size_labels: self._fft_size_combo_box.addItem(label)
        self._fft_size_callback = lambda i: Qt.QMetaObject.invokeMethod(self._fft_size_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._fft_size_options.index(i)))
        self._fft_size_callback(self.fft_size)
        self._fft_size_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_fft_size(self._fft_size_options[i]))
        self.top_layout.addWidget(self._fft_size_tool_bar)
        self._dest_host_options = ("pwct1.ctl.nist.gov", "129.6.230.12", "129.6.142.181", "129.6.142.138", )
        self._dest_host_labels = ("pwct1", "Naceur Laptop", "pwct5Desktop", "Pwct5", )
        self._dest_host_tool_bar = Qt.QToolBar(self)
        self._dest_host_tool_bar.addWidget(Qt.QLabel(dest_host+": "))
        self._dest_host_combo_box = Qt.QComboBox()
        self._dest_host_tool_bar.addWidget(self._dest_host_combo_box)
        for label in self._dest_host_labels: self._dest_host_combo_box.addItem(label)
        self._dest_host_callback = lambda i: Qt.QMetaObject.invokeMethod(self._dest_host_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._dest_host_options.index(i)))
        self._dest_host_callback(self.dest_host)
        self._dest_host_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_dest_host(self._dest_host_options[i]))
        self.top_layout.addWidget(self._dest_host_tool_bar)
        self._center_freq_options = (709.01e6, 782e6, 724e6, )
        self._center_freq_labels = ("AT&T", "Verizon", "ChannelEmulator", )
        self._center_freq_tool_bar = Qt.QToolBar(self)
        self._center_freq_tool_bar.addWidget(Qt.QLabel("center_freq"+": "))
        self._center_freq_combo_box = Qt.QComboBox()
        self._center_freq_tool_bar.addWidget(self._center_freq_combo_box)
        for label in self._center_freq_labels: self._center_freq_combo_box.addItem(label)
        self._center_freq_callback = lambda i: Qt.QMetaObject.invokeMethod(self._center_freq_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._center_freq_options.index(i)))
        self._center_freq_callback(self.center_freq)
        self._center_freq_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_center_freq(self._center_freq_options[i]))
        self.top_layout.addWidget(self._center_freq_tool_bar)
        self.uhd_rfnoc_streamer_vector_iir_0 = ettus.rfnoc_generic(
              self.device3,
              uhd.stream_args( # TX Stream Args
                  cpu_format="fc32",
                  otw_format="sc16",
                  args="spp={},alpha={},beta={}".format(fft_size, 0.984375, 0.015625),
              ),
              uhd.stream_args( # TX Stream Args
                  cpu_format="fc32",
                  otw_format="sc16",
                  args="spp={},alpha={},beta={}".format(fft_size, 0.984375, 0.015625),
              ),
              "VectorIIR", -1, -1,
        )
        self.uhd_rfnoc_streamer_vector_iir_0.set_arg("alpha", 0.984375)
        self.uhd_rfnoc_streamer_vector_iir_0.set_arg("beta",  0.015625)
          
        self.uhd_rfnoc_streamer_radio_0 = ettus.rfnoc_radio(
            self.device3,
            uhd.stream_args( # Tx Stream Args
                cpu_format="fc32",
                otw_format="sc16",
                args="", # empty
            ),
            uhd.stream_args( # Rx Stream Args
                cpu_format="fc32",
                otw_format="sc16",
        	args="",
            ),
            0, -1
        )
        self.uhd_rfnoc_streamer_radio_0.set_rx_freq(center_freq)
        self.uhd_rfnoc_streamer_radio_0.set_rx_rate(samp_rate)
        self.uhd_rfnoc_streamer_radio_0.set_rx_gain(rx_gain)
        self.uhd_rfnoc_streamer_radio_0.set_rx_antenna("TX/RX")
        self.uhd_rfnoc_streamer_radio_0.set_rx_dc_offset(True)
        self.uhd_rfnoc_streamer_fifo_0 = ettus.rfnoc_generic(
            self.device3,
            uhd.stream_args( # TX Stream Args
                cpu_format="fc32",
                otw_format="sc16",
                args="gr_vlen={0},{1}".format(fft_size, "" if fft_size == 1 else "spp={0}".format(fft_size)),
            ),
            uhd.stream_args( # RX Stream Args
                cpu_format="fc32",
                otw_format="sc16",
                args="gr_vlen={0},{1}".format(fft_size, "" if fft_size == 1 else "spp={0}".format(fft_size)),
            ),
            "FIFO", -1, -1,
        )
        self.uhd_rfnoc_streamer_fft_0 = ettus.rfnoc_generic(
            self.device3,
            uhd.stream_args( # TX Stream Args
                cpu_format="fc32", # TODO: This must be made an option
                otw_format="sc16",
                args="spp={},magnitude_out={}".format(1024, "MAGNITUDE_SQUARED"),
            ),
            uhd.stream_args( # RX Stream Args
                cpu_format="fc32", # TODO: This must be made an option
                otw_format="sc16",
                args="",
            ),
            "FFT", -1, -1,
        )
        self.msod_sensor_sslsocket_sink_0 = msod_sensor.sslsocket_sink(num_ch, dest_host, "/raid/nae/pybombs_RFNoC/src/gr-msod_latency/examples/sensor.loc", "/raid/nae/pybombs_RFNoC/src/gr-msod_latency/examples/sensor.sys", "X310", "NaN", center_freq, ActualBW, meas_interval, 0, samp_rate, False)
        self.msod_sensor_bin_statistics_0 = msod_sensor.bin_statistics(num_ch, meas_period)
        self.msod_sensor_bin_aggregator_0 = msod_sensor.bin_aggregator(fft_size, num_ch, samp_rate, fft_size, center_freq, ActualBW, channel_bw, [0] * fft_size, False)
        self.blocks_float_to_char_0 = blocks.float_to_char(num_ch, 1.0)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(fft_size)
        self._bandwidth_options = (10.08e6, 9e6, 4.5e6, 2.7e6, 1.08e6, )
        self._bandwidth_labels = ("10.08e6", "9e6", "4.5e6", "2.7e6", "1.08e6", )
        self._bandwidth_tool_bar = Qt.QToolBar(self)
        self._bandwidth_tool_bar.addWidget(Qt.QLabel("bandwidth"+": "))
        self._bandwidth_combo_box = Qt.QComboBox()
        self._bandwidth_tool_bar.addWidget(self._bandwidth_combo_box)
        for label in self._bandwidth_labels: self._bandwidth_combo_box.addItem(label)
        self._bandwidth_callback = lambda i: Qt.QMetaObject.invokeMethod(self._bandwidth_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._bandwidth_options.index(i)))
        self._bandwidth_callback(self.bandwidth)
        self._bandwidth_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_bandwidth(self._bandwidth_options[i]))
        self.top_layout.addWidget(self._bandwidth_tool_bar)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_real_0, 0), (self.msod_sensor_bin_aggregator_0, 0))    
        self.connect((self.blocks_float_to_char_0, 0), (self.msod_sensor_sslsocket_sink_0, 0))    
        self.connect((self.msod_sensor_bin_aggregator_0, 0), (self.msod_sensor_bin_statistics_0, 0))    
        self.connect((self.msod_sensor_bin_statistics_0, 0), (self.blocks_float_to_char_0, 0))    
        self.connect((self.uhd_rfnoc_streamer_vector_iir_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.device3.connect(self.uhd_rfnoc_streamer_fft_0.get_block_id(), 0, self.uhd_rfnoc_streamer_vector_iir_0.get_block_id(), 0)    
        self.device3.connect(self.uhd_rfnoc_streamer_fifo_0.get_block_id(), 0, self.uhd_rfnoc_streamer_fft_0.get_block_id(), 0)    
        self.device3.connect(self.uhd_rfnoc_streamer_radio_0.get_block_id(), 0, self.uhd_rfnoc_streamer_fifo_0.get_block_id(), 0)    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "MSOD_SSLSensor_X310_RFNoC")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_hz_per_bin(self.samp_rate / self.fft_size)
        self.set_meas_period(max(1, int(round(self.meas_interval * self.samp_rate / self.fft_size))))
        self._samp_rate_callback(self.samp_rate)
        self.uhd_rfnoc_streamer_radio_0.set_rx_rate(self.samp_rate)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size
        self._fft_size_callback(self.fft_size)
        self.set_hz_per_bin(self.samp_rate / self.fft_size)
        self.set_meas_period(max(1, int(round(self.meas_interval * self.samp_rate / self.fft_size))))

    def get_num_ch(self):
        return self.num_ch

    def set_num_ch(self, num_ch):
        self.num_ch = num_ch
        self.set_ActualBW(self.channel_bw * self.num_ch)
        self.set_channel_bw(self.hz_per_bin * round(self.bandwidth / self.num_ch / self.hz_per_bin))
        self._num_ch_callback(self.num_ch)

    def get_hz_per_bin(self):
        return self.hz_per_bin

    def set_hz_per_bin(self, hz_per_bin):
        self.hz_per_bin = hz_per_bin
        self.set_channel_bw(self.hz_per_bin * round(self.bandwidth / self.num_ch / self.hz_per_bin))

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self._bandwidth_callback(self.bandwidth)
        self.set_channel_bw(self.hz_per_bin * round(self.bandwidth / self.num_ch / self.hz_per_bin))

    def get_meas_interval(self):
        return self.meas_interval

    def set_meas_interval(self, meas_interval):
        self.meas_interval = meas_interval
        self.set_meas_period(max(1, int(round(self.meas_interval * self.samp_rate / self.fft_size))))

    def get_channel_bw(self):
        return self.channel_bw

    def set_channel_bw(self, channel_bw):
        self.channel_bw = channel_bw
        self.set_ActualBW(self.channel_bw * self.num_ch)

    def get_variable_uhd_device3_0(self):
        return self.variable_uhd_device3_0

    def set_variable_uhd_device3_0(self, variable_uhd_device3_0):
        self.variable_uhd_device3_0 = variable_uhd_device3_0

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_rfnoc_streamer_radio_0.set_rx_gain(self.rx_gain)

    def get_meas_period(self):
        return self.meas_period

    def set_meas_period(self, meas_period):
        self.meas_period = meas_period

    def get_impedance(self):
        return self.impedance

    def set_impedance(self, impedance):
        self.impedance = impedance

    def get_dest_host(self):
        return self.dest_host

    def set_dest_host(self, dest_host):
        self.dest_host = dest_host
        self._dest_host_callback(self.dest_host)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self._center_freq_callback(self.center_freq)
        self.uhd_rfnoc_streamer_radio_0.set_rx_freq(self.center_freq)

    def get_ActualBW(self):
        return self.ActualBW

    def set_ActualBW(self, ActualBW):
        self.ActualBW = ActualBW


def main(top_block_cls=MSOD_SSLSensor_X310_RFNoC, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
