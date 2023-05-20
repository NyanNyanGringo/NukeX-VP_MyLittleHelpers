import nuke

from PySide2.QtWidgets import QAction

import vp_smart_autosave.smart_autosave as smart_autosave

from vp_little_helpers import configHelper, qtHelper


# work with config
def write_config_settings(action):
    configHelper.write_config("use_smart_autosave", action.isChecked())


def load_config_settings(action):
    if configHelper.check_key("use_smart_autosave"):
        action.setChecked(configHelper.read_config_key("use_smart_autosave"))


# create action
action = QAction("Use Smart AutoSave?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addAction(action)

# set triggers for action: save config + start read_write_coloriser
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: smart_autosave.start())

# when initialize Nuke
load_config_settings(action)
smart_autosave.start()

# add callbacks
nuke.addOnScriptLoad(smart_autosave.start)
