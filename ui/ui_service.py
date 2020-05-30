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
            try:
                self.data_request = DataRequest(time_scheduler=self.data_request.time_scheduler)
                time.sleep(env['time_update'])
            except Exception as ex:
                pass

    """
    Main class ui. Write screen
    """

    def __init__(self, master=None, **kwargs):
        # Data receiver request
        try:
            self.data_request = DataRequest(time_scheduler=-2)
        except Exception as ex:
            self.data_request = None
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
        self.figures = FigureMain(data=self.data_request, tk=self.tk)
        self.list_canvas = list(map(lambda canvas: FigureCanvasTkAgg(canvas.fig, master=self), self.figures.graphics))
        self.list_canvas_text = list(
            map(lambda canvas: FigureCanvasTkAgg(canvas.fig, master=self), self.figures.table_text))

        self.list_canvas[0].get_tk_widget().grid(column=0, row=0)
        self.list_canvas_text[0].get_tk_widget().grid(column=1, row=0)
        self.list_canvas[1].get_tk_widget().grid(column=0, row=1)
        self.list_canvas_text[1].get_tk_widget().grid(column=1, row=1)

        self.start()

    def start(self):
        """
        Strat animations
        :return:
        """
        self.ani_graphic_cpu = animation.FuncAnimation(self.figures.graphics[0].fig, self.update_fig)

        self.ani_text_A = animation.FuncAnimation(self.figures.table_text[0].fig, self.update_fig)

        self.ani_graphic_gpu = animation.FuncAnimation(self.figures.graphics[1].fig, self.update_fig)

        self.ani_text_B = animation.FuncAnimation(self.figures.table_text[1].fig, self.update_fig)

        self.update_name = 'load'
    def update_fig(self, i):
        """
        Update animated figures
        :param i:
        :return:
        """
        try:
            # logger.info("Update")
            new_data = self.data_updated.get_data_update(data_request=self.data_request, data=self.data_updated)
            change = False
            if self.data_request.update['graphic_cpu'] is True:
                self.data_request.update['graphic_cpu'] = False
                self.figures.graphics[0].lines[0].set_data(new_data['graphics'][0])
                self.figures.graphics[0].lines[1].set_data(new_data['graphics'][1])
                self.figures.graphics[0].text_temp.set_text(new_data['temp_cpu'])
                self.figures.graphics[0].text_load.set_text(new_data['load_cpu'])
                count = 0
                if len(new_data['graphics'][0][1]) % 30 == 0:
                    if self.update_name in 'load':
                        self.update_name = 'frec'
                    else:
                        self.update_name = 'load'

                for cpu in self.figures.table_text[0].text_cpu:
                    count += 1
                    cpu.set_text(new_data['cores'][self.update_name]['thread' + str(count)])

            if self.data_request.update['graphic_gpu'] is True:
                self.data_request.update['graphic_gpu'] = False
                self.figures.graphics[1].lines[0].set_data(new_data['graphics'][2])
                self.figures.graphics[1].lines[1].set_data(new_data['graphics'][3])
                self.figures.graphics[1].text_temp.set_text(new_data['temp_gpu'])
                self.figures.graphics[1].text_load.set_text(new_data['load_gpu'])
                count = 0

                for fan in self.figures.table_text[1].fans:
                    fan.set_text(new_data['fans'][count])
                    count += 1
                self.figures.table_text[1].pump.set_text(new_data['pump'])
                self.figures.table_text[1].text_gpu_menory_use.set_text(new_data['gpu']['used_memory'])
                self.figures.table_text[1].text_gpu_menory_frec.set_text(new_data['gpu']['frec_memory'])
                self.figures.table_text[1].text_gpu_shader.set_text(new_data['gpu']['shader'])

                count = 0
                for text_storeage in self.figures.table_text[1].list_storage:
                    self.figures.table_text[1].list_storage[count].set_text(new_data['storage']['string'][count])
                    self.figures.table_text[1].bar[count].set_width(new_data['storage']['data'][count])
                    count +=1



        except Exception as ex:
            time.sleep(5)
            pass


def get_config_ui():
    """
    Config UI screen

    :return:
    """
    root = tk.Tk()
    root.configure(background='black')
    # root.attributes("-fullscreen", True)
    root.geometry("800x480")
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
