from models.measure import Measure


class RAM:
    def __init__(self, data):
        self.load = Measure(data.split(' ')[0].replace(",", "."), data.split(' ')[1])
