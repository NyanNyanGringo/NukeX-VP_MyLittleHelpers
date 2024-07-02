from PySide2.QtWidgets import QAction

from little_helpers.vp_linear_animation import linear_animation

from little_helpers.vp_little_helpers import qtHelper
from little_helpers.vp_little_helpers import configHelper


# work with config
def write_config_settings(action):
    configHelper.write_config("use_linear_animation", action.isChecked())


def load_config_settings(action):
    if configHelper.check_key("use_linear_animation"):
        action.setChecked(configHelper.read_config_key("use_linear_animation"))


# create action
action = QAction("Kronos/TimeWarp Linear Animation On Create?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addAction(action)

# set triggers for action: save config + start read_write_coloriser
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: linear_animation.start())

# when initialize Nuke
load_config_settings(action)
linear_animation.start()
