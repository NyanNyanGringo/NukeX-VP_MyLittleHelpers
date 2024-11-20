from PySide2.QtWidgets import QAction

from little_helpers.vp_little_helpers import qtHelper, configHelper

from little_helpers.vp_dot_aligner import dot_aligner

CONFIG_KEY = "dot_aligner"
STUDIO_CONFIG_KEY = "LITTLE_HELPERS_DOT_ALIGNER"


def write_config_settings(action):
    configHelper.write_config(CONFIG_KEY, action.isChecked())


# create action
action = QAction("Use dot aligner?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addAction(action)

# initialize when Nuke starts up
configHelper.load_config_settings(action=action, config_key=CONFIG_KEY, studio_config_key=STUDIO_CONFIG_KEY)

# set triggers for action
nuke.addKnobChanged(lambda: dot_aligner.start(action))
