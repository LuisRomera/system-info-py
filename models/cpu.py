from models.measure import Measure
from models.thread import Thread


class CPU:
    def get_values(self, cpu_data, param, param_1):
        string = list(filter(lambda ele: ele['Text'] in param_1,
                             list(filter(lambda element: element['Text'] in param, cpu_data))[0]['Children']))[0][
            'Value']
        return Measure(float(string.split(' ')[0].replace(",", ".")), string.split(' ')[1])

    def __init__(self, data):
        self.frecuency = data
        cpu_data = \
            list(filter(lambda element: element['ImageURL'] in 'images_icon/cpu.png',
                        data['Children'][0]['Children']))[0]['Children']

        self.threads = Thread(cpu_data)

        self.load = self.get_values(cpu_data, 'Load', 'CPU Total')

        self.temp_package = self.get_values(cpu_data, 'Temperatures', 'CPU Package')