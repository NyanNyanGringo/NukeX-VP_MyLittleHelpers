"""
"""

# # # # # # # # # # # # # # #  HELPER: CONFIG OPENER # # # # # # # # # # # # # # #

# description: show/hide config editor
# supported values: True | False

config_editor_active = True

# description: here you can add name of item and path to folder or file.
# then you will have ability to open this files from inside Nuke.
# supported values №1: string, name of item in Nuke menu
# supported values №2: string, path to directory or file relatively .nuke folder

config_editor_files = {
"Autolabel": "./PythonConstruct/custom_autolabel.py",
"CallBacks": "./PythonConstruct/custom_callbacks.py",
"Favorite": "./PythonConstruct/custom_favorite.py",
"Guides": "./PythonConstruct/custom_guides.py",
"HotKeys": "./PythonConstruct/set_nuke_hot_keys.py",
"Knob Defaults": "./PythonConstruct/set_nuke_knobs_default.py",
"Plugin Path": "./PythonConstruct/set_nuke_plugin_paths.py",
}
