import json
import urllib

from logger import logger

from model.component import Component
from model.cores import Core
from model.cpu import Cpu
from model.data import Data
from model.fan import Fan
from model.gpu import Gpu
from model.pc import Pc
from model.values import Value
from utils.constans import json_names, MOTHER_BOARD, CPU, GPU
from utils.mother_board_parser import parser_mother_board


def read_json():
    """
    Read json
    :return:
    """
    with urllib.request.urlopen('http://192.168.0.14:8085/data.json') as url:
        return json.loads(url.read().decode())


#    with open("example.json") as json_config:
#        return json.load(json_config)


def get_component_prop(json):
    """
    Get mothe board properties
    :param json:
    :return:
    """
    return list(map(lambda c: Component().parse_component(c), json))


def get_children(json):
    return json.get('Children', {})


def get_prop_cpu(prop):
    return list(map(lambda y: {y.get("Text"): y.get("Value").split(" ")},
                    filter(lambda x: "CPU" in x.get("Text") and "Total" not in x.get("Text"), prop)))


def parse_json_ohm(json):
    """
    Parse request json
    :return:
    """
    try:
        # Parser all components
        pc_componens = list(
            filter(lambda c: c.name is not None, get_component_prop(get_children(get_children(json)[0]))))

        # Mother board
        fans = parser_mother_board(pc_componens)

        # Cpu
        cpu = list(filter(lambda c: str(c.name) in CPU, pc_componens))[0]
        name = cpu.name
        model = cpu.model
        image = cpu.image

        # Cores
        clock = get_prop_cpu(get_children(list(filter(lambda x: x.get('Text') in 'Clocks', cpu.properties))[0]))
        temp = get_prop_cpu(get_children(list(filter(lambda x: x.get('Text') in 'Temperatures', cpu.properties))[0]))
        load = get_prop_cpu(get_children(list(filter(lambda x: x.get('Text') in 'Load', cpu.properties))[0]))
        # power = get_prop_cpu(get_children(list(filter(lambda x: x.get('Text') in 'Powers', cpu.properties))[0]))
        cores = list()
        for key in list(map(lambda x: list(x.keys())[0], clock)):
            cores.append(
                Core(
                    key,
                    Value(list(filter(lambda x: list(x.keys())[0] in key, temp))[0].get(key)),
                    Value(list(filter(lambda x: list(x.keys())[0] in key, load))[0].get(key)),
                    Value(list(filter(lambda x: list(x.keys())[0] in key, clock))[0].get(key))))

        t = 0.0
        l = 0.0
        c = 0.0
        for core in cores:
            t = t + core.temp.value
            l = l + core.load.value
            c = c + core.frec.value
        cpu = Cpu(name=name, cores=cores, load_total=l / len(cores), temp_total=list(filter(lambda c: 'CPU Package' in str(c), temp))[0]['CPU Package'][0])

        gpu_json = list(filter(lambda c: str(c.name) in GPU, pc_componens))[0]
        gpu_temp = get_children(list(filter(lambda c: str(c['Text']) in "Temperatures", gpu_json.properties))[0])[0][
            'Value']
        gpu_load = get_children(list(filter(lambda c: str(c['Text']) in "Load", gpu_json.properties))[0])[0]['Value']
        gpu = Gpu(name=gpu_json.name, temp=Data(gpu_temp), load=Data(gpu_load))
        return Pc(cpu=cpu, fans=fans, gpu=gpu)
    except Exception as ex:
        logger.error(str(ex))
        return None


def parse_json_ccp(json):
    keys_fans = list(filter(lambda key: 'FAN' in key.upper(), json.keys()))
    fans = list(map(
        lambda key: Fan(name=key, speed_value=json[key].lower().replace('rpm', ''), speed_max=None, speed_min=None,
                        speed_unit='rpm', image=None), keys_fans))

    return Pc(fans=fans)
