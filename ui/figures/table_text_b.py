import matplotlib.pyplot as plt

from config.desing import font_label, font_normal


class TableTextB:
    def __init__(self, name=None, data=None):

        self.fig = plt.Figure(facecolor='black', figsize=(3, 2.1), dpi=110)
        self.fig.text(0.2, 0.93, 'GPU', fontdict=font_label)
        self.text_gpu_menory_use = self.fig.text(0.05, 0.9 - 0.07, 'used memory: ' + str(int(100*data.pc.gpu.memory_use.value/data.pc.gpu.memory_free.value)) + '%', font_normal)
        self.text_gpu_menory_frec = self.fig.text(0.05, 0.9 - 0.07*2, 'frec memory: ' + str(int(data.pc.gpu.frec_memory.value)) + data.pc.gpu.frec_memory.unit, font_normal)
        self.text_gpu_shader = self.fig.text(0.05, 0.9 - 0.07*3, 'shader: ' + str(int(data.pc.gpu.shader.value)) + data.pc.gpu.shader.unit, font_normal)

        self.fig.text(0.6, 0.93, 'FANS', fontdict=font_label)
        count = 0
        self.fans = []
        for fan in data.pc.fans.all_fans:
            count += 1
            self.fans.append(self.fig.text(0.6, 0.9 - count * 0.07, fan.name + ": " + str(fan.speed.value) + fan.speed.unit, font_normal))

        count += 1

        self.pump = self.fig.text(0.6, 0.9 - count * 0.07,
                                       "Pump: " + str(data.pc.pump.all_fans[0].speed.value) +
                                       data.pc.pump.all_fans[0].speed.unit, font_normal)

        count += 1
        self.fig.text(0.6, 0.9 - count * 0.07 - 0.03, 'Storage', fontdict=font_label)

