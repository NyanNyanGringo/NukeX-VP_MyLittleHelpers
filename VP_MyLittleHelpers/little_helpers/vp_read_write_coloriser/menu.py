import nuke

from PySide2.QtWidgets import QAction

from little_helpers.vp_little_helpers import qtHelper, configHelper

import little_helpers.vp_read_write_coloriser.read_write_coloriser as read_write_coloriser

CONFIG_KEY = "use_coloriser"
STUDIO_CONFIG_KEY = "LITTLE_HELPERS_READ_WRITE_COLORIZER"


def write_config_settings(action):
    configHelper.write_config(CONFIG_KEY, action.isChecked())


# create action
action = QAction("Use Read Write Coloriser?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addAction(action)

# when initialize Nuke
configHelper.load_config_settings(action=action, config_key=CONFIG_KEY, studio_config_key=STUDIO_CONFIG_KEY)
read_write_coloriser.start(action)

# set triggers for action
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: read_write_coloriser.start(action))

# when script loads
nuke.addOnScriptLoad(lambda: read_write_coloriser.start(action))
