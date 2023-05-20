import nuke

from PySide2.QtWidgets import QAction

import vp_compare_versions_before_render.compare_versions_before_render as compare_versions_before_render

from vp_little_helpers import configHelper

import __userconfig_little_helpers__ as userconfig


# work with config
def write_config_settings(action):
    configHelper.write_config("use_compare_versions_before_render", action.isChecked())


def load_config_settings(action):
    if configHelper.check_key("use_compare_versions_before_render"):
        action.setChecked(configHelper.read_config_key("use_compare_versions_before_render"))


# create action
action = QAction("Compare Versions Before Render?")
action.setCheckable(True)

# add action to menu
userconfig.little_helpers_menu.addMenu("Render").addAction(action)

# set triggers for action: save config + start read_write_coloriser
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: compare_versions_before_render.set_compare_versions_before_render())

# when initialize Nuke
load_config_settings(action)
compare_versions_before_render.set_compare_versions_before_render()

# add callbacks
nuke.addOnScriptLoad(compare_versions_before_render.set_compare_versions_before_render)
