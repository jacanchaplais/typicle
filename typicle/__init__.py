from pathlib import Path

import yaml


THIS_DIR = Path(__file__).parent

def parse_yaml(path: str):
    with open(path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

def struc_type(type_dict: dict) -> list:
    return list(type_dict.items())

class Types:
    def __init__(self, config_file: str=str(THIS_DIR / 'types.yml')):
        data = parse_yaml(config_file)
        for key, val in data['TYPE'].items():
            setattr(self, key, val)
        self.__pmu = data['PMU_DTYPE']
        self.__edge = data['EDGE_DTYPE']
        self.__color = data['COLOR_DTYPE']

    @property
    def pmu(self):
        return struc_type(self.__pmu)

    @property
    def edge(self):
        return struc_type(self.__edge)

    @property
    def color(self):
        return struc_type(self.__color)
