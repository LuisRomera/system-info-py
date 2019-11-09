import json
import time
import urllib


class DataRequest:
    """
    Request data
    """
    def __init__(self):
        while True:
            with urllib.request.urlopen('http://192.168.0.17:8085/data.json') as url:
                data_ = json.loads(url.read().decode())
            if self.t is 0:
                self.t = 1 + self.t
                break
            self.t = 1 + self.t
            time.sleep(0.5)
