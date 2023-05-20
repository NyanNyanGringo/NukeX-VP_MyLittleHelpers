from vp_little_helpers import iniHelper
import nuke


def error_message(text,  say_about_download=True, string_number=-1):
    """
    Developer helper to write message about problem in USERCONFIG.ini
    :param text: message text
    :param say_about_download: bool
    :param string_number: int
    :return: None
    """
    basic_text = "VP_LittleHelpers\nERROR: " + iniHelper.get_ini_config_path()

    if not string_number == -1 and string_number >= 0:
        basic_text += "\nMISTAKE: " + str(string_number) + " string"

    basic_text += "\n\n"

    download_text = ""
    if say_about_download:
        download_text = "\n\nMake changes manually or download USERCONFIG.ini again."

    nuke.message(basic_text + text + download_text)


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


# variables
ini_config = iniHelper.get_ini_config()


# check section numbers are correct
if not len(ini_config.sections()) == 3:
    error_message(
        text="USERCONFIG.ini doesn't exists or have wrong number of sections!\n\n"
    )
    raise SystemExit

# check all sections exists and have correct name
for section in ["UI SETTINGS", "READ WRITE COLORS", "CONFIG EDITOR"]:
    if section not in ini_config.sections():
        error_message(
            text="I can't find section with name " + section + " in USERCONFIG.ini")
        raise SystemExit


# check UI SETTINGS section
section_name = "UI SETTINGS"
if not len(list(ini_config[section_name])) == 1:
    error_message(text="Wrong number of elements in UI SETTINGS section!")
    raise SystemExit

for element in list(ini_config[section_name]):
    if not element == "menu_name":
        error_message(text="First element in UI SETTINGS section should be names as menu_name!")
        raise SystemExit


# check READ WRITE COLORS section
section_name = "READ WRITE COLORS"
for element in list(ini_config[section_name]):
    rgb_value = ini_config[section_name][element]
    if not check_color_string_validity(rgb_value):
        error_message(text="You have incorrect format for RGB value for " + element)
        raise SystemExit


# check CONFIG EDITOR section
section_name = "CONFIG EDITOR"
for element in list(ini_config[section_name]):
    path_value = ini_config[section_name][element]
    if not check_path_validity(path_value):
        error_message(text="You have incorrect format for path value for " + element)
        raise SystemExit
