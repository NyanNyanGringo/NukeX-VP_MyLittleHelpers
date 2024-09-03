from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QAction

from little_helpers.vp_little_helpers import qtHelper, configHelper

from little_helpers.vp_show_shortcuts_in_tab_menu import show_shortcuts_in_tab_menu

CONFIG_KEY = "show_shortcuts_in_tab_menu"
STUDIO_CONFIG_KEY = "LITTLE_HELPERS_SHOW_SHORTCUTS_IN_TAB_MENU"


def write_config_settings(action):
    configHelper.write_config(CONFIG_KEY, action.isChecked())


# create action
action = QAction("Show Shortcuts in Tab menu?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addAction(action)

# initialize when Nuke starts up
configHelper.load_config_settings(action=action, config_key=CONFIG_KEY, studio_config_key=STUDIO_CONFIG_KEY)

# start after 1 second after loading Nuke - so we can find NodeGraph QWidget
QTimer.singleShot(1 * 1000, lambda: show_shortcuts_in_tab_menu.start(action))

# set triggers for action
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: show_shortcuts_in_tab_menu.start(action))
