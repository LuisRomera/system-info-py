from tkinter import Canvas

import matplotlib.pyplot as plt

from config.desing import font_label, font_normal


class TableText:
    def __init__(self, name=None, list_table=None):
        self.fig = plt.Figure(facecolor='black', figsize=(3, 2.2), dpi=110)
        self.fig.text(0.4, 0.9, name, fontdict=font_label)
        self.text_cpu = []

        count = 0
        count_h = 0
        for x in list_table.load:
            count += 1
            count_h += 1
            count_w = int((count) / 12)
            if count == 12:
                count_w = 0
            if count == 24:
                count_w = 1

            self.text_cpu.append(self.fig.text(count_w * 0.5 + 0.05, 0.9 - count_h * 0.07,
                                               'core ' + str(count) + ': ' + str(int(x.value)) + '%',
                                               fontdict=font_normal))
            if count == 12:
                count_h = 0

            if count == 24:
                count_h = 1
        # list(map(lambda x: self.fig.text(0.05, 0.9, x, fontdict=list_table)))
        # self.cores =
        # self.fig.text(0.05, 0.9, name, fontdict=font_normal)

        # self.text_temp = self.fig.text(0.5, 0.9, 'Texto: ', fontdict=font_temp)
