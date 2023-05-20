import nuke

from PySide2.QtWidgets import QAction

import vp_read_write_coloriser.read_write_coloriser as read_write_coloriser

from vp_little_helpers import configHelper, qtHelper

# work with config
def write_config_settings(action):
    configHelper.write_config("use_coloriser", action.isChecked())


def load_config_settings(action):
    if configHelper.check_key("use_coloriser"):
        action.setChecked(configHelper.read_config_key("use_coloriser"))


# create action
action = QAction("Use Read Write Coloriser?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addAction(action)

# set triggers for action: save config + start read_write_coloriser
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: read_write_coloriser.set_all_read_and_write_tile_color())

# when initialize Nuke
load_config_settings(action)
read_write_coloriser.set_all_read_and_write_tile_color()

# add callbacks
nuke.addOnCreate(lambda: read_write_coloriser.set_tile_color_to_node(nuke.thisNode()), nodeClass='Read')
nuke.addOnCreate(lambda: read_write_coloriser.set_tile_color_to_node(nuke.thisNode()), nodeClass='Write')

nuke.addOnScriptLoad(read_write_coloriser.set_all_read_and_write_tile_color)

nuke.addKnobChanged(read_write_coloriser.colorise_on_node_create, nodeClass='Read')
nuke.addKnobChanged(read_write_coloriser.colorise_on_node_create, nodeClass='Write')
