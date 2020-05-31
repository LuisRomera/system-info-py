import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.patches import Rectangle

from config.desing import font_label, font_normal, font_small, font_storage


class TableTextB:
    def __init__(self, name=None, data=None):
        self.fig = plt.Figure(facecolor='black', figsize=(3, 2.15), dpi=110)
        self.fig.text(0.05, 0.94, 'GPU', fontdict=font_label)
        self.text_gpu_menory_use = self.fig.text(0.05, 0.9 - 0.02, 'used memory: ' + str(
            int(100 * data.pc.gpu.memory_use.value / data.pc.gpu.memory_free.value)) + '%', font_normal)
        self.text_gpu_menory_frec = self.fig.text(0.05, 0.95 - 0.07 * 2, 'frec memory: ' + str(
            int(data.pc.gpu.frec_memory.value)) + data.pc.gpu.frec_memory.unit, font_normal)
        self.text_gpu_shader = self.fig.text(0.05, 0.95 - 0.07 * 3,
                                             'shader: ' + str(int(data.pc.gpu.shader.value)) + data.pc.gpu.shader.unit,
                                             font_normal)

        self.fig.text(0.6, 0.94, 'FANS', fontdict=font_label)
        count = 0
        self.fans = []
        for fan in data.pc.fans.all_fans:
            count += 1
            self.fans.append(
                self.fig.text(0.6, 0.94 - count * 0.07, fan.name + ": " + str(fan.speed.value) + fan.speed.unit,
                              font_normal))

        count += 1

        self.pump = self.fig.text(0.6, 0.94 - count * 0.07,
                                  "Pump: " + str(data.pc.pump.all_fans[0].speed.value) +
                                  data.pc.pump.all_fans[0].speed.unit, font_normal)


        count += 1

        self.fig.text(0.6, 0.94 - count * 0.07 - 0.03, 'Storage', fontdict=font_label)
        self.list_storage = []

        self.ax = self.fig.add_axes([0.6, 0.01, 0.39, 0.38], facecolor='black')
        unit = list(map(lambda s: s.name, data.pc.storage))
        used = list(map(lambda s: int(float(s.used.value)), data.pc.storage))[::-1]

        self.bar = self.ax.barh(unit, used, height=0.9, color='red')
        self.ax.set_xlim(0, 100)
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['right'].set_color('white')
        self.ax.spines['top'].set_color('white')

        for storage in data.pc.storage:
            count += 1.61
            self.list_storage.append(
                self.fig.text(0.61, 0.97 - count * 0.077, storage.name + str(storage.used.value) +
                              storage.used.unit, font_storage, size=10))

        self.mother_temp = []

        count_izq = 4
        self.fig.text(0.05, 0.95 - count_izq * 0.07 - 0.03, 'Main board', fontdict=font_label)

        for temp_chip in data.pc.mother_board.temp:
            count_izq += 1.1
            key = list(temp_chip.keys())[0].replace('Temperature', 'Temp')
            self.mother_temp.append(self.fig.text(0.05, 0.93 - count_izq * 0.07, key + ": " + str(
                temp_chip[list(temp_chip.keys())[0]].value) + temp_chip[list(temp_chip.keys())[0]].unit, font_normal,
                                                  size=8))

        count_izq += 1
        self.fig.text(0.05, 0.95 - count_izq * 0.07 - 0.03, 'RAM', fontdict=font_label)
        count_izq += 0.5
        self.ram_text = self.fig.text(0.05, 0.91 - count_izq * 0.07 - 0.03, 'used: ' + str(data.pc.ram.load.value) + " " + data.pc.ram.load.unit,
                      fontdict=font_normal)
