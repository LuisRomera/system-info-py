from logger import logger
from matplotlib import pyplot as plt

from config.desing import font_label, font_temp, font_load
from config.environment import get_config
from ui.figures.graphic import Graphic


class FigureMain:

    def __init__(self):
        logger.info("")
        # Graphics
        self.graphics = [Graphic('CPU'), Graphic('GPU')]



