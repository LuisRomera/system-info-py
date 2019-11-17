from config.environment import get_config


class Data:
    def __init__(self):
        self.list_cpu_temp = []
        self.list_gpu_temp = []
        self.list_cpu_load = []
        self.list_gpu_load = []
        self.time = []

    def get_data_update_graphics(self, data_request=None, data=None):
        data.list_cpu_temp.append(data_request.data_ohm.cpu.temp_total)
        data.list_cpu_load.append(data_request.data_ohm.cpu.load_total)
        data.list_gpu_temp.append(data_request.data_ohm.gpu.temp.value)
        data.list_gpu_load.append(data_request.data_ohm.gpu.load.value)

        data.time.append(data_request.time_scheduler)

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
        unit_temp = data_request.data_ohm.gpu.temp.unit
        unit_load = data_request.data_ohm.gpu.load.unit
        update_data = {
            'graphics': self.get_data_update_graphics(data_request, data),
            'temp_cpu': 'Temp: ' + "{0:.2f}".format(data_request.data_ohm.cpu.temp_total) + f'{unit_temp}',
            'load_cpu': 'Load: ' + "{0:.2f}".format(data_request.data_ohm.cpu.load_total) + f'{unit_load}',
            'temp_gpu': 'Temp: ' + "{0:.2f}".format(data_request.data_ohm.gpu.temp.value) + f'{unit_temp}',
            'load_gpu': 'Load: ' + "{0:.2f}".format(data_request.data_ohm.gpu.load.value) + f'{unit_load}'
        }


        return update_data
