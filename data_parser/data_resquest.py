import itertools
import json

from logger import logger

from config.environment import get_config
from utils.parser import parse_json_ohm, parse_json_ccp


class DataRequest:
    """
    Request data
    """

    def __init__(self, time_scheduler=None, data_ohm=None, data_ccp=None, update=None):
        """
        :param time_scheduler:
        :param data_ohm:
        :param data_ccp:
        :param update:
        """
        self.time_scheduler = time_scheduler + 1
        env = get_config()
        self.data_ohm = parse_json_ohm(self.get_ohm_json(
            'http://' + env['server']['host'] + ':' + env['open_hardware_monitor']['port'] + '/data.json'))

        self.data_ccp = parse_json_ccp(self \
                                       .get_ohm_json(
            'http://' + env['server']['host'] + ':' + str(env['server']['port']) + '/commanderPro/'))
        self.update = {"graphic_cpu": True, "graphic_gpu": True}

        self.fans = self.append_elemts(self.data_ccp.fans, self.data_ohm.fans)

        logger.info(str(self.data_ohm.__dict__))

    @staticmethod
    def get_ohm_json(url):
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

    @staticmethod
    def append_elemts(elemt_0, elemt_1):
        """
        Group elements
        :param elemt_0:
        :param elemt_1:
        :return:
        """
        elemts = []
        if elemt_0 is not None:
            elemts.append(elemt_0)
        if elemt_1 is not None:
            elemts.append(elemt_1)
        return list(itertools.chain(*elemts))
