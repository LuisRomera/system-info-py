from ui.figures.graphic import Graphic
from ui.figures.table_text import TableText
import matplotlib.pyplot as plt

from ui.figures.table_text_b import TableTextB


class FigureMain:

    def __init__(self, data=None, tk=None):
        try:
            self.tk = tk
            self.data = data
            # Graphics
            self.graphics = [Graphic('CPU'), Graphic('GPU')]

            self.table_text = [TableText(name='CORES', list_table=data.pc.cpu.threads),
                               TableTextB(name='Others', data=data)]



        except Exception as ex:
            pass
