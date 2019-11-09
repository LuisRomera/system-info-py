class Cpu:
    def __init__(self, name=None, cores=None, load_total=None, temp_total=None):
        self.name = name
        self.cores = cores
        self.load_total = load_total
        self.temp_total = temp_total

    def parse_cpu(self, json, image=None):
        self.name = json.get('Text', None)
        self.speed_value = json.get('Value').split(" ")[0]
        self.speed_max = json.get('Max').split(" ")[0]
        self.speed_min = json.get('Min').split(" ")[0]
        self.speed_unit = json.get('Value').split(" ")[1]
        self.image = image
        return self
