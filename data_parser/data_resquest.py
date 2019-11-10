import json

from logger import logger

from config.environment import get_config
from utils.parser import parse_json


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
        self.data_ohm = parse_json(self.get_ohm_json(
            'http://' + env['server']['host'] + ':' + env['open_hardware_monitor']['port'] + '/data.json'))

        logger.info(str(self.data_ohm.__dict__))
        self.data_ccp = self \
            .get_ohm_json('http://' + env['server']['host'] + ':' + str(env['server']['port']) + '/commanderPro/')
        self.update = {"graphic_cpu": True, "graphic_gpu": True}

        logger.info(str(self.data_ccp))

    @staticmethod
    def get_ohm_json(url):
        """
        Open request
        :return:
        """
        data = None
        try:
            import urllib.request as request
            with request.urlopen(url) as url_str:
                data = json.loads(url_str.read().decode())
        except Exception as ex:
            pass
        return data
