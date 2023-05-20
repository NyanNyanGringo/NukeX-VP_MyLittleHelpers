from vp_little_helpers import configHelper


def check_action_is_checked(config_key):
    """
    Check action is checked by using config key
    :param config_key: string
    :return: bool
    """
    if configHelper.check_key(config_key):
        return configHelper.read_config_key(config_key)
    return False
