#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Msod Sslsensor Bladerf
# Generated: Tue Mar  8 11:32:02 2016
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
from gnuradio import fft
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import math
import msod_sensor
import osmosdr
import sys
import time


class MSOD_SSLSensor_BladeRF(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Msod Sslsensor Bladerf")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Msod Sslsensor Bladerf")
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

        self.settings = Qt.QSettings("GNU Radio", "MSOD_SSLSensor_BladeRF")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 10e6
        self.fft_size = fft_size = 1000
        self.num_ch = num_ch = 50
        self.mywindow = mywindow = window.blackmanharris(fft_size)
        self.hz_per_bin = hz_per_bin = samp_rate / fft_size
        self.bandwidth = bandwidth = 9e6
        self.window_power = window_power = sum(map(lambda x: x*x, mywindow))
        self.meas_interval = meas_interval = 1e-3
        self.impedance = impedance = 50.0
        self.channel_bw = channel_bw = hz_per_bin * round(bandwidth / num_ch / hz_per_bin)
        self.rx_gain = rx_gain = 0
        self.meas_period = meas_period = max(1, int(round(meas_interval * samp_rate / fft_size)))
        self.dest_host = dest_host = "pwct5.ctl.nist.gov"
        self.center_freq = center_freq = 724e6
        self.Vsq2W_dB = Vsq2W_dB = -10.0 * math.log10(fft_size * int(window_power) * impedance)
        self.ActualBW = ActualBW = channel_bw * num_ch

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_options = (10e6, 15.36e6, 7.68e6, 3.84e6, 1.92e6, )
        self._samp_rate_labels = ("10e6", "15.36e6", "7.68e6", "3.84e6", "1.92e6", )
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
        self._fft_size_options = (1000, 1024, 512, 256, 128, )
        self._fft_size_labels = ("1000", "1024", "512", "256", "128", )
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
        self._dest_host_options = ("pwct1.ctl.nist.gov", "129.6.230.12", "pwc8.ctl.nist.gov", "pwct5.ctl.nist.gov", )
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
        self._center_freq_options = (709.01e6, 782e6, 724e6, 729e6, )
        self._center_freq_labels = ("AT&T", "Verizon", "ChannelEmulator", "HackRF Shifted Freq", )
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
        self._rx_gain_range = Range(0, 31.5, 0.5, 0, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, "rx_gain", "counter_slider", float)
        self.top_layout.addWidget(self._rx_gain_win)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "bladerf=0" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(1, 0)
        self.osmosdr_source_0.set_iq_balance_mode(2, 0)
        self.osmosdr_source_0.set_gain_mode(True, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(32, 0)
        self.osmosdr_source_0.set_bb_gain(40, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(20e6, 0)
          
        self.msod_sensor_sslsocket_sink_0 = msod_sensor.sslsocket_sink(num_ch, dest_host, "/raid/nae/pybombs/src/gr-msod_latency/examples/sensor_HackRF.loc", "/raid/nae/pybombs/src/gr-msod_latency/examples/sensor_HackRF.sys", "HackRF", "NaN", center_freq, ActualBW, meas_interval, 0, samp_rate, False)
        self.msod_sensor_bin_statistics_0 = msod_sensor.bin_statistics(num_ch, meas_period)
        self.msod_sensor_bin_aggregator_0 = msod_sensor.bin_aggregator(fft_size, num_ch, samp_rate, fft_size, center_freq, ActualBW, channel_bw, [0] * fft_size, False)
        self.fft_vxx_0 = fft.fft_vcc(fft_size, True, (mywindow), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, num_ch, 30.0 + Vsq2W_dB)
        self.blocks_float_to_char_0 = blocks.float_to_char(num_ch, 1.0)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(fft_size)
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
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.msod_sensor_bin_aggregator_0, 0))    
        self.connect((self.blocks_float_to_char_0, 0), (self.msod_sensor_sslsocket_sink_0, 0))    
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_float_to_char_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.msod_sensor_bin_aggregator_0, 0), (self.msod_sensor_bin_statistics_0, 0))    
        self.connect((self.msod_sensor_bin_statistics_0, 0), (self.blocks_nlog10_ff_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_stream_to_vector_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "MSOD_SSLSensor_BladeRF")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_hz_per_bin(self.samp_rate / self.fft_size)
        self.set_meas_period(max(1, int(round(self.meas_interval * self.samp_rate / self.fft_size))))
        self._samp_rate_callback(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size
        self.set_Vsq2W_dB(-10.0 * math.log10(self.fft_size * int(self.window_power) * self.impedance))
        self._fft_size_callback(self.fft_size)
        self.set_hz_per_bin(self.samp_rate / self.fft_size)
        self.set_meas_period(max(1, int(round(self.meas_interval * self.samp_rate / self.fft_size))))
        self.set_mywindow(window.blackmanharris(self.fft_size))

    def get_num_ch(self):
        return self.num_ch

    def set_num_ch(self, num_ch):
        self.num_ch = num_ch
        self.set_ActualBW(self.channel_bw * self.num_ch)
        self.set_channel_bw(self.hz_per_bin * round(self.bandwidth / self.num_ch / self.hz_per_bin))
        self._num_ch_callback(self.num_ch)

    def get_mywindow(self):
        return self.mywindow

    def set_mywindow(self, mywindow):
        self.mywindow = mywindow
        self.set_window_power(sum(map(lambda x: x*x, self.mywindow)))

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

    def get_window_power(self):
        return self.window_power

    def set_window_power(self, window_power):
        self.window_power = window_power
        self.set_Vsq2W_dB(-10.0 * math.log10(self.fft_size * int(self.window_power) * self.impedance))

    def get_meas_interval(self):
        return self.meas_interval

    def set_meas_interval(self, meas_interval):
        self.meas_interval = meas_interval
        self.set_meas_period(max(1, int(round(self.meas_interval * self.samp_rate / self.fft_size))))

    def get_impedance(self):
        return self.impedance

    def set_impedance(self, impedance):
        self.impedance = impedance
        self.set_Vsq2W_dB(-10.0 * math.log10(self.fft_size * int(self.window_power) * self.impedance))

    def get_channel_bw(self):
        return self.channel_bw

    def set_channel_bw(self, channel_bw):
        self.channel_bw = channel_bw
        self.set_ActualBW(self.channel_bw * self.num_ch)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain

    def get_meas_period(self):
        return self.meas_period

    def set_meas_period(self, meas_period):
        self.meas_period = meas_period

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
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)

    def get_Vsq2W_dB(self):
        return self.Vsq2W_dB

    def set_Vsq2W_dB(self, Vsq2W_dB):
        self.Vsq2W_dB = Vsq2W_dB

    def get_ActualBW(self):
        return self.ActualBW

    def set_ActualBW(self, ActualBW):
        self.ActualBW = ActualBW


def main(top_block_cls=MSOD_SSLSensor_BladeRF, options=None):

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
