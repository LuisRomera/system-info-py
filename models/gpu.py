from models.measure import Measure
from models.thread import Thread


class GPU:
    def get_values(self, gpu_data, param, param_1):
        string = list(filter(lambda ele: ele['Text'] in param_1,
                             list(filter(lambda element: element['Text'] in param, gpu_data))[0]['Children']))[0][
            'Value']
        return Measure(float(string.split(' ')[0].replace(",", ".")), string.split(' ')[1])

    def __init__(self, data):
        gpu_data = \
            list(filter(lambda element: element['ImageURL'] in 'images_icon/nvidia.png' or element['ImageURL'] in 'images_icon/amd.png',
                        data['Children'][0]['Children']))[0]['Children']

        #self.threads = list(map(lambda t: Thread(t), list(filter(lambda elem: 'CPU' in elem['Text'],
        #                                                         list(filter(lambda element: element['Text'] in 'Clocks',
        #                                                                     cpu_data))[0]['Children']))))
        self.load = self.get_values(gpu_data, 'Clocks', 'GPU Core')

        self.temp_core = self.get_values(gpu_data, 'Temperatures', 'GPU Core')

        self.load = self.get_values(gpu_data, 'Load', 'GPU Core')

        self.menory_use = self.get_values(gpu_data, 'Data', 'GPU Memory Used')

        self.menory_free = self.get_values(gpu_data, 'Data', 'GPU Memory Free')

        self.menory_total = self.get_values(gpu_data, 'Data', 'GPU Memory Total')