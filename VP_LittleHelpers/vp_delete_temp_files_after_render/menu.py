import nuke

from PySide2.QtWidgets import QAction

import vp_delete_temp_files_after_render.delete_temp_files_after_render as delete_temp_files_after_render

from vp_little_helpers import configHelper

import __userconfig_little_helpers__ as userconfig


# work with config
def write_config_settings(action):
    configHelper.write_config("use_delete_temp_files_after_render", action.isChecked())


def load_config_settings(action):
    if configHelper.check_key("use_delete_temp_files_after_render"):
        action.setChecked(configHelper.read_config_key("use_delete_temp_files_after_render"))


# create action
action = QAction("Delete .temp Files After Render?")
action.setCheckable(True)

# add action to menu
userconfig.little_helpers_menu.addMenu("Render").addAction(action)

# set triggers for action: save config + start read_write_coloriser
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: delete_temp_files_after_render.set_delete_temp_files_after_render())

# when initialize Nuke
load_config_settings(action)
delete_temp_files_after_render.set_delete_temp_files_after_render()

# add callbacks
nuke.addOnScriptLoad(delete_temp_files_after_render.set_delete_temp_files_after_render)
