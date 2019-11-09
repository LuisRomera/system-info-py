class Value:
    def __init__(self, value=None):
        if ',' in value[0]:
            self.value = float(value[0].replace(',', '.'))
        else:
            self.value = float(value[0])
        self.unit = value[1]
