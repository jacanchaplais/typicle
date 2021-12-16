from pathlib import Path
from typing import ClassVar
from dataclasses import dataclass, InitVar, field

import yaml


THIS_DIR = Path(__file__).parent

def parse_yaml(path: str):
    with open(path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

def struc_type(type_dict: dict) -> list:
    return list(type_dict.items())

@dataclass()
class DataTypes:
    config_file: str = str(THIS_DIR / 'types.yml')
    __data: ClassVar[dict] = parse_yaml(config_file)
    __base: ClassVar[dict] = __data['TYPE']
    bool: str = field(init=False, default=__base['bool'])
    half: str = field(init=False, default=__base['half'])
    single: str = field(init=False, default=__base['single'])
    double: str = field(init=False, default=__base['double'])
    h_int: str = field(init=False, default=__base['h_int'])
    int: str = field(init=False, default=__base['int'])
    d_int: str = field(init=False, default=__base['d_int'])
    pmu: list = field(init=False, default_factory=list)
    edge: list = field(init=False, default_factory=list)
    color: list = field(init=False, default_factory=list)

    def __post_init__(self):
        self.pmu = struc_type(self.__data['PMU_DTYPE'])
        self.edge = struc_type(self.__data['EDGE_DTYPE'])
        self.color = struc_type(self.__data['COLOR_DTYPE'])
