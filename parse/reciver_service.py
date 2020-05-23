import json

import logger

from config.environment import get_config
import urllib.request as request

from models.cpu import CPU
from models.gpu import GPU
from models.thread import Thread

env = get_config()


class ReciverService:

    def __init__(self):
        url = 'http://' + env['server']['host'] + ':' + env['open_hardware_monitor']['port'] + '/data.json'
        self.data = self.get_ohm_json(url)
        self.cpu = CPU(self.data)
        self.gpu = GPU(self.data)

    def get_ohm_json(self, url):
        """
        Open request
        :return:
        """
        data_str = None
        try:
            import urllib.request as request
            with request.urlopen(url) as url_str:
                data_str = url_str.read().decode()
            if 'COMMANDER PRO ' in data_str:
                data_str = data_str.replace('COMMANDER PRO ', '')
        except Exception as ex:
            return None
        return json.loads(data_str)
