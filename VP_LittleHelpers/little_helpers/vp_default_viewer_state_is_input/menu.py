from PySide2.QtWidgets import QAction

from little_helpers.vp_default_viewer_state_is_input import default_viewer_state_is_input

from little_helpers.vp_little_helpers import qtHelper
from little_helpers.vp_little_helpers import configHelper


# work with config
def write_config_settings(action):
    configHelper.write_config("use_default_viewer_state_as_input", action.isChecked())


def load_config_settings(action):
    if configHelper.check_key("use_default_viewer_state_as_input"):
        action.setChecked(configHelper.read_config_key("use_default_viewer_state_as_input"))


# create action
action = QAction("Set Default Viewer State as Input?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addMenu("Viewer").addAction(action)

# set triggers for action: save config + start read_write_coloriser
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: default_viewer_state_is_input.start())

# when initialize Nuke
load_config_settings(action)
default_viewer_state_is_input.start()
