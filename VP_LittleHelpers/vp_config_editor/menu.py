import nuke
import os

from vp_little_helpers import qtHelper, iniHelper

import vp_config_editor.config_editor as config_editor


# variables
nuke_plugin_path = (os.environ['HOME'] + '/.nuke').replace("\\", "/")
ini_config = iniHelper.get_ini_config()


# menu
menu_open = qtHelper.create_and_get_helper_menu().addMenu("Config Editor")


# add open .nuke dir command
menu_open.addCommand(".nuke", "os.startfile('" + nuke_plugin_path + "')")
menu_open.addSeparator()


# add command from userconfig
for action_name in list(ini_config["CONFIG EDITOR"]):
    relative_path_to_file = ini_config["CONFIG EDITOR"][action_name]
    full_path_to_file = (nuke_plugin_path + relative_path_to_file[1:]).replace("\\", "/")
    menu_open.addCommand(action_name, 'os.startfile("' + full_path_to_file + '")')
menu_open.addSeparator()


# add restart nuke command
menu_open.addCommand("Restart Nuke", config_editor.restart_any_nuke)
