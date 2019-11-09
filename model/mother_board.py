class MotherBoard:
    def __init__(self, json=None):
        self.name = json.get('Text', None)
        self.image = json.get('ImageURL', None)
