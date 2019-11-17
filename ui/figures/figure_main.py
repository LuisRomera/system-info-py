from ui.figures.graphic import Graphic
from ui.figures.table_text import TableText


class FigureMain:

    def __init__(self, data=None):
        self.data = data
        # Graphics
        self.graphics = [Graphic('CPU'), Graphic('GPU')]
        self.table_text = [TableText(name='Fans', list_table=data.fans)]

        print("")
