from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QAction

from little_helpers.vp_version_up_remidner import version_up_reminder

from little_helpers.vp_little_helpers import qtHelper
from little_helpers.vp_little_helpers import configHelper


# work with config
def write_config_settings(action):
    configHelper.write_config("version_up_reminder", action.isChecked())


def load_config_settings(action):
    if configHelper.check_key("version_up_reminder"):
        action.setChecked(configHelper.read_config_key("version_up_reminder"))


# create action
action = QAction("Use VersionUp Reminder?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addAction(action)

# set triggers for action: save config + start read_write_coloriser
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: version_up_reminder.start())

# when initialize Nuke
load_config_settings(action)
# start after 1 second after loading Nuke
QTimer.singleShot(1 * 1000, version_up_reminder.start)
