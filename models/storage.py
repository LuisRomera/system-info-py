from models.measure import Measure


class Storage:
    def __init__(self, hdd):
        self.name = hdd['Text']
        self.used = Measure(hdd['Children'][0]['Children'][0]['Value'].split(' ')[0].replace(',', '.'),hdd['Children'][0]['Children'][0]['Value'].split(' ')[1])
