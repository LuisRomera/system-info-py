from models.measure import Measure
from models.thread import Thread


class Fans:
    def get_values(self, gpu_data, param, param_1):
        fan = {}
        list_string = list(map(lambda ele: {'name':ele['Text'], 'value': ele['Value']},
                          list(filter(lambda element: element['Text'] in param, gpu_data))[0]['Children']))
        return list(map(lambda f: Fan(f['name'], Measure(f['value'].split(' ')[0].replace(",", "."), f['value'].split(' ')[1])), list_string))

    def __init__(self, data):
        self.data = data
        self.all_fans = self.get_values(data['Children'], 'Fans', 'Fan')


class Fan:

    def __init__(self, name=None, measure=None):
        self.name = name
        self.speed = measure
