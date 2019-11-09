try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


class App(tk.Frame):

    def worker_request(self):
        return


    """
    Main class ui. Write screen
    """
    def __init__(self, master=None, **kwargs):
        # Data receiver request
        self.data_request = None

        self.worker_request()




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
