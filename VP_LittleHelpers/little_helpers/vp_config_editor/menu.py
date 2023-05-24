import os

from little_helpers.vp_little_helpers import qtHelper, userconfigHelper

import little_helpers.vp_config_editor.config_editor as config_editor


# variables
nuke_plugin_path = (os.environ['HOME'] + '/.nuke').replace("\\", "/")
userconfig = userconfigHelper.parse_userconfig()


# menu
menu_open = qtHelper.create_and_get_helper_menu().addMenu(".nuke Editor")


# add open .nuke dir command
menu_open.addCommand(".nuke", "little_helpers.vp_little_helpers.osHelpers.startfile('" + nuke_plugin_path + "')")
menu_open.addSeparator()


# add command from userconfig
for action_name in list(userconfig["CONFIG EDITOR"]):
    relative_path_to_file = userconfig["CONFIG EDITOR"][action_name]
    full_path_to_file = (nuke_plugin_path + relative_path_to_file[1:]).replace("\\", "/")
    menu_open.addCommand(action_name, 'little_helpers.vp_little_helpers.osHelpers.startfile("'+full_path_to_file+'")')
menu_open.addSeparator()


# add restart nuke command
menu_open.addCommand("Restart Nuke", config_editor.restart_any_nuke)
