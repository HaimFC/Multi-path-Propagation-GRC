#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.7.14.0
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
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import scipy.constants
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.wall_2_distance_t = wall_2_distance_t = 10
        self.wall_2_distance_r = wall_2_distance_r = 10
        self.distance = distance = 10
        self.wall_1_distance_r = wall_1_distance_r = 10
        self.d_tag = d_tag = numpy.sqrt(numpy.square(distance) - numpy.square(wall_2_distance_r - wall_2_distance_t))
        self.y = y = d_tag * wall_2_distance_t/(wall_2_distance_r+wall_1_distance_r)
        self.x = x = d_tag * wall_1_distance_r/(wall_2_distance_r+wall_1_distance_r)
        self.ant_hight_t = ant_hight_t = 10
        self.z2 = z2 = ant_hight_t*x/d_tag
        self.z1 = z1 = ant_hight_t*(d_tag - (x+y))/d_tag
        self.d = d = distance
        self.ant_hight_r = ant_hight_r = 10
        self.ant_gain_t = ant_gain_t = 1
        self.ant_gain_r = ant_gain_r = 1
        self.a = a = (d_tag*wall_2_distance_r)/(wall_2_distance_t+wall_2_distance_r)
        self.z = z = ant_hight_t*a/d_tag
        self.hp2 = hp2 = ant_hight_r+z2
        self.hp1 = hp1 = ant_hight_r+z1+z2
        self.cos_theta = cos_theta = d/(numpy.sqrt(numpy.square(ant_gain_t-ant_gain_r )+numpy.square(distance)))
        self.frequency = frequency = 900000000
        self.WG_distance = WG_distance = (numpy.sqrt(numpy.square(ant_hight_r-ant_hight_t-z)+numpy.square(d-a)) + numpy.sqrt(numpy.square(z+2*ant_hight_r)+numpy.square(a)))/cos_theta
        self.TW_distance = TW_distance = (numpy.sqrt(numpy.square(y) + numpy.square(ant_hight_t+hp1))+numpy.sqrt(numpy.square(d-(x+y))+numpy.square(hp1+hp2)) + numpy.sqrt(numpy.square(x) + numpy.square(ant_hight_r + hp2)))/cos_theta
        self.SW_distance = SW_distance = (numpy.sqrt(numpy.square(ant_hight_r-ant_hight_t-z)+numpy.square(d-a)) + numpy.sqrt(numpy.square(z)+numpy.square(a)))/cos_theta
        self.LOS_distance = LOS_distance = numpy.sqrt(numpy.square(ant_gain_t-ant_gain_r )+numpy.square(distance))
        self.GR_distance = GR_distance = numpy.sqrt(numpy.square(ant_hight_t+ant_hight_r )+numpy.square(distance))
        self.DW_distance = DW_distance = (numpy. sqrt(numpy. square(distance) + numpy. square(wall_2_distance_r + 2 * wall_2_distance_t + wall_1_distance_r)))/cos_theta
        self.wavelength = wavelength = scipy.constants.c/frequency
        self.wall_1_distance_t = wall_1_distance_t = 10
        self.samp_rate = samp_rate = 512e9
        self.WG_delay = WG_delay = WG_distance/scipy.constants.c
        self.TW_delay = TW_delay = TW_distance/scipy.constants.c
        self.SW_delay = SW_delay = SW_distance/scipy.constants.c
        self.LOS_delay = LOS_delay = LOS_distance/scipy.constants.c
        self.GR_delay = GR_delay = GR_distance/scipy.constants.c
        self.DW_delay = DW_delay = DW_distance/scipy.constants.c

        ##################################################
        # Blocks
        ##################################################
        self._frequency_range = Range(1, 6e9, 100, 900000000, 200)
        self._frequency_win = RangeWidget(self._frequency_range, self.set_frequency, "frequency", "counter_slider", float)
        self.top_grid_layout.addWidget(self._frequency_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	4096, #size
        	samp_rate, #samp_rate
        	"", #name
        	10 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label(' Power (W)', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['LOS', 'Ground Reflected\r', 'SW', 'SW', 'WG',
                  'WG', 'DW', 'DW', 'TW', 'Combined']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(10):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self._distance_range = Range(10, 15000, 10, 10, 200)
        self._distance_win = RangeWidget(self._distance_range, self.set_distance, "distance", "counter_slider", float)
        self.top_grid_layout.addWidget(self._distance_win)
        self.blocks_multiply_const_vxx_1_3 = blocks.multiply_const_vff((ant_gain_t*ant_gain_r*numpy.square(wavelength/(4*(numpy.pi)*TW_distance))
        , ))
        self.blocks_multiply_const_vxx_1_2 = blocks.multiply_const_vff((ant_gain_t*ant_gain_r*numpy.square(wavelength/(4*(numpy.pi)*DW_distance))
        , ))
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_vff((ant_gain_t*ant_gain_r*numpy.square(wavelength/(4*(numpy.pi)*WG_distance))
        , ))
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vff((ant_gain_t*ant_gain_r*numpy.square(wavelength/(4*(numpy.pi)*SW_distance))
        , ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((ant_gain_t*ant_gain_r*numpy.square(wavelength/(4*(numpy.pi)*GR_distance))
        , ))
        self.blocks_multiply_const_vxx_0_3 = blocks.multiply_const_vff((ant_gain_t*ant_gain_r*numpy.square(wavelength/(4*(numpy.pi)*TW_distance))
        , ))
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_vff((ant_gain_t*ant_gain_r*numpy.square(wavelength/(4*(numpy.pi)*DW_distance))
        , ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vff((ant_gain_t*ant_gain_r*numpy.square(wavelength/(4*(numpy.pi)*WG_distance))
        , ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((ant_gain_t*ant_gain_r*numpy.square(wavelength/(4*(numpy.pi)*SW_distance))
        , ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((ant_gain_t*ant_gain_r*numpy.square(wavelength/(4*(numpy.pi)*LOS_distance))
        , ))
        self.blocks_delay_2_3 = blocks.delay(gr.sizeof_float*1, int(TW_delay*samp_rate)
        )
        self.blocks_delay_2_2 = blocks.delay(gr.sizeof_float*1, int(DW_delay*samp_rate)
        )
        self.blocks_delay_2_1 = blocks.delay(gr.sizeof_float*1, int(WG_delay*samp_rate)
        )
        self.blocks_delay_2_0_2 = blocks.delay(gr.sizeof_float*1, int(TW_delay*samp_rate)
        )
        self.blocks_delay_2_0_1 = blocks.delay(gr.sizeof_float*1, int(DW_delay*samp_rate)
        )
        self.blocks_delay_2_0_0 = blocks.delay(gr.sizeof_float*1, int(WG_delay*samp_rate)
        )
        self.blocks_delay_2_0 = blocks.delay(gr.sizeof_float*1, int(SW_delay*samp_rate)
        )
        self.blocks_delay_2 = blocks.delay(gr.sizeof_float*1, int(SW_delay*samp_rate)
        )
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1, int(GR_delay*samp_rate)
        )
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, int(LOS_delay*samp_rate)
        )
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, frequency, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_1, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_2, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_2_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_2_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_2_0_1, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_2_0_2, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_2_1, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_2_2, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_2_3, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 9))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_delay_1, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_delay_2, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_delay_2_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.blocks_delay_2_0_0, 0), (self.blocks_multiply_const_vxx_1_1, 0))
        self.connect((self.blocks_delay_2_0_1, 0), (self.blocks_multiply_const_vxx_1_2, 0))
        self.connect((self.blocks_delay_2_0_2, 0), (self.blocks_multiply_const_vxx_1_3, 0))
        self.connect((self.blocks_delay_2_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.blocks_delay_2_2, 0), (self.blocks_multiply_const_vxx_0_2, 0))
        self.connect((self.blocks_delay_2_3, 0), (self.blocks_multiply_const_vxx_0_3, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.qtgui_time_sink_x_0, 4))
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.blocks_add_xx_0, 6))
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.qtgui_time_sink_x_0, 6))
        self.connect((self.blocks_multiply_const_vxx_0_3, 0), (self.blocks_add_xx_0, 8))
        self.connect((self.blocks_multiply_const_vxx_0_3, 0), (self.qtgui_time_sink_x_0, 8))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.blocks_add_xx_0, 5))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.qtgui_time_sink_x_0, 5))
        self.connect((self.blocks_multiply_const_vxx_1_2, 0), (self.blocks_add_xx_0, 7))
        self.connect((self.blocks_multiply_const_vxx_1_2, 0), (self.qtgui_time_sink_x_0, 7))
        self.connect((self.blocks_multiply_const_vxx_1_3, 0), (self.blocks_add_xx_0, 9))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_wall_2_distance_t(self):
        return self.wall_2_distance_t

    def set_wall_2_distance_t(self, wall_2_distance_t):
        self.wall_2_distance_t = wall_2_distance_t
        self.set_DW_distance((numpy. sqrt(numpy. square(self.distance) + numpy. square(self.wall_2_distance_r + 2 * self.wall_2_distance_t + self.wall_1_distance_r)))/self.cos_theta)
        self.set_y(self.d_tag * self.wall_2_distance_t/(self.wall_2_distance_r+self.wall_1_distance_r))
        self.set_d_tag(numpy.sqrt(numpy.square(self.distance) - numpy.square(self.wall_2_distance_r - self.wall_2_distance_t)))
        self.set_a((self.d_tag*self.wall_2_distance_r)/(self.wall_2_distance_t+self.wall_2_distance_r))

    def get_wall_2_distance_r(self):
        return self.wall_2_distance_r

    def set_wall_2_distance_r(self, wall_2_distance_r):
        self.wall_2_distance_r = wall_2_distance_r
        self.set_DW_distance((numpy. sqrt(numpy. square(self.distance) + numpy. square(self.wall_2_distance_r + 2 * self.wall_2_distance_t + self.wall_1_distance_r)))/self.cos_theta)
        self.set_y(self.d_tag * self.wall_2_distance_t/(self.wall_2_distance_r+self.wall_1_distance_r))
        self.set_x(self.d_tag * self.wall_1_distance_r/(self.wall_2_distance_r+self.wall_1_distance_r))
        self.set_d_tag(numpy.sqrt(numpy.square(self.distance) - numpy.square(self.wall_2_distance_r - self.wall_2_distance_t)))
        self.set_a((self.d_tag*self.wall_2_distance_r)/(self.wall_2_distance_t+self.wall_2_distance_r))

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance
        self.set_LOS_distance(numpy.sqrt(numpy.square(self.ant_gain_t-self.ant_gain_r )+numpy.square(self.distance)))
        self.set_GR_distance(numpy.sqrt(numpy.square(self.ant_hight_t+self.ant_hight_r )+numpy.square(self.distance))
        )
        self.set_DW_distance((numpy. sqrt(numpy. square(self.distance) + numpy. square(self.wall_2_distance_r + 2 * self.wall_2_distance_t + self.wall_1_distance_r)))/self.cos_theta)
        self.set_d_tag(numpy.sqrt(numpy.square(self.distance) - numpy.square(self.wall_2_distance_r - self.wall_2_distance_t)))
        self.set_d(self.distance)
        self.set_cos_theta(self.d/(numpy.sqrt(numpy.square(self.ant_gain_t-self.ant_gain_r )+numpy.square(self.distance))))

    def get_wall_1_distance_r(self):
        return self.wall_1_distance_r

    def set_wall_1_distance_r(self, wall_1_distance_r):
        self.wall_1_distance_r = wall_1_distance_r
        self.set_DW_distance((numpy. sqrt(numpy. square(self.distance) + numpy. square(self.wall_2_distance_r + 2 * self.wall_2_distance_t + self.wall_1_distance_r)))/self.cos_theta)
        self.set_y(self.d_tag * self.wall_2_distance_t/(self.wall_2_distance_r+self.wall_1_distance_r))
        self.set_x(self.d_tag * self.wall_1_distance_r/(self.wall_2_distance_r+self.wall_1_distance_r))

    def get_d_tag(self):
        return self.d_tag

    def set_d_tag(self, d_tag):
        self.d_tag = d_tag
        self.set_z2(self.ant_hight_t*self.x/self.d_tag)
        self.set_z1(self.ant_hight_t*(self.d_tag - (self.x+self.y))/self.d_tag)
        self.set_z(self.ant_hight_t*self.a/self.d_tag)
        self.set_y(self.d_tag * self.wall_2_distance_t/(self.wall_2_distance_r+self.wall_1_distance_r))
        self.set_x(self.d_tag * self.wall_1_distance_r/(self.wall_2_distance_r+self.wall_1_distance_r))
        self.set_a((self.d_tag*self.wall_2_distance_r)/(self.wall_2_distance_t+self.wall_2_distance_r))

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y
        self.set_TW_distance((numpy.sqrt(numpy.square(self.y) + numpy.square(self.ant_hight_t+self.hp1))+numpy.sqrt(numpy.square(self.d-(self.x+self.y))+numpy.square(self.hp1+self.hp2)) + numpy.sqrt(numpy.square(self.x) + numpy.square(self.ant_hight_r + self.hp2)))/self.cos_theta)
        self.set_z1(self.ant_hight_t*(self.d_tag - (self.x+self.y))/self.d_tag)

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x
        self.set_TW_distance((numpy.sqrt(numpy.square(self.y) + numpy.square(self.ant_hight_t+self.hp1))+numpy.sqrt(numpy.square(self.d-(self.x+self.y))+numpy.square(self.hp1+self.hp2)) + numpy.sqrt(numpy.square(self.x) + numpy.square(self.ant_hight_r + self.hp2)))/self.cos_theta)
        self.set_z2(self.ant_hight_t*self.x/self.d_tag)
        self.set_z1(self.ant_hight_t*(self.d_tag - (self.x+self.y))/self.d_tag)

    def get_ant_hight_t(self):
        return self.ant_hight_t

    def set_ant_hight_t(self, ant_hight_t):
        self.ant_hight_t = ant_hight_t
        self.set_WG_distance((numpy.sqrt(numpy.square(self.ant_hight_r-self.ant_hight_t-self.z)+numpy.square(self.d-self.a)) + numpy.sqrt(numpy.square(self.z+2*self.ant_hight_r)+numpy.square(self.a)))/self.cos_theta)
        self.set_TW_distance((numpy.sqrt(numpy.square(self.y) + numpy.square(self.ant_hight_t+self.hp1))+numpy.sqrt(numpy.square(self.d-(self.x+self.y))+numpy.square(self.hp1+self.hp2)) + numpy.sqrt(numpy.square(self.x) + numpy.square(self.ant_hight_r + self.hp2)))/self.cos_theta)
        self.set_SW_distance((numpy.sqrt(numpy.square(self.ant_hight_r-self.ant_hight_t-self.z)+numpy.square(self.d-self.a)) + numpy.sqrt(numpy.square(self.z)+numpy.square(self.a)))/self.cos_theta)
        self.set_GR_distance(numpy.sqrt(numpy.square(self.ant_hight_t+self.ant_hight_r )+numpy.square(self.distance))
        )
        self.set_z2(self.ant_hight_t*self.x/self.d_tag)
        self.set_z1(self.ant_hight_t*(self.d_tag - (self.x+self.y))/self.d_tag)
        self.set_z(self.ant_hight_t*self.a/self.d_tag)

    def get_z2(self):
        return self.z2

    def set_z2(self, z2):
        self.z2 = z2
        self.set_hp2(self.ant_hight_r+self.z2)
        self.set_hp1(self.ant_hight_r+self.z1+self.z2)

    def get_z1(self):
        return self.z1

    def set_z1(self, z1):
        self.z1 = z1
        self.set_hp1(self.ant_hight_r+self.z1+self.z2)

    def get_d(self):
        return self.d

    def set_d(self, d):
        self.d = d
        self.set_WG_distance((numpy.sqrt(numpy.square(self.ant_hight_r-self.ant_hight_t-self.z)+numpy.square(self.d-self.a)) + numpy.sqrt(numpy.square(self.z+2*self.ant_hight_r)+numpy.square(self.a)))/self.cos_theta)
        self.set_TW_distance((numpy.sqrt(numpy.square(self.y) + numpy.square(self.ant_hight_t+self.hp1))+numpy.sqrt(numpy.square(self.d-(self.x+self.y))+numpy.square(self.hp1+self.hp2)) + numpy.sqrt(numpy.square(self.x) + numpy.square(self.ant_hight_r + self.hp2)))/self.cos_theta)
        self.set_SW_distance((numpy.sqrt(numpy.square(self.ant_hight_r-self.ant_hight_t-self.z)+numpy.square(self.d-self.a)) + numpy.sqrt(numpy.square(self.z)+numpy.square(self.a)))/self.cos_theta)
        self.set_cos_theta(self.d/(numpy.sqrt(numpy.square(self.ant_gain_t-self.ant_gain_r )+numpy.square(self.distance))))

    def get_ant_hight_r(self):
        return self.ant_hight_r

    def set_ant_hight_r(self, ant_hight_r):
        self.ant_hight_r = ant_hight_r
        self.set_WG_distance((numpy.sqrt(numpy.square(self.ant_hight_r-self.ant_hight_t-self.z)+numpy.square(self.d-self.a)) + numpy.sqrt(numpy.square(self.z+2*self.ant_hight_r)+numpy.square(self.a)))/self.cos_theta)
        self.set_TW_distance((numpy.sqrt(numpy.square(self.y) + numpy.square(self.ant_hight_t+self.hp1))+numpy.sqrt(numpy.square(self.d-(self.x+self.y))+numpy.square(self.hp1+self.hp2)) + numpy.sqrt(numpy.square(self.x) + numpy.square(self.ant_hight_r + self.hp2)))/self.cos_theta)
        self.set_SW_distance((numpy.sqrt(numpy.square(self.ant_hight_r-self.ant_hight_t-self.z)+numpy.square(self.d-self.a)) + numpy.sqrt(numpy.square(self.z)+numpy.square(self.a)))/self.cos_theta)
        self.set_GR_distance(numpy.sqrt(numpy.square(self.ant_hight_t+self.ant_hight_r )+numpy.square(self.distance))
        )
        self.set_hp2(self.ant_hight_r+self.z2)
        self.set_hp1(self.ant_hight_r+self.z1+self.z2)

    def get_ant_gain_t(self):
        return self.ant_gain_t

    def set_ant_gain_t(self, ant_gain_t):
        self.ant_gain_t = ant_gain_t
        self.set_LOS_distance(numpy.sqrt(numpy.square(self.ant_gain_t-self.ant_gain_r )+numpy.square(self.distance)))
        self.set_cos_theta(self.d/(numpy.sqrt(numpy.square(self.ant_gain_t-self.ant_gain_r )+numpy.square(self.distance))))
        self.blocks_multiply_const_vxx_1_3.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.TW_distance))
        , ))
        self.blocks_multiply_const_vxx_1_2.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.DW_distance))
        , ))
        self.blocks_multiply_const_vxx_1_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.WG_distance))
        , ))
        self.blocks_multiply_const_vxx_1_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.SW_distance))
        , ))
        self.blocks_multiply_const_vxx_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.GR_distance))
        , ))
        self.blocks_multiply_const_vxx_0_3.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.TW_distance))
        , ))
        self.blocks_multiply_const_vxx_0_2.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.DW_distance))
        , ))
        self.blocks_multiply_const_vxx_0_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.WG_distance))
        , ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.SW_distance))
        , ))
        self.blocks_multiply_const_vxx_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.LOS_distance))
        , ))

    def get_ant_gain_r(self):
        return self.ant_gain_r

    def set_ant_gain_r(self, ant_gain_r):
        self.ant_gain_r = ant_gain_r
        self.set_LOS_distance(numpy.sqrt(numpy.square(self.ant_gain_t-self.ant_gain_r )+numpy.square(self.distance)))
        self.set_cos_theta(self.d/(numpy.sqrt(numpy.square(self.ant_gain_t-self.ant_gain_r )+numpy.square(self.distance))))
        self.blocks_multiply_const_vxx_1_3.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.TW_distance))
        , ))
        self.blocks_multiply_const_vxx_1_2.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.DW_distance))
        , ))
        self.blocks_multiply_const_vxx_1_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.WG_distance))
        , ))
        self.blocks_multiply_const_vxx_1_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.SW_distance))
        , ))
        self.blocks_multiply_const_vxx_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.GR_distance))
        , ))
        self.blocks_multiply_const_vxx_0_3.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.TW_distance))
        , ))
        self.blocks_multiply_const_vxx_0_2.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.DW_distance))
        , ))
        self.blocks_multiply_const_vxx_0_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.WG_distance))
        , ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.SW_distance))
        , ))
        self.blocks_multiply_const_vxx_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.LOS_distance))
        , ))

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a
        self.set_WG_distance((numpy.sqrt(numpy.square(self.ant_hight_r-self.ant_hight_t-self.z)+numpy.square(self.d-self.a)) + numpy.sqrt(numpy.square(self.z+2*self.ant_hight_r)+numpy.square(self.a)))/self.cos_theta)
        self.set_SW_distance((numpy.sqrt(numpy.square(self.ant_hight_r-self.ant_hight_t-self.z)+numpy.square(self.d-self.a)) + numpy.sqrt(numpy.square(self.z)+numpy.square(self.a)))/self.cos_theta)
        self.set_z(self.ant_hight_t*self.a/self.d_tag)

    def get_z(self):
        return self.z

    def set_z(self, z):
        self.z = z
        self.set_WG_distance((numpy.sqrt(numpy.square(self.ant_hight_r-self.ant_hight_t-self.z)+numpy.square(self.d-self.a)) + numpy.sqrt(numpy.square(self.z+2*self.ant_hight_r)+numpy.square(self.a)))/self.cos_theta)
        self.set_SW_distance((numpy.sqrt(numpy.square(self.ant_hight_r-self.ant_hight_t-self.z)+numpy.square(self.d-self.a)) + numpy.sqrt(numpy.square(self.z)+numpy.square(self.a)))/self.cos_theta)

    def get_hp2(self):
        return self.hp2

    def set_hp2(self, hp2):
        self.hp2 = hp2
        self.set_TW_distance((numpy.sqrt(numpy.square(self.y) + numpy.square(self.ant_hight_t+self.hp1))+numpy.sqrt(numpy.square(self.d-(self.x+self.y))+numpy.square(self.hp1+self.hp2)) + numpy.sqrt(numpy.square(self.x) + numpy.square(self.ant_hight_r + self.hp2)))/self.cos_theta)

    def get_hp1(self):
        return self.hp1

    def set_hp1(self, hp1):
        self.hp1 = hp1
        self.set_TW_distance((numpy.sqrt(numpy.square(self.y) + numpy.square(self.ant_hight_t+self.hp1))+numpy.sqrt(numpy.square(self.d-(self.x+self.y))+numpy.square(self.hp1+self.hp2)) + numpy.sqrt(numpy.square(self.x) + numpy.square(self.ant_hight_r + self.hp2)))/self.cos_theta)

    def get_cos_theta(self):
        return self.cos_theta

    def set_cos_theta(self, cos_theta):
        self.cos_theta = cos_theta
        self.set_WG_distance((numpy.sqrt(numpy.square(self.ant_hight_r-self.ant_hight_t-self.z)+numpy.square(self.d-self.a)) + numpy.sqrt(numpy.square(self.z+2*self.ant_hight_r)+numpy.square(self.a)))/self.cos_theta)
        self.set_TW_distance((numpy.sqrt(numpy.square(self.y) + numpy.square(self.ant_hight_t+self.hp1))+numpy.sqrt(numpy.square(self.d-(self.x+self.y))+numpy.square(self.hp1+self.hp2)) + numpy.sqrt(numpy.square(self.x) + numpy.square(self.ant_hight_r + self.hp2)))/self.cos_theta)
        self.set_SW_distance((numpy.sqrt(numpy.square(self.ant_hight_r-self.ant_hight_t-self.z)+numpy.square(self.d-self.a)) + numpy.sqrt(numpy.square(self.z)+numpy.square(self.a)))/self.cos_theta)
        self.set_DW_distance((numpy. sqrt(numpy. square(self.distance) + numpy. square(self.wall_2_distance_r + 2 * self.wall_2_distance_t + self.wall_1_distance_r)))/self.cos_theta)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.set_wavelength(scipy.constants.c/self.frequency)
        self.analog_sig_source_x_0.set_frequency(self.frequency)

    def get_WG_distance(self):
        return self.WG_distance

    def set_WG_distance(self, WG_distance):
        self.WG_distance = WG_distance
        self.set_WG_delay(self.WG_distance/scipy.constants.c)
        self.blocks_multiply_const_vxx_1_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.WG_distance))
        , ))
        self.blocks_multiply_const_vxx_0_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.WG_distance))
        , ))

    def get_TW_distance(self):
        return self.TW_distance

    def set_TW_distance(self, TW_distance):
        self.TW_distance = TW_distance
        self.set_TW_delay(self.TW_distance/scipy.constants.c)
        self.blocks_multiply_const_vxx_1_3.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.TW_distance))
        , ))
        self.blocks_multiply_const_vxx_0_3.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.TW_distance))
        , ))

    def get_SW_distance(self):
        return self.SW_distance

    def set_SW_distance(self, SW_distance):
        self.SW_distance = SW_distance
        self.set_SW_delay(self.SW_distance/scipy.constants.c)
        self.blocks_multiply_const_vxx_1_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.SW_distance))
        , ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.SW_distance))
        , ))

    def get_LOS_distance(self):
        return self.LOS_distance

    def set_LOS_distance(self, LOS_distance):
        self.LOS_distance = LOS_distance
        self.set_LOS_delay(self.LOS_distance/scipy.constants.c)
        self.blocks_multiply_const_vxx_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.LOS_distance))
        , ))

    def get_GR_distance(self):
        return self.GR_distance

    def set_GR_distance(self, GR_distance):
        self.GR_distance = GR_distance
        self.set_GR_delay(self.GR_distance/scipy.constants.c)
        self.blocks_multiply_const_vxx_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.GR_distance))
        , ))

    def get_DW_distance(self):
        return self.DW_distance

    def set_DW_distance(self, DW_distance):
        self.DW_distance = DW_distance
        self.set_DW_delay(self.DW_distance/scipy.constants.c)
        self.blocks_multiply_const_vxx_1_2.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.DW_distance))
        , ))
        self.blocks_multiply_const_vxx_0_2.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.DW_distance))
        , ))

    def get_wavelength(self):
        return self.wavelength

    def set_wavelength(self, wavelength):
        self.wavelength = wavelength
        self.blocks_multiply_const_vxx_1_3.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.TW_distance))
        , ))
        self.blocks_multiply_const_vxx_1_2.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.DW_distance))
        , ))
        self.blocks_multiply_const_vxx_1_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.WG_distance))
        , ))
        self.blocks_multiply_const_vxx_1_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.SW_distance))
        , ))
        self.blocks_multiply_const_vxx_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.GR_distance))
        , ))
        self.blocks_multiply_const_vxx_0_3.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.TW_distance))
        , ))
        self.blocks_multiply_const_vxx_0_2.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.DW_distance))
        , ))
        self.blocks_multiply_const_vxx_0_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.WG_distance))
        , ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.SW_distance))
        , ))
        self.blocks_multiply_const_vxx_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.LOS_distance))
        , ))

    def get_wall_1_distance_t(self):
        return self.wall_1_distance_t

    def set_wall_1_distance_t(self, wall_1_distance_t):
        self.wall_1_distance_t = wall_1_distance_t

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_delay_2_3.set_dly(int(self.TW_delay*self.samp_rate)
        )
        self.blocks_delay_2_2.set_dly(int(self.DW_delay*self.samp_rate)
        )
        self.blocks_delay_2_1.set_dly(int(self.WG_delay*self.samp_rate)
        )
        self.blocks_delay_2_0_2.set_dly(int(self.TW_delay*self.samp_rate)
        )
        self.blocks_delay_2_0_1.set_dly(int(self.DW_delay*self.samp_rate)
        )
        self.blocks_delay_2_0_0.set_dly(int(self.WG_delay*self.samp_rate)
        )
        self.blocks_delay_2_0.set_dly(int(self.SW_delay*self.samp_rate)
        )
        self.blocks_delay_2.set_dly(int(self.SW_delay*self.samp_rate)
        )
        self.blocks_delay_1.set_dly(int(self.GR_delay*self.samp_rate)
        )
        self.blocks_delay_0.set_dly(int(self.LOS_delay*self.samp_rate)
        )
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_WG_delay(self):
        return self.WG_delay

    def set_WG_delay(self, WG_delay):
        self.WG_delay = WG_delay
        self.blocks_delay_2_1.set_dly(int(self.WG_delay*self.samp_rate)
        )
        self.blocks_delay_2_0_0.set_dly(int(self.WG_delay*self.samp_rate)
        )

    def get_TW_delay(self):
        return self.TW_delay

    def set_TW_delay(self, TW_delay):
        self.TW_delay = TW_delay
        self.blocks_delay_2_3.set_dly(int(self.TW_delay*self.samp_rate)
        )
        self.blocks_delay_2_0_2.set_dly(int(self.TW_delay*self.samp_rate)
        )

    def get_SW_delay(self):
        return self.SW_delay

    def set_SW_delay(self, SW_delay):
        self.SW_delay = SW_delay
        self.blocks_delay_2_0.set_dly(int(self.SW_delay*self.samp_rate)
        )
        self.blocks_delay_2.set_dly(int(self.SW_delay*self.samp_rate)
        )

    def get_LOS_delay(self):
        return self.LOS_delay

    def set_LOS_delay(self, LOS_delay):
        self.LOS_delay = LOS_delay
        self.blocks_delay_0.set_dly(int(self.LOS_delay*self.samp_rate)
        )

    def get_GR_delay(self):
        return self.GR_delay

    def set_GR_delay(self, GR_delay):
        self.GR_delay = GR_delay
        self.blocks_delay_1.set_dly(int(self.GR_delay*self.samp_rate)
        )

    def get_DW_delay(self):
        return self.DW_delay

    def set_DW_delay(self, DW_delay):
        self.DW_delay = DW_delay
        self.blocks_delay_2_2.set_dly(int(self.DW_delay*self.samp_rate)
        )
        self.blocks_delay_2_0_1.set_dly(int(self.DW_delay*self.samp_rate)
        )


def main(top_block_cls=top_block, options=None):

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
