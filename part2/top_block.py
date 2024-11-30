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
        self.distance = distance = 10
        self.ant_hight_t = ant_hight_t = 10
        self.ant_hight_r = ant_hight_r = 10
        self.frequency = frequency = 900000000
        self.LOS_distance = LOS_distance = numpy.sqrt(numpy.square(ant_hight_t-ant_hight_r )+numpy.square(distance))
        self.GR_distance = GR_distance = numpy.sqrt(numpy.square(ant_hight_t+ant_hight_r )+numpy.square(distance))
        self.wavelength = wavelength = scipy.constants.c/frequency
        self.samp_rate = samp_rate = 512e9
        self.ant_gain_t = ant_gain_t = 1
        self.ant_gain_r = ant_gain_r = 1
        self.LOS_delay = LOS_delay = LOS_distance/scipy.constants.c
        self.GR_delay = GR_delay = GR_distance/scipy.constants.c

        ##################################################
        # Blocks
        ##################################################
        self._frequency_range = Range(1, 6e9, 100, 900000000, 200)
        self._frequency_win = RangeWidget(self._frequency_range, self.set_frequency, "frequency", "counter_slider", float)
        self.top_grid_layout.addWidget(self._frequency_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	3 #number of inputs
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

        labels = ['LOS', 'Ground Reflected\r', 'Combined', '', '',
                  '', '', '', '', '']
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

        for i in xrange(3):
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
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((ant_gain_t*ant_gain_r*numpy.square(wavelength/(4*(numpy.pi)*GR_distance))
        , ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((ant_gain_t*ant_gain_r*numpy.square(wavelength/(4*(numpy.pi)*LOS_distance))
        , ))
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
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_delay_1, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_time_sink_x_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance
        self.set_LOS_distance(numpy.sqrt(numpy.square(self.ant_hight_t-self.ant_hight_r )+numpy.square(self.distance)))
        self.set_GR_distance(numpy.sqrt(numpy.square(self.ant_hight_t+self.ant_hight_r )+numpy.square(self.distance))
        )

    def get_ant_hight_t(self):
        return self.ant_hight_t

    def set_ant_hight_t(self, ant_hight_t):
        self.ant_hight_t = ant_hight_t
        self.set_LOS_distance(numpy.sqrt(numpy.square(self.ant_hight_t-self.ant_hight_r )+numpy.square(self.distance)))
        self.set_GR_distance(numpy.sqrt(numpy.square(self.ant_hight_t+self.ant_hight_r )+numpy.square(self.distance))
        )

    def get_ant_hight_r(self):
        return self.ant_hight_r

    def set_ant_hight_r(self, ant_hight_r):
        self.ant_hight_r = ant_hight_r
        self.set_LOS_distance(numpy.sqrt(numpy.square(self.ant_hight_t-self.ant_hight_r )+numpy.square(self.distance)))
        self.set_GR_distance(numpy.sqrt(numpy.square(self.ant_hight_t+self.ant_hight_r )+numpy.square(self.distance))
        )

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.set_wavelength(scipy.constants.c/self.frequency)
        self.analog_sig_source_x_0.set_frequency(self.frequency)

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

    def get_wavelength(self):
        return self.wavelength

    def set_wavelength(self, wavelength):
        self.wavelength = wavelength
        self.blocks_multiply_const_vxx_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.GR_distance))
        , ))
        self.blocks_multiply_const_vxx_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.LOS_distance))
        , ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_delay_1.set_dly(int(self.GR_delay*self.samp_rate)
        )
        self.blocks_delay_0.set_dly(int(self.LOS_delay*self.samp_rate)
        )
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_ant_gain_t(self):
        return self.ant_gain_t

    def set_ant_gain_t(self, ant_gain_t):
        self.ant_gain_t = ant_gain_t
        self.blocks_multiply_const_vxx_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.GR_distance))
        , ))
        self.blocks_multiply_const_vxx_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.LOS_distance))
        , ))

    def get_ant_gain_r(self):
        return self.ant_gain_r

    def set_ant_gain_r(self, ant_gain_r):
        self.ant_gain_r = ant_gain_r
        self.blocks_multiply_const_vxx_1.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.GR_distance))
        , ))
        self.blocks_multiply_const_vxx_0.set_k((self.ant_gain_t*self.ant_gain_r*numpy.square(self.wavelength/(4*(numpy.pi)*self.LOS_distance))
        , ))

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
