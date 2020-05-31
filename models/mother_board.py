from models.measure import Measure


class MotherBoard:
    def __init__(self, data):
        temperature = list(filter(lambda t: t['Text'] in 'Temperatures', data['Children'][0]['Children']))[0]['Children']
        self.temp = list(map(lambda t: {t['Text']: Measure(t['Value'].split(' ')[0].replace(',', '.'), t['Value'].split(' ')[1])}, temperature))
