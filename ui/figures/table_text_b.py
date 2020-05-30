import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.patches import Rectangle

from config.desing import font_label, font_normal, font_small


class TableTextB:
    def __init__(self, name=None, data=None):
        self.fig = plt.Figure(facecolor='black', figsize=(3, 2.1), dpi=110)
        self.fig.text(0.2, 0.93, 'GPU', fontdict=font_label)
        self.text_gpu_menory_use = self.fig.text(0.05, 0.9 - 0.07, 'used memory: ' + str(
            int(100 * data.pc.gpu.memory_use.value / data.pc.gpu.memory_free.value)) + '%', font_normal)
        self.text_gpu_menory_frec = self.fig.text(0.05, 0.9 - 0.07 * 2, 'frec memory: ' + str(
            int(data.pc.gpu.frec_memory.value)) + data.pc.gpu.frec_memory.unit, font_normal)
        self.text_gpu_shader = self.fig.text(0.05, 0.9 - 0.07 * 3,
                                             'shader: ' + str(int(data.pc.gpu.shader.value)) + data.pc.gpu.shader.unit,
                                             font_normal)

        self.fig.text(0.6, 0.93, 'FANS', fontdict=font_label)
        count = 0
        self.fans = []
        for fan in data.pc.fans.all_fans:
            count += 1

            self.fans.append(
                self.fig.text(0.6, 0.9 - count * 0.07, fan.name + ": " + str(fan.speed.value) + fan.speed.unit,
                              font_normal))

        count += 1

        self.pump = self.fig.text(0.6, 0.9 - count * 0.07,
                                  "Pump: " + str(data.pc.pump.all_fans[0].speed.value) +
                                  data.pc.pump.all_fans[0].speed.unit, font_normal)

        count += 1
        self.fig.text(0.6, 0.9 - count * 0.07 - 0.03, 'Storage', fontdict=font_label)

        self.list_storage = []

        self.ax = self.fig.add_axes([0.6, 0, 0.4, 0.36], facecolor='black')
        unit = list(map(lambda s: s.name, data.pc.storage))
        used = list(map(lambda s: int(float(s.used.value)), data.pc.storage))[::-1]

        self.bar = self.ax.barh(unit, used, height=0.9, color='red')
        self.ax.set_xlim(0, 100)

        for storage in data.pc.storage:
            count += 1.2
            self.list_storage.append(self.fig.text(0.62, 0.86 - count * 0.07, storage.name + str(storage.used.value) +
                                                   storage.used.unit, font_small, size=8))
