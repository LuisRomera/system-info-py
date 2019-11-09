class Fan:
    def __init__(self, name=None, speed_value=None, speed_max=None, speed_min=None, speed_unit=None, image=None):
        self.name = name
        self.speed_value = speed_value
        self.speed_max = speed_max
        self.speed_min = speed_min
        self.speed_unit = speed_unit
        self.image = image

    def parse_fan(self, json, image=None):
        self.name = json.get('Text', None)
        self.speed_value = float(json.get('Value').split(" ")[0])
        self.speed_max = float(json.get('Max').split(" ")[0])
        self.speed_min = float(json.get('Min').split(" ")[0])
        self.speed_unit = json.get('Value').split(" ")[1]
        self.image = image
        return self
