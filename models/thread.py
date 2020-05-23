from models.measure import Measure


class Thread:
    def __init__(self, data):
        self.frecuency_actual = Measure(float(data['Value'].split(' ')[0].replace(',', '.')), data['Value'].split(' ')[1])
