import nuke

from PySide2.QtWidgets import QAction

import vp_disconnect_viewers_inputs_after_script_load.disconnect_viewers_inputs_after_script_load as \
    disconnect_viewers_inputs_after_script_load

from vp_little_helpers import configHelper

import __userconfig_little_helpers__ as userconfig


# work with config
def write_config_settings(action):
    configHelper.write_config("use_disconnect_viewer_inputs", action.isChecked())


def load_config_settings(action):
    if configHelper.check_key("use_disconnect_viewer_inputs"):
        action.setChecked(configHelper.read_config_key("use_disconnect_viewer_inputs"))


# create action
action = QAction("Disconnect Viewer Inputs After Script Load?")
action.setCheckable(True)

# add action to menu
userconfig.little_helpers_menu.addMenu("Viewer").addAction(action)

# set triggers for action: save config + start read_write_coloriser
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: disconnect_viewers_inputs_after_script_load.set_disconnect_viewer_inputs())

# when initialize Nuke
load_config_settings(action)
disconnect_viewers_inputs_after_script_load.set_disconnect_viewer_inputs()

# add callbacks
nuke.addOnScriptLoad(disconnect_viewers_inputs_after_script_load.set_disconnect_viewer_inputs)
