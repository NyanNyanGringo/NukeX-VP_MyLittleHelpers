import nuke
import os

import _USER_CONFIG

import config_editor


# # # # # # # # # # # # # # # VARIABLES # # # # # # # # # # # # # # #


nuke_plugin_path = (os.environ['HOME'] + '/.nuke').replace("\\", "/")
menu_help = nuke.menu("Nuke").addMenu("Help")
menu_help.addSeparator()


# # # # # # # # # # # # # # # HELPER: CONFIG OPENER # # # # # # # # # # # # # # #


if _USER_CONFIG.config_editor_active:

    menu_open = menu_help.addMenu("Config Opener")

    menu_open.addCommand(".nuke", "os.startfile('" + nuke_plugin_path + "')")
    menu_open.addSeparator()

    for key, value in _USER_CONFIG.config_editor_files.items():
        p = (nuke_plugin_path + value[1:]).replace("\\", "/")
        menu_open.addCommand(key, "os.startfile('" + p + "')")

    menu_open.addSeparator()

    menu_open.addCommand("Restart Nuke", config_editor.restart_any_nuke)
