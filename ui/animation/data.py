from config.environment import get_config


class Data:
    def __init__(self):
        self.list_cpu_temp = []
        self.list_gpu_temp = []
        self.list_cpu_load = []
        self.list_gpu_load = []
        self.time = []

    def get_data_update(self, data_request=None, data=None):
        data.list_cpu_temp.append(data_request.data_ohm.cpu.temp_total)
        data.list_cpu_load.append(data_request.data_ohm.cpu.load_total)
        data.time.append(data_request.time_scheduler)
        if data.time[-1] > get_config()['max_time']:
            del data.time[-1]
            data.list_cpu_temp.pop(0)
            data.list_cpu_load.pop(0)
        data_graphic = []
        line_1 = data.time, data.list_cpu_temp
        line_2 = data.time, data.list_cpu_load
        data_graphic.append(line_1)
        data_graphic.append(line_2)
        return data_graphic
