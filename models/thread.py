from models.measure import Measure


class Thread:
    def __init__(self, data):
        f_string = list(map(lambda t: t, list(filter(lambda elem: 'CPU' in elem['Text'],
                                                            list(filter(lambda element: element['Text'] in 'Clocks',
                                                                        data))[0]['Children']))))
        load_string = list(map(lambda t: t, list(filter(lambda elem: 'CPU Total' not in elem['Text'],
                                                     list(filter(lambda element: element['Text'] in 'Load',
                                                                 data))[0]['Children']))))

        self.frecuency_actual = list(map(lambda x: Measure(float(x['Value'].split(' ')[0].replace(',', '.')), x['Value'].split(' ')[1]), f_string))

        self.load = list(map(lambda x: Measure(float(x['Value'].split(' ')[0].replace(',', '.')), x['Value'].split(' ')[1]), load_string))
