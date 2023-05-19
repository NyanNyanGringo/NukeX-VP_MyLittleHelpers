import nuke
import nukescripts

from PySide2.QtWidgets import QAction

import read_write_coloriser
import coloriser_config_helper


def write_config_settings(action):
	coloriser_config_helper.write_config("use_coloriser", action.isChecked())


def load_config_settings(action):
    if coloriser_config_helper.check_key("use_coloriser"):
    	action.setChecked(coloriser_config_helper.read_config_key("use_coloriser"))



action = QAction("Colorise Read and Write?")
action.setCheckable(True)


menu = nuke.menu("Nuke").addMenu("Tools")
menu.addAction(action)


action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: read_write_coloriser.set_all_read_and_write_tile_color())


# START
load_config_settings(action)
read_write_coloriser.set_all_read_and_write_tile_color()
