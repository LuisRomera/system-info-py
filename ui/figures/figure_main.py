from ui.figures.graphic import Graphic
from ui.figures.table_text import TableText
import matplotlib.pyplot as plt



class FigureMain:

    def __init__(self, data=None, tk=None):
        try:
            self.tk = tk
            self.data = data
            # Graphics
            self.graphics = [Graphic('CPU'), Graphic('GPU')]

            self.table_text = [TableText(name='Cores', list_table=data.pc.cpu.threads)]



        except Exception as ex:
            pass
