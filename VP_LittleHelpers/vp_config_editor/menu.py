import nuke
import os

import __userconfig_little_helpers__ as userconfig

import vp_config_editor.config_editor as config_editor


# variables
nuke_plugin_path = (os.environ['HOME'] + '/.nuke').replace("\\", "/")

# menu
menu_help = nuke.menu("Nuke").addMenu(userconfig.little_helpers_menu)
menu_open = menu_help.addMenu("Config Opener")

# add open .nuke dir command
menu_open.addCommand(".nuke", "os.startfile('" + nuke_plugin_path + "')")
menu_open.addSeparator()

# add command from userconfig
for key, value in userconfig.config_editor_files.items():
    p = (nuke_plugin_path + value[1:]).replace("\\", "/")
    menu_open.addCommand(key, "os.startfile('" + p + "')")
menu_open.addSeparator()

# add restart nuke command
menu_open.addCommand("Restart Nuke", config_editor.restart_any_nuke)
