import glob
import os
import time

from logger import logger


class CommanderProService:
    def __init__(self, path):
        self.path = path

    def get_file_open(self):
        files = [f for f in glob.glob(self.path + "**/*.csv", recursive=True)]
        for file in files:
            try:
                os.remove(file)
            except Exception as ex:
                pass
            try:
                file_name = [f for f in glob.glob(self.path + "**/*.csv", recursive=True)][0]
                file = open(file_name, mode='r', encoding='utf-8-sig')
                lines = file.readlines()
                file.close()
                return {"last_line": lines[-1], "header": lines[0].replace('"', '').replace('\n', '').split(',')}
            except Exception as ex:
                return {"file_name": None, "header": None}

    def parser_info(self, param, header):
        param_list = param.replace('\n', '').replace('"', '').split(',')
        corsair_dict = {}
        for index in range(len(header)):
            corsair_dict[header[index]] = param_list[index]
        return corsair_dict

    def get_info_corsair_comamander(self):
        file_open = self.get_file_open()
        if file_open["last_line"] is not None:
            try:
                return self.parser_info(file_open["last_line"], file_open['header'])
            except Exception as ex:
                logger.error(ex)
