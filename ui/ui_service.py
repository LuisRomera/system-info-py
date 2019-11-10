import threading
import time

from logger import logger
from matplotlib import animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from config.environment import get_config
from data_parser.data_resquest import DataRequest
from ui.animation.data import Data
from ui.figures.figure_main import FigureMain

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

env = get_config()

class App(tk.Frame):

    def worker_request(self):
        while True:
            logger.info(str(self.data_request.__dict__))
            self.data_request = DataRequest(time_scheduler=self.data_request.time_scheduler)
            time.sleep(env['time_update'])

    """
    Main class ui. Write screen
    """

    def __init__(self, master=None, **kwargs):
        # Data receiver request
        self.data_request = DataRequest(time_scheduler=-2)
        t = threading.Thread(target=self.worker_request)
        t.start()
        self.data_updated = Data()

        # Interface
        tk.Frame.__init__(self, master, **kwargs)
        self.running = True
        self.ani = True
        self.interval = tk.Entry(width=0)
        self.interval.insert(0, '10')

        # Figures
        self.figures = FigureMain()
        self.list_canvas = list(map(lambda canvas: FigureCanvasTkAgg(canvas.fig, master=self), self.figures.graphics))
        self.list_canvas = list(map(lambda c: c.get_tk_widget().pack(), self.list_canvas))
        self.start()

    def start(self):
        """
        Strat animations
        :return:
        """
        self.ani_graphic_cpu = animation.FuncAnimation(self.figures.graphics[0].fig, self.update_fig)
        self.ani_graphic_gpu = animation.FuncAnimation(self.figures.graphics[1].fig, self.update_fig)

    def update_fig(self, i):
        """
        Update animated figures
        :param i:
        :return:
        """
        new_data = self.data_updated.get_data_update(data_request=self.data_request, data=self.data_updated)
        if self.data_request.update['graphic_cpu'] is True:
            self.data_request.update['graphic_cpu'] = False
            self.figures.graphics[0].lines[0].set_data(new_data[0])
            self.figures.graphics[0].lines[1].set_data(new_data[1])
        if self.data_request.update['graphic_gpu'] is True:
            self.data_request.update['graphic_gpu'] = False
            self.figures.graphics[1].lines[0].set_data(new_data[0])
            self.figures.graphics[1].lines[1].set_data(new_data[1])


def get_config_ui():
    """
    Config UI screen

    :return:
    """
    root = tk.Tk()
    root.configure(background='black')
    # root.attributes("-fullscreen", True)
    return root


def init_ui():
    """
    Start UI
    :return:
    """
    root = get_config_ui()
    app = App(root)
    app.pack()
    root.mainloop()