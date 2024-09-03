from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QAction

from little_helpers.vp_show_shortcuts_in_tab_menu import show_shortcuts_in_tab_menu

from little_helpers.vp_little_helpers import qtHelper
from little_helpers.vp_little_helpers import configHelper


# work with config
def write_config_settings(action):
    configHelper.write_config("show_shortcuts_in_tab_menu", action.isChecked())


def load_config_settings(action):
    if configHelper.check_key("show_shortcuts_in_tab_menu"):
        action.setChecked(configHelper.read_config_key("show_shortcuts_in_tab_menu"))


# create action
action = QAction("Show Shortcuts in Tab menu?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addAction(action)

# set triggers for action: save config + start read_write_coloriser
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: show_shortcuts_in_tab_menu.start())

# when initialize Nuke
load_config_settings(action)
# start after 1 second after loading Nuke - so we can find NodeGraph QWidget
QTimer.singleShot(1 * 1000, show_shortcuts_in_tab_menu.start)
