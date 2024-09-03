from PySide2.QtWidgets import QAction

from little_helpers.vp_little_helpers import qtHelper, configHelper

import little_helpers.vp_smart_autosave.smart_autosave as smart_autosave

CONFIG_KEY = "use_smart_autosave"
STUDIO_CONFIG_KEY = "LITTLE_HELPERS_SMART_AUTOSAVE"


def write_config_settings(action):
    configHelper.write_config(CONFIG_KEY, action.isChecked())


# create action
action = QAction("Use Smart AutoSave?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addAction(action)

# initialize when Nuke starts up
configHelper.load_config_settings(action=action, config_key=CONFIG_KEY, studio_config_key=STUDIO_CONFIG_KEY)
smart_autosave.start(action)

# set triggers for action
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: smart_autosave.start(action))
