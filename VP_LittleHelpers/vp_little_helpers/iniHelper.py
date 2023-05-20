import configparser
import os


def get_ini_config_path():
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "USERCONFIG.ini").replace("\\", "/")


def get_ini_config():
    ini_config = configparser.ConfigParser()
    ini_config.read(get_ini_config_path())
    return ini_config
