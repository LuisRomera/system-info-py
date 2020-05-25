import json

import logger

from config.environment import get_config
import urllib.request as request

from model.fan import Fan
from models.cpu import CPU
from models.fan import Fans
from models.gpu import GPU
from models.pump import Pump, Pumps
from models.storage import Storage
from models.thread import Thread

env = get_config()


class ReciverService:

    def __init__(self):
        url = 'http://' + env['server']['host'] + ':' + env['open_hardware_monitor']['port'] + '/data.json'
        self.data = self.get_ohm_json(url)
        self.cpu = CPU(self.data)
        self.gpu = GPU(self.data)
        string_mother_board = list(filter(lambda element: element['ImageURL'] in 'images_icon/nvidia.png' or element[
            'ImageURL'] in 'images_icon/mainboard.png', self.data['Children'][0]['Children']))[0]['Children'][0]
        self.fans = Fans(string_mother_board)
        self.pump = Pumps(string_mother_board)
        self.storage = list(map(lambda hdd: Storage(hdd), list(
            filter(lambda elem: elem['ImageURL'] in 'images_icon/hdd.png', self.data['Children'][0]['Children']))))

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
