"""
"""
import nuke


# # # # # # # # # # # # # # #  OTHER # # # # # # # # # # # # # # #

# description: you can change menu where VP_LittleHelpers will be added.
# by default, it is menu with name 'Help'

little_helpers_menu = nuke.menu("Nuke").addMenu("Help")


# # # # # # # # # # # # # # #  HELPER: READ WRITE COLORISER # # # # # # # # # # # # # # #

# description: ...
# supported values: ...

coloriser_colors = {
"exr": [0.282, 0.494, 0.564],
"jpeg": [0.564, 0.392, 0.282],
"jpg": [0.482, 0.282, 0.564],
"tiff": [0.564, 0.564, 0.564],
"mov": [0.0, 0.623, 1.0],
"png": [0.564, 0.282, 0.286],
"dpx": [0.564, 0.560, 0.282],
"psd": [0.505, 0.639, 1.0]
}


# # # # # # # # # # # # # # #  HELPER: CONFIG EDITOR # # # # # # # # # # # # # # #

# description: here you can add name of item and path to folder or file.
# then you will have ability to open this files from inside Nuke.
# supported values №1: string, name of item in Nuke menu
# supported values №2: string, path to directory or file relatively .nuke folder*
# * file path should start with "./"!

config_editor_files = {
"Autolabel": "./PythonConstruct/custom_autolabel.py",
"CallBacks": "./PythonConstruct/custom_callbacks.py",
"Favorite": "./PythonConstruct/custom_favorite.py",
"Guides": "./PythonConstruct/custom_guides.py",
"HotKeys": "./PythonConstruct/set_nuke_hot_keys.py",
"Knob Defaults": "./PythonConstruct/set_nuke_knobs_default.py",
"Plugin Path": "./PythonConstruct/set_nuke_plugin_paths.py",
}
