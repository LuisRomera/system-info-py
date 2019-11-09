from logger import logger
from matplotlib import pyplot as plt

from config.desing import font_label, font_temp, font_load
from config.environment import get_config


class FigureMain:

    def __init__(self, fig=None):
        self.env = get_config()
        logger.info("")

        self.fig = plt.Figure(facecolor='black', figsize=(4, 2), dpi=100)
        self.fig.text(0, 0.9, 'CPU ', fontdict=font_label)
        text_a_temp = self.fig.text(0.5, 0.9, 'Temp: ', fontdict=font_temp)
        text_a_load = self.fig.text(0.13, 0.9, 'Load: ', fontdict=font_load)

        self.ax1 = self.fig.add_subplot(111)
        self.ax1.patch.set_facecolor('black')
        self.ax1.spines['left'].set_color('white')
        self.ax1.spines['bottom'].set_color('white')
        self.ax1.tick_params(axis='x', colors='white')
        self.ax1.tick_params(axis='y', colors='white')
        line_temp, = self.ax1.plot([], [], lw=1, color='red')
        line_load, = self.ax1.plot([], [], lw=1, color='deepskyblue')
        line_clock, = self.ax1.plot([], [], lw=1, color='green')
        self.lines = [line_temp, line_load, line_clock]
        self.ax1.set_ylim(0, 110)
        self.ax1.set_xlim(0, self.env['max_time'])




