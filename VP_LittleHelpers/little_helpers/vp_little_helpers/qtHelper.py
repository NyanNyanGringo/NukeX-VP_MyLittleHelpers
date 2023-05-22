from little_helpers.vp_little_helpers import configHelper, userconfigHelper
import nuke


def check_action_is_checked(config_key):
    """
    Check action is checked by using config key
    :param config_key: string
    :return: bool
    """
    if configHelper.check_key(config_key):
        return configHelper.read_config_key(config_key)
    return False


def create_and_get_helper_menu():
    """
    Create and Get menu for VP_LittleHelpers. If exists - return existed
    menu. Get menu name using ini_config
    :return: Nuke Menu
    """
    userconfig = userconfigHelper.parse_userconfig()
    menu_name = userconfig["UI SETTINGS"]["menu_name"].replace("\\", "/")

    menu = nuke.menu("Nuke")
    for m in menu_name.split("/"):
        menu = menu.addMenu(m)

    return menu
