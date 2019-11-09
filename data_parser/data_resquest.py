import json
import time

from config.environment import get_config


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
        self.time_scheduler = time_scheduler
        env = get_config()
        while True:
            self.data_ohm = self.get_ohm_json(
                'http://' + env['server']['host'] + ':' + env['open_hardware_monitor']['port'] + '/data.json')
            self.data_ccp = self \
                .get_ohm_json('http://' + env['server']['host'] + ':' + str(env['server']['port']) + '/commanderPro/')

            if self.time_scheduler is 0:
                self.time_scheduler = 1 + self.time_scheduler
                break
        time.sleep(env['time_update'])
        self.update = True

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
