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
        # unit_temp = data_request.data_ohm.gpu.temp.unit

        time_scheduler = data_request.time_scheduler
        data_request = ReciverService()
        unit_temp = data_request.cpu.temp_package.unit
        # unit_load = data_request.data_ohm.gpu.load.unit
        unit_load = data_request.cpu.load.unit
        update_data = {
            'graphics': self.get_data_update_graphics(data_request, data, time_scheduler),
            'temp_cpu': 'Temp: ' + "{0:.2f}".format(data_request.cpu.temp_package.value) + f'{unit_temp}',
            'load_cpu': 'Load: ' + "{0:.2f}".format(data_request.cpu.load.value) + f'{unit_load}',
            'temp_gpu': 'Temp: ' + "{0:.2f}".format(data_request.gpu.temp_core.value) + f'{unit_temp}',
            'load_gpu': 'Load: ' + "{0:.2f}".format(data_request.gpu.load.value) + f'{unit_load}'
        }
        count = 0
        for thread in data_request.cpu.threads.load:
            count += 1
            update_data['thread' + str(count)] = 'core ' + str(count) + ': ' + str(int(thread.value)) + '%'

        print(update_data)



        return update_data
