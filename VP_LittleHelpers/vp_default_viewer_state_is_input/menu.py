import nuke

from PySide2.QtWidgets import QAction

import vp_default_viewer_state_is_input.default_viewer_state_is_input as default_viewer_state_is_input

from vp_little_helpers import configHelper

import __userconfig_little_helpers__ as userconfig


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
userconfig.little_helpers_menu.addMenu("Viewer").addAction(action)

# set triggers for action: save config + start read_write_coloriser
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: default_viewer_state_is_input.start(called_from_user=True))

# when initialize Nuke
load_config_settings(action)
default_viewer_state_is_input.start(called_from_user=False)

# add callbacks
# nuke.addOnScriptLoad(default_viewer_state_is_input.start)
# nuke.addKnobChanged(lambda: print(nuke.thisKnob().name()), nodeClass="Viewer")
