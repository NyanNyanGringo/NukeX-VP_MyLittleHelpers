"""
Библиотека для работы с конфиг-файлами формата .json

Если не указывать значение conf_file_path в функциях,
то работа будет происходить с дефолтным конфиг-файлом.
"""

import nuke
import json
import os
import tempfile


# def get_temp_config_path() -> str:
#     configs_path = os.environ['HOME'].replace("\\", "/") + "/.nuke/configs"
#     if not os.path.exists(configs_path):
#         os.mkdir(configs_path)
#     return configs_path + "/read_write_coloriser.json"

def get_temp_config_path() -> str:
    configs_path = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    return configs_path + "/read_write_coloriser.json"

def write_configs(keys, confs, conf_file_path=get_temp_config_path()) -> True:
    """
    Записать значения в конфиг-файл в формате ключ-значение.
    :
    :param keys: list | dict of str
    :param confs: list | dict of str
    :param conf_file_path: str
    """
    config_data = dict()

    if len(keys) != len(confs):
        raise Exception("Different length of keys and values!")

    if os.path.isfile(conf_file_path):
        f = open(conf_file_path, mode='r')
        config_data = json.load(f)
        f.close()

    i = 0
    for key in keys:
        config_data[key] = confs[i]
        i += 1

    f = open(conf_file_path, mode='w')
    json.dump(config_data, f, indent=2, sort_keys=True)
    f.close()

    return True


def write_config(key, conf, conf_file_path=get_temp_config_path()) -> True:
    """
    Записать значение в конфиг-файл в формате ключ-значение.
    :
    :param key: str
    :param conf: any
    :param conf_file_path: str
    """
    config_data = dict()

    if os.path.isfile(conf_file_path):
        f = open(conf_file_path, mode='r')
        config_data = json.load(f)
        f.close()

    config_data[key] = conf

    f = open(conf_file_path, mode='w')
    json.dump(config_data, f, indent=2, sort_keys=True)
    f.close()

    return True


def read_config(conf_file_path=get_temp_config_path()) -> dict:
    """
    Прочитать весь конфиг файл
    :
    :param conf_file_path: str
    """

    if not os.path.isfile(conf_file_path):
        raise Exception(f"Config {conf_file_path} doesn't exists!")

    f = open(conf_file_path, mode='r')
    config_data_input = json.load(f)
    f.close()

    return config_data_input


def read_config_key(key, conf_file_path=get_temp_config_path()) -> any:
    """
    Прочитать значение по ключу из конфига
    :
    :param key: any
    :param conf_file_path: str
    """

    if not check_key(key, conf_file_path):
        raise Exception(f"Config {conf_file_path} or key {key} doesn't exists!")

    f = open(conf_file_path, mode='r')
    config_data_input = json.load(f)
    f.close()

    return config_data_input[key]


def check_key(key, conf_file_path=get_temp_config_path()) -> bool:
    """
    Проверить - существует ли конфинг-файл и есть ли у него ключ
    :
    :param key: any
    :param conf_file_path: str
    """

    if not os.path.isfile(conf_file_path):
        return False

    f = open(conf_file_path, mode='r')
    config_data_input = json.load(f)
    f.close()

    if key in config_data_input.keys():
        return True
    else:
        return False


def delete_key(key, conf_file_path=get_temp_config_path()) -> bool:
    """
    Удалить ключ и его значение из конфиг-файла
    :
    :param key: any
    :param conf_file_path: str
    """

    if check_key(key, conf_file_path):
        f = open(conf_file_path, mode='r')
        config_data = json.load(f)
        f.close()

        del config_data[key]

        f = open(conf_file_path, mode='w')
        json.dump(config_data, f, indent=2, sort_keys=True)
        f.close()
        return True
    return False
