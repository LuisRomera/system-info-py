from utils import constans


class Component:
    def __init__(self, name=None, model=None, imagen=None, properties=None):
        self.name = name
        self.model = model
        self.image = imagen
        self.properties = properties

    def parse_component(self, json=None):
        self.name = constans.imagen.get(json.get('ImageURL'), None)
        self.model = json.get('Text', None)
        self.image = json.get('ImageURL', None)
        self.properties = json.get('Children', {})
        return self
