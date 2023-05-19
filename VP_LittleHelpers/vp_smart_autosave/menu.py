import nuke
import os


# variables
nuke_plugin_path = (os.environ['HOME'] + '/.nuke').replace("\\", "/")
menu_help = nuke.menu("Nuke").addMenu("Help")
menu_help.addSeparator()

smart_autosave_command = menu_help.addCommand("Use Smart Autosave")
