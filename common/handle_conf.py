import os
from configparser import ConfigParser
from common.handle_path import CONF_DIR


class conf(ConfigParser):
    def __init__(self, filename, encoding='utf-8'):
        super().__init__()
        self.read(filename, encoding)


cof = conf(os.path.join(CONF_DIR, 'config.ini'))