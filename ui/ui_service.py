import threading

from logger import logger
from matplotlib import animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from config.environment import get_config
from data_parser.data_resquest import DataRequest
from ui.figures.figure_main import FigureMain

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

# ---------------------------------------------------------------
list_blue = []
list_red = []
list_green = []
list_x = []
env = get_config()


def get_data(t, datos):
    """
    replace this function with whatever you want to provide the data
    for now, we just return soem random data
    :param i:
    :return:
    """
    list_red.append(1)
    list_blue.append(1)
    list_green.append(1)
    list_green.append(0)
    list_x.append(t)
    # if len(list_x) > env['max_time'] + 2:
    if list_x[-1] > env['max_time'] + 2:
        del list_x[-1]
        list_blue.pop(0)
        list_red.pop(0)
        list_green.pop(0)

    data = []
    line_1 = list_x, list_red
    line_2 = list_x, list_blue
    line_3 = list_x, list_green
    data.append(line_1)
    data.append(line_2)
    data.append(line_3)
    return data


# ----------------------------------------

class App(tk.Frame):

    def worker_request(self):
        data = DataRequest(time_scheduler=self.t)
        logger.info(str(data.__dict__))
        return DataRequest(time_scheduler=self.t)

    """
    Main class ui. Write screen
    """

    def __init__(self, master=None, **kwargs):
        self.t = 0
        # Data receiver request
        self.data_request = self.worker_request()
        threading.Thread(target=self.worker_request).start()

        # Interface
        tk.Frame.__init__(self, master, **kwargs)
        self.running = True
        self.ani = True
        self.interval = tk.Entry(width=0)
        self.interval.insert(0, '10')

        # Figures
        self.figures = FigureMain()
        self.canvas = FigureCanvasTkAgg(self.figures.fig, master=self)
        self.canvas.get_tk_widget().pack()

        self.start()

    def start(self):
        self.ani = animation.FuncAnimation(
            self.figures.fig,
            self.update_graph,
            interval=int(self.interval.get()),
            repeat=False, blit=True)

        self.ani._start()

    def update_graph(self, i):
        if self.data_request.update is True:
            self.data_request.update = False
            self.figures.lines[0].set_data(get_data(self.t, self.data_request.data_ccp)[0])
            self.figures.lines[1].set_data(get_data(self.t, self.data_request.data_ccp)[0])
            self.figures.lines[2].set_data(get_data(self.t, self.data_request.data_ccp)[0])
        return self.figures.lines


def get_config_ui():
    """
    Config UI screen

    :return:
    """
    root = tk.Tk()
    root.configure(background='black')
    root.attributes("-fullscreen", True)
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
