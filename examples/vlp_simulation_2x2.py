#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: VLP Simulation of 2x2 Array
# Author: Richard McAllister, Mike Rahaim
# Generated: Fri Mar 31 15:13:05 2017
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import math
import numpy
import sip
import sys
import vlc
import vlp2


class vlp_simulation_2x2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "VLP Simulation of 2x2 Array")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("VLP Simulation of 2x2 Array")
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

        self.settings = Qt.QSettings("GNU Radio", "vlp_simulation_2x2")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.y_var = y_var = .23
        self.x_var = x_var = 0.75
        self.TX4_location = TX4_location = 0.750, 0.93, 0
        self.TX3_location = TX3_location = 0.25, 0.93, 0
        self.TX2_location = TX2_location = .25, 0.23, 0
        self.TX1_location = TX1_location = .75, .23, 0
        self.Dz = Dz = 1.355
        self.distance4 = distance4 = numpy.sqrt( (x_var-TX4_location[0])**2 + (y_var-TX4_location[1])**2 + Dz**2)
        self.distance3 = distance3 = numpy.sqrt( (x_var-TX3_location[0])**2 + (y_var-TX3_location[1])**2 + Dz**2)
        self.distance2 = distance2 = numpy.sqrt( (x_var-TX2_location[0])**2 + (y_var-TX2_location[1])**2 + Dz**2)
        self.distance1 = distance1 = numpy.sqrt( (x_var-TX1_location[0])**2 + (y_var-TX1_location[1])**2 + Dz**2)
        self.tx_number = tx_number = 4
        self.samp_rate = samp_rate = int(2e6)
        self.noise = noise = 0
        self.lam_order = lam_order = 0.88
        self.goertzel_size = goertzel_size = 2000
        self.angle4 = angle4 = (numpy.arccos(  Dz/distance4  ) ) * (180/math.pi)
        self.angle3 = angle3 = (numpy.arccos(  Dz/distance3 ) ) * (180/math.pi)
        self.angle2 = angle2 = (numpy.arccos(  Dz/distance2  ) ) * (180/math.pi)
        self.angle1 = angle1 = (numpy.arccos(  Dz/distance1  ) ) * (180/math.pi)
        self.TXn_ampl = TXn_ampl = 0.7
        self.TX4_f = TX4_f = 400000
        self.TX3_f = TX3_f = 200000
        self.TX2_f = TX2_f = 300000
        self.TX1_f = TX1_f = 100000
        self.CtCr = CtCr = [1.37567074, 1.45229190, 1.50731873, 1.39086524]

        ##################################################
        # Blocks
        ##################################################
        self._y_var_range = Range(0, 1, .005, .23, 200)
        self._y_var_win = RangeWidget(self._y_var_range, self.set_y_var, "y_var", "counter_slider", float)
        self.top_layout.addWidget(self._y_var_win)
        self._x_var_range = Range(0, 1, .005, 0.75, 200)
        self._x_var_win = RangeWidget(self._x_var_range, self.set_x_var, "x_var", "counter_slider", float)
        self.top_layout.addWidget(self._x_var_win)
        self._noise_range = Range(0, 1, .01, 0, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, "noise", "counter_slider", float)
        self.top_layout.addWidget(self._noise_win)
        self.vlp2_trilat_scaleable_ff_0 = vlp2.trilat_scaleable_ff((TX1_location, TX2_location, TX3_location, TX4_location), 4, Dz)
        self.vlp2_amp2d_ff_0 = vlp2.amp2d_ff(TXn_ampl, Dz, lam_order, (CtCr), 1, 1, 1, 1, 90, tx_number)
        self.vlc_channel_relative_0_2 = vlc.channel_relative(angle4, angle4, distance4, lam_order, 1, 1, 90, CtCr[3], 1)
        self.vlc_channel_relative_0_1 = vlc.channel_relative(angle3, angle3, distance3, lam_order, 1, 1, 90, CtCr[2], 1)
        self.vlc_channel_relative_0_0 = vlc.channel_relative(angle2, angle2, distance2, lam_order, 1, 1, 90, CtCr[1], 1)
        self.vlc_channel_relative_0 = vlc.channel_relative(angle1, angle1, distance1, lam_order, 1, 1, 90, CtCr[0], 1)
        self.qtgui_number_sink_0_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            2
        )
        self.qtgui_number_sink_0_1.set_update_time(0.10)
        self.qtgui_number_sink_0_1.set_title("")
        
        labels = ["X Estimate", "Y Estimate", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(2):
            self.qtgui_number_sink_0_1.set_min(i, -1)
            self.qtgui_number_sink_0_1.set_max(i, 1)
            self.qtgui_number_sink_0_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_1.set_label(i, labels[i])
            self.qtgui_number_sink_0_1.set_unit(i, units[i])
            self.qtgui_number_sink_0_1.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_1.enable_autoscale(False)
        self._qtgui_number_sink_0_1_win = sip.wrapinstance(self.qtgui_number_sink_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_1_win)
        self.goertzel_fc_0_2 = fft.goertzel_fc(samp_rate, goertzel_size, TX2_f)
        self.goertzel_fc_0_1 = fft.goertzel_fc(samp_rate, goertzel_size, TX3_f)
        self.goertzel_fc_0_0 = fft.goertzel_fc(samp_rate, goertzel_size, TX4_f)
        self.goertzel_fc_0 = fft.goertzel_fc(samp_rate, goertzel_size, TX1_f)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_vff((2, ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vff((2, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((2, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((2, ))
        self.blocks_float_to_complex_1_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_complex_to_mag_0_2 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0_1 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_3 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, TX3_f, TXn_ampl, 0)
        self.analog_sig_source_x_2 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, TX4_f, TXn_ampl, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, TX2_f, TXn_ampl, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, TX1_f, TXn_ampl, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise, 0)
        self.analog_const_source_x_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, y_var)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, x_var)
        self.Position = qtgui.const_sink_c(
        	1024, #size
        	"Receiver (2D) Position", #name
        	2 #number of inputs
        )
        self.Position.set_update_time(.01)
        self.Position.set_y_axis(0, 1.5)
        self.Position.set_x_axis(0, 1.5)
        self.Position.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.Position.enable_autoscale(False)
        self.Position.enable_grid(True)
        self.Position.enable_axis_labels(True)
        
        if not True:
          self.Position.disable_legend()
        
        labels = ["X position", "Y position", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.Position.set_line_label(i, "Data {0}".format(i))
            else:
                self.Position.set_line_label(i, labels[i])
            self.Position.set_line_width(i, widths[i])
            self.Position.set_line_color(i, colors[i])
            self.Position.set_line_style(i, styles[i])
            self.Position.set_line_marker(i, markers[i])
            self.Position.set_line_alpha(i, alphas[i])
        
        self._Position_win = sip.wrapinstance(self.Position.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._Position_win)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_1_0, 0))    
        self.connect((self.analog_const_source_x_1, 0), (self.blocks_float_to_complex_1_0, 1))    
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 4))    
        self.connect((self.analog_sig_source_x_0, 0), (self.vlc_channel_relative_0, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.vlc_channel_relative_0_0, 0))    
        self.connect((self.analog_sig_source_x_2, 0), (self.vlc_channel_relative_0_2, 0))    
        self.connect((self.analog_sig_source_x_3, 0), (self.vlc_channel_relative_0_1, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.goertzel_fc_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.goertzel_fc_0_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.goertzel_fc_0_1, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.goertzel_fc_0_2, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_complex_to_mag_0_0, 0), (self.blocks_multiply_const_vxx_0_2, 0))    
        self.connect((self.blocks_complex_to_mag_0_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))    
        self.connect((self.blocks_complex_to_mag_0_2, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_float_to_complex_1, 0), (self.Position, 1))    
        self.connect((self.blocks_float_to_complex_1_0, 0), (self.blocks_throttle_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.vlp2_amp2d_ff_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.vlp2_amp2d_ff_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.vlp2_amp2d_ff_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.vlp2_amp2d_ff_0, 3))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_throttle_1, 0), (self.Position, 0))    
        self.connect((self.goertzel_fc_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.goertzel_fc_0_0, 0), (self.blocks_complex_to_mag_0_0, 0))    
        self.connect((self.goertzel_fc_0_1, 0), (self.blocks_complex_to_mag_0_1, 0))    
        self.connect((self.goertzel_fc_0_2, 0), (self.blocks_complex_to_mag_0_2, 0))    
        self.connect((self.vlc_channel_relative_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.vlc_channel_relative_0_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.vlc_channel_relative_0_1, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.vlc_channel_relative_0_2, 0), (self.blocks_add_xx_0, 3))    
        self.connect((self.vlp2_amp2d_ff_0, 0), (self.vlp2_trilat_scaleable_ff_0, 0))    
        self.connect((self.vlp2_amp2d_ff_0, 1), (self.vlp2_trilat_scaleable_ff_0, 1))    
        self.connect((self.vlp2_amp2d_ff_0, 2), (self.vlp2_trilat_scaleable_ff_0, 2))    
        self.connect((self.vlp2_amp2d_ff_0, 3), (self.vlp2_trilat_scaleable_ff_0, 3))    
        self.connect((self.vlp2_trilat_scaleable_ff_0, 0), (self.blocks_float_to_complex_1, 0))    
        self.connect((self.vlp2_trilat_scaleable_ff_0, 1), (self.blocks_float_to_complex_1, 1))    
        self.connect((self.vlp2_trilat_scaleable_ff_0, 2), (self.blocks_null_sink_0, 0))    
        self.connect((self.vlp2_trilat_scaleable_ff_0, 0), (self.qtgui_number_sink_0_1, 0))    
        self.connect((self.vlp2_trilat_scaleable_ff_0, 1), (self.qtgui_number_sink_0_1, 1))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "vlp_simulation_2x2")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_y_var(self):
        return self.y_var

    def set_y_var(self, y_var):
        self.y_var = y_var
        self.set_distance4(numpy.sqrt( (self.x_var-self.TX4_location[0])**2 + (self.y_var-self.TX4_location[1])**2 + self.Dz**2))
        self.set_distance3(numpy.sqrt( (self.x_var-self.TX3_location[0])**2 + (self.y_var-self.TX3_location[1])**2 + self.Dz**2))
        self.set_distance2(numpy.sqrt( (self.x_var-self.TX2_location[0])**2 + (self.y_var-self.TX2_location[1])**2 + self.Dz**2))
        self.set_distance1(numpy.sqrt( (self.x_var-self.TX1_location[0])**2 + (self.y_var-self.TX1_location[1])**2 + self.Dz**2))
        self.analog_const_source_x_1.set_offset(self.y_var)

    def get_x_var(self):
        return self.x_var

    def set_x_var(self, x_var):
        self.x_var = x_var
        self.set_distance4(numpy.sqrt( (self.x_var-self.TX4_location[0])**2 + (self.y_var-self.TX4_location[1])**2 + self.Dz**2))
        self.set_distance3(numpy.sqrt( (self.x_var-self.TX3_location[0])**2 + (self.y_var-self.TX3_location[1])**2 + self.Dz**2))
        self.set_distance2(numpy.sqrt( (self.x_var-self.TX2_location[0])**2 + (self.y_var-self.TX2_location[1])**2 + self.Dz**2))
        self.set_distance1(numpy.sqrt( (self.x_var-self.TX1_location[0])**2 + (self.y_var-self.TX1_location[1])**2 + self.Dz**2))
        self.analog_const_source_x_0.set_offset(self.x_var)

    def get_TX4_location(self):
        return self.TX4_location

    def set_TX4_location(self, TX4_location):
        self.TX4_location = TX4_location
        self.set_distance4(numpy.sqrt( (self.x_var-self.TX4_location[0])**2 + (self.y_var-self.TX4_location[1])**2 + self.Dz**2))

    def get_TX3_location(self):
        return self.TX3_location

    def set_TX3_location(self, TX3_location):
        self.TX3_location = TX3_location
        self.set_distance3(numpy.sqrt( (self.x_var-self.TX3_location[0])**2 + (self.y_var-self.TX3_location[1])**2 + self.Dz**2))

    def get_TX2_location(self):
        return self.TX2_location

    def set_TX2_location(self, TX2_location):
        self.TX2_location = TX2_location
        self.set_distance2(numpy.sqrt( (self.x_var-self.TX2_location[0])**2 + (self.y_var-self.TX2_location[1])**2 + self.Dz**2))

    def get_TX1_location(self):
        return self.TX1_location

    def set_TX1_location(self, TX1_location):
        self.TX1_location = TX1_location
        self.set_distance1(numpy.sqrt( (self.x_var-self.TX1_location[0])**2 + (self.y_var-self.TX1_location[1])**2 + self.Dz**2))

    def get_Dz(self):
        return self.Dz

    def set_Dz(self, Dz):
        self.Dz = Dz
        self.set_distance4(numpy.sqrt( (self.x_var-self.TX4_location[0])**2 + (self.y_var-self.TX4_location[1])**2 + self.Dz**2))
        self.set_distance3(numpy.sqrt( (self.x_var-self.TX3_location[0])**2 + (self.y_var-self.TX3_location[1])**2 + self.Dz**2))
        self.set_distance2(numpy.sqrt( (self.x_var-self.TX2_location[0])**2 + (self.y_var-self.TX2_location[1])**2 + self.Dz**2))
        self.set_distance1(numpy.sqrt( (self.x_var-self.TX1_location[0])**2 + (self.y_var-self.TX1_location[1])**2 + self.Dz**2))
        self.set_angle4((numpy.arccos(  self.Dz/self.distance4  ) ) * (180/math.pi))
        self.set_angle3((numpy.arccos(  self.Dz/self.distance3 ) ) * (180/math.pi))
        self.set_angle2((numpy.arccos(  self.Dz/self.distance2  ) ) * (180/math.pi))
        self.set_angle1((numpy.arccos(  self.Dz/self.distance1  ) ) * (180/math.pi))

    def get_distance4(self):
        return self.distance4

    def set_distance4(self, distance4):
        self.distance4 = distance4
        self.set_angle4((numpy.arccos(  self.Dz/self.distance4  ) ) * (180/math.pi))
        self.vlc_channel_relative_0_2.set_d(self.distance4)

    def get_distance3(self):
        return self.distance3

    def set_distance3(self, distance3):
        self.distance3 = distance3
        self.set_angle3((numpy.arccos(  self.Dz/self.distance3 ) ) * (180/math.pi))
        self.vlc_channel_relative_0_1.set_d(self.distance3)

    def get_distance2(self):
        return self.distance2

    def set_distance2(self, distance2):
        self.distance2 = distance2
        self.set_angle2((numpy.arccos(  self.Dz/self.distance2  ) ) * (180/math.pi))
        self.vlc_channel_relative_0_0.set_d(self.distance2)

    def get_distance1(self):
        return self.distance1

    def set_distance1(self, distance1):
        self.distance1 = distance1
        self.set_angle1((numpy.arccos(  self.Dz/self.distance1  ) ) * (180/math.pi))
        self.vlc_channel_relative_0.set_d(self.distance1)

    def get_tx_number(self):
        return self.tx_number

    def set_tx_number(self, tx_number):
        self.tx_number = tx_number

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.goertzel_fc_0_2.set_rate(self.samp_rate)
        self.goertzel_fc_0_1.set_rate(self.samp_rate)
        self.goertzel_fc_0_0.set_rate(self.samp_rate)
        self.goertzel_fc_0.set_rate(self.samp_rate)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_3.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.analog_noise_source_x_0.set_amplitude(self.noise)

    def get_lam_order(self):
        return self.lam_order

    def set_lam_order(self, lam_order):
        self.lam_order = lam_order

    def get_goertzel_size(self):
        return self.goertzel_size

    def set_goertzel_size(self, goertzel_size):
        self.goertzel_size = goertzel_size

    def get_angle4(self):
        return self.angle4

    def set_angle4(self, angle4):
        self.angle4 = angle4
        self.vlc_channel_relative_0_2.set_phi(self.angle4)
        self.vlc_channel_relative_0_2.set_psi(self.angle4)

    def get_angle3(self):
        return self.angle3

    def set_angle3(self, angle3):
        self.angle3 = angle3
        self.vlc_channel_relative_0_1.set_phi(self.angle3)
        self.vlc_channel_relative_0_1.set_psi(self.angle3)

    def get_angle2(self):
        return self.angle2

    def set_angle2(self, angle2):
        self.angle2 = angle2
        self.vlc_channel_relative_0_0.set_phi(self.angle2)
        self.vlc_channel_relative_0_0.set_psi(self.angle2)

    def get_angle1(self):
        return self.angle1

    def set_angle1(self, angle1):
        self.angle1 = angle1
        self.vlc_channel_relative_0.set_phi(self.angle1)
        self.vlc_channel_relative_0.set_psi(self.angle1)

    def get_TXn_ampl(self):
        return self.TXn_ampl

    def set_TXn_ampl(self, TXn_ampl):
        self.TXn_ampl = TXn_ampl
        self.analog_sig_source_x_3.set_amplitude(self.TXn_ampl)
        self.analog_sig_source_x_2.set_amplitude(self.TXn_ampl)
        self.analog_sig_source_x_1.set_amplitude(self.TXn_ampl)
        self.analog_sig_source_x_0.set_amplitude(self.TXn_ampl)

    def get_TX4_f(self):
        return self.TX4_f

    def set_TX4_f(self, TX4_f):
        self.TX4_f = TX4_f
        self.goertzel_fc_0_0.set_freq(self.TX4_f)
        self.analog_sig_source_x_2.set_frequency(self.TX4_f)

    def get_TX3_f(self):
        return self.TX3_f

    def set_TX3_f(self, TX3_f):
        self.TX3_f = TX3_f
        self.goertzel_fc_0_1.set_freq(self.TX3_f)
        self.analog_sig_source_x_3.set_frequency(self.TX3_f)

    def get_TX2_f(self):
        return self.TX2_f

    def set_TX2_f(self, TX2_f):
        self.TX2_f = TX2_f
        self.goertzel_fc_0_2.set_freq(self.TX2_f)
        self.analog_sig_source_x_1.set_frequency(self.TX2_f)

    def get_TX1_f(self):
        return self.TX1_f

    def set_TX1_f(self, TX1_f):
        self.TX1_f = TX1_f
        self.goertzel_fc_0.set_freq(self.TX1_f)
        self.analog_sig_source_x_0.set_frequency(self.TX1_f)

    def get_CtCr(self):
        return self.CtCr

    def set_CtCr(self, CtCr):
        self.CtCr = CtCr


def main(top_block_cls=vlp_simulation_2x2, options=None):

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
