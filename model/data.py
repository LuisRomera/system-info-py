from model.values import Value


class Data:
    def __init__(self, data):
        self.value = None
        self.unit = None
        if " " in data:
            self.value = float(data.split(" ")[0].replace(",", "."))
            self.unit = data.split(" ")[1]
