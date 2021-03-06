import random

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
            'temp_cpu': 'Temp: ' + str(int(data_request.pc.cpu.temp_package.value)) + unit_temp,
            'load_cpu': 'Load: ' + str(int(data_request.pc.cpu.load.value)) + unit_load,
            'temp_gpu': 'Temp: ' + str(int(data_request.pc.gpu.temp_core.value)) + unit_temp,
            'load_gpu': 'Load: ' + str(int(data_request.pc.gpu.load.value)) + unit_load
        }
        count = 0
        update_data['cores'] = {}
        update_data['cores']['load'] = {}
        update_data['cores']['frec'] = {}
        for thread in data_request.pc.cpu.threads.load:
            count += 1
            if len(str(count)) == 1:
                update_data['cores']['load']['thread' + str(count)] = 'Core ' + '  ' + str(count) + ': ' + str(int(thread.value)) + '%'
            else:
                update_data['cores']['load']['thread' + str(count)] = 'Core ' + str(count) + ': ' + str(int(thread.value)) + '%'

        count = 0
        for thread in data_request.pc.cpu.threads.frecuency_actual:
            count += 1
            if len(str(count)) == 1:
                update_data['cores']['frec']['thread' + str(count)] = 'Core '+ '  ' + str(count) + ': ' + str(int(thread.value)) + 'MHz'
            else:
                update_data['cores']['frec']['thread' + str(count)] = 'Core ' + str(count) + ': ' + str(int(thread.value)) + 'MHz'
        update_data['gpu'] = {}
        update_data['gpu']['used_memory'] = 'used memory: ' + str(int(100*data_request.pc.gpu.memory_use.value/data_request.pc.gpu.memory_free.value)) + '%'
        update_data['gpu']['frec_memory'] = 'frec memory: ' + str(int(data_request.pc.gpu.frec_memory.value)) + data_request.pc.gpu.frec_memory.unit
        update_data['gpu']['shader'] = 'shader: ' + str(int(data_request.pc.gpu.shader.value)) + data_request.pc.gpu.shader.unit

        update_data['fans'] = []

        for fan in data_request.pc.fans.all_fans:
            if len(str(fan.speed.value)) == 4:
                update_data['fans'].append(fan.name + ": " + str(fan.speed.value) + fan.speed.unit)
            else:
                update_data['fans'].append(fan.name + ":   " + str(fan.speed.value) + fan.speed.unit)
        update_data['pump'] = "Pump: " + str(data_request.pc.pump.all_fans[0].speed.value) + \
                              data_request.pc.pump.all_fans[0].speed.unit

        update_data['storage'] = {}

        update_data['storage']['string'] = list(map(lambda storage: storage.name + " " + str(storage.used.value) + storage.used.unit, data_request.pc.storage))
        update_data['storage']['data'] = list(map(lambda s: int(float(s.used.value)), data_request.pc.storage))[::-1]


        update_data['chip'] = []
        for temp_chip in data_request.pc.mother_board.temp:
            key = list(temp_chip.keys())[0].replace('Temperature', 'Temp')
            update_data['chip'].append(key + ": " + str(temp_chip[list(temp_chip.keys())[0]].value) + temp_chip[list(temp_chip.keys())[0]].unit)

        update_data['ram'] = 'used: ' + str(data_request.pc.ram.load.value) + " " + data_request.pc.ram.load.unit

        return update_data
