from config.environment import get_config
from parse.reciver_service import ReciverService


class Data:
    def __init__(self):
        self.list_cpu_temp = []
        self.list_gpu_temp = []
        self.list_cpu_load = []
        self.list_gpu_load = []
        self.time = []

    def get_data_update_graphics(self, data_request=None, data=None, time_scheduler=None):
        data.list_cpu_temp.append(data_request.cpu.temp_package.value)
        data.list_cpu_load.append(data_request.cpu.load.value)
        data.list_gpu_temp.append(data_request.gpu.temp_core.value)
        data.list_gpu_load.append(data_request.gpu.load.value)

        data.time.append(time_scheduler)

        if data.time[-1] > get_config()['max_time']:
            del data.time[-1]
            data.list_cpu_temp.pop(0)
            data.list_cpu_load.pop(0)
            data.list_gpu_temp.pop(0)
            data.list_gpu_load.pop(0)

        data_graphic = []
        line_1 = data.time, data.list_cpu_temp
        line_2 = data.time, data.list_cpu_load
        line_3 = data.time, data.list_gpu_temp
        line_4 = data.time, data.list_gpu_load

        data_graphic.append(line_1)
        data_graphic.append(line_2)

        data_graphic.append(line_3)
        data_graphic.append(line_4)

        return data_graphic

    def get_data_update(self, data_request=None, data=None):
        unit_temp = data_request.pc.cpu.temp_package.unit
        unit_load = data_request.pc.cpu.load.unit
        update_data = {
            'graphics': self.get_data_update_graphics(data_request.pc, data, data_request.time_scheduler),
            'temp_cpu': 'Temp: ' + "{0:.2f}".format(data_request.pc.cpu.temp_package.value) + f'{unit_temp}',
            'load_cpu': 'Load: ' + "{0:.2f}".format(data_request.pc.cpu.load.value) + f'{unit_load}',
            'temp_gpu': 'Temp: ' + "{0:.2f}".format(data_request.pc.gpu.temp_core.value) + f'{unit_temp}',
            'load_gpu': 'Load: ' + "{0:.2f}".format(data_request.pc.gpu.load.value) + f'{unit_load}'
        }
        count = 0
        update_data['cores'] = {}
        update_data['cores']['load'] = {}
        update_data['cores']['frec'] = {}
        for thread in data_request.pc.cpu.threads.load:
            count += 1
            if len(str(count)) == 1:
                update_data['cores']['load']['thread' + str(count)] = 'Core  ' + str(count) + ': ' + str(int(thread.value)) + '%'
            else:
                update_data['cores']['load']['thread' + str(count)] = 'Core ' + str(count) + ': ' + str(int(thread.value)) + '%'

        count = 0

        for thread in data_request.pc.cpu.threads.frecuency_actual:
            count += 1
            if len(str(count)) == 1:
                update_data['cores']['frec']['thread' + str(count)] = 'Core  ' + str(count) + ': ' + str(int(thread.value)) + 'MHz'
            else:
                update_data['cores']['frec']['thread' + str(count)] = 'Core ' + str(count) + ': ' + str(int(thread.value)) + 'MHz'

        return update_data
