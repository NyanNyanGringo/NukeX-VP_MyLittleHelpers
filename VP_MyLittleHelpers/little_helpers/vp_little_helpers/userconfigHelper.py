"""
How to add sections and elements:
1. get_userconfig_structure() -> добавить значения в структуру
2. check_userconfig_before_start_nuke() -> написать проверки перед запуском
"""
import configparser
import os

import nuke

from little_helpers.vp_little_helpers import osHelpers, configHelper


# HELPERS


def raise_error(message: str, error_line: list = None, exit_nuke: bool = True) -> None:
    """
    Developer helper to write message about problem in USERCONFIG.ini
    :param: error_line: [int, str], [line_number, line_text]
    """
    base_text = f"Error in: {get_userconfig_path()}"
    if error_line:
        base_text += f"\nLine {error_line[0]}: {error_line[1]}"
    base_text += "\n\n"
    base_text += f"{message}\n\n"
    base_text += "Solution №1: check USERCONFIG.ini and edit manually;\n"
    base_text += "Solution №2: delete USERCONFIG.ini and restart Nuke."

    nuke.message(base_text)

    if exit_nuke:
        osHelpers.open_in_finder(get_userconfig_path())
        raise SystemExit


def find_element_line(element, value):
    i = 1
    with open(get_userconfig_path(), "r") as f:
        for line in f:
            if (element in line) and (value in line):
                return i
            i += 1
    return None


def check_color_string_validity(input_string):
    allowed_characters = set("0123456789|. ")
    for char in input_string:
        if char not in allowed_characters:
            return False

    if not len(input_string.split("|")) == 3:
        return False

    return True


def check_path_validity(path):
    if path.startswith("./"):
        return True
    else:
        return False


# GET USERCONFIG


def get_userconfig_structure() -> dict:
    """
    :return: dict that contains USERCONFIG.ini structure:
    {SECTION: {element: [default_value, required**, comment]}}

    **can't be deleted by user (is mandatory)
    """
    return {
        "UI SETTINGS": {
            "menu_name": ["Help", True, "you can use '/' to add submenus (like: 'Help/SubmenuName')"]
        },
        "READ WRITE COLORS": {
            "exr": ["0.28 | 0.49 | 0.56", False, ""],
            "jpeg": ["0.56 | 0.39 | 0.28", False, ""],
            "jpg": ["0.48 | 0.28 | 0.56", False, ""],
            "tiff": ["0.56 | 0.56 | 0.56", False, ""],
            "mov": ["0.00 | 0.62 | 1.00", False, ""],
            "png": ["0.56 | 0.28 | 0.29", False, ""],
            "dpx": ["0.56 | 0.56 | 0.28", False, ""],
            "psd": ["0.51 | 0.64 | 1.00", False, "you can add your own extensions!"]
        },
        "CONFIG EDITOR": {
            "Init.py": ["./init.py", False, ""],
            "Menu.py": ["./submenu.py", False, "path is specified relative to the .nuke directory"]
        }
    }


def get_userconfig_text(for_section: str = None) -> str:
    text = ""
    for section, item in get_userconfig_structure().items():

        if for_section and not section == for_section:
            continue

        text += f"[{section}]\n"

        for element, subitem in item.items():
            default_value = subitem[0]
            comment = subitem[2]

            text += f"{element} = {default_value}\n"

            if comment:
                text += f"# {comment}\n"

        text += "\n\n"

    return text


def get_required_sections_elements(for_section: str = None) -> list:
    """
    return: [(section, element)]
    """
    result = []

    for section, item in get_userconfig_structure().items():

        if for_section and not section == for_section:
            continue

        for element, subitem in item.items():
            required = subitem[1]

            if required:
                result.append((section, element))

    return result


# FILE USERCONFIG


def get_userconfig_path():
    return os.path.join(configHelper.get_config_folder(), "USERCONFIG.ini").replace("\\", "/")

def parse_userconfig():
    userconfig = configparser.ConfigParser()
    userconfig.read(get_userconfig_path())
    return userconfig


def create_userconfig():
    userconfig_path = get_userconfig_path()

    if os.path.exists(userconfig_path):
        raise Exception(userconfig_path + " already exists!")

    with open(userconfig_path, "w") as f:
        f.write(get_userconfig_text())


def add_section_to_userconfig(section: str):
    with open(get_userconfig_path(), "a") as f:
        f.write(get_userconfig_text(section))


# CHECK USERCONFIG


def check_userconfig_exists():
    if os.path.exists(get_userconfig_path()):
        return True
    return False


def check_section_exists(section: str) -> bool:
    if section in parse_userconfig().sections():
        return True
    return False


def check_element_exists(section, required_element):
    if required_element in list(parse_userconfig()[section]):
        return True
    return False


def check_UI_SETTINGS_quantity_of_elements() -> bool:
    if len(list(parse_userconfig()["UI SETTINGS"])) == 1:
        return True
    return False


def check_READ_WRITE_COLORS_elements_values() -> tuple:
    userconfig = parse_userconfig()
    section_name = "READ WRITE COLORS"

    for element in list(userconfig[section_name]):
        rgb_value = userconfig[section_name][element]
        if not check_color_string_validity(rgb_value):
            return False, element, rgb_value
    return True, None, None


def check_CONFIG_EDITOR_elements_values() -> tuple:
    userconfig = parse_userconfig()
    section_name = "CONFIG EDITOR"
    for element in list(userconfig[section_name]):
        path_value = userconfig[section_name][element]
        if not check_path_validity(path_value):
            return False, element, path_value
    return True, None, None

def check_userconfig_before_start_nuke() -> None:
    # Проверка существует ли конфиг
    if not check_userconfig_exists():
        return

    # Проверка наличия в конфиге необходимых секций
    for required_section in ["UI SETTINGS"]:
        if required_section not in parse_userconfig().sections():
            raise_error(message=f"Section '{required_section}' - not found!")

    # Проверка наличия в конфиге необходимых элементов
    for item in get_required_sections_elements():
        section, element = item[0], item[1]
        if not check_element_exists(section, element):
            raise_error(message=f"In section '{section}' element '{element}' - not found!")

    # Проверка значений в UI SETTINGS
    if not check_UI_SETTINGS_quantity_of_elements():
        raise_error(message=f"In section 'UI SETTINGS' - wrong number of elements!")

    # Проверка значений в READ WRITE COLORS
    if check_section_exists("READ WRITE COLORS"):
        check, element, rgb_value = check_READ_WRITE_COLORS_elements_values()
        if not check:
            raise_error(message=f"In section 'READ WRITE COLORS' element '{element}' - syntax error!",
                        error_line=[find_element_line(element, rgb_value), rgb_value])

    # Проверка значений в CONFIG EDITOR
    if check_section_exists("CONFIG EDITOR"):
        check, element, path_value = check_CONFIG_EDITOR_elements_values()
        if not check:
            raise_error(message=f"In section 'CONFIG EDITOR' element '{element}' - syntax error!",
                        error_line=[find_element_line(element, path_value), path_value])


def update_userconfig_before_start_nuke() -> None:
    # Создание конфига, если его нет и возвращение из функции в таком случае
    if not check_userconfig_exists():
        create_userconfig()
        return

    # Добавление в конфиг секций, если их не существует
    for requiered_section in get_userconfig_structure():
        if requiered_section not in parse_userconfig().sections():
            add_section_to_userconfig(requiered_section)
