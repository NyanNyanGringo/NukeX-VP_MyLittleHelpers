from PySide2.QtWidgets import QAction

from little_helpers.vp_viewer_beside import viewer_beside

from little_helpers.vp_little_helpers import qtHelper
from little_helpers.vp_little_helpers import configHelper


# work with config
def write_config_settings(action):
    configHelper.write_config("use_viewer_beside", action.isChecked())


def load_config_settings(action):
    if configHelper.check_key("use_viewer_beside"):
        action.setChecked(configHelper.read_config_key("use_viewer_beside"))


# create action
action = QAction("Place Viewer Next to the Viewed Node?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addMenu("Viewer").addAction(action)

# set triggers for action: save config + start read_write_coloriser
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: viewer_beside.start())

# when initialize Nuke
load_config_settings(action)
viewer_beside.start()
