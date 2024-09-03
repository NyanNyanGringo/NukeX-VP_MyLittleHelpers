from PySide2.QtWidgets import QAction

from little_helpers.vp_little_helpers import qtHelper, configHelper

from little_helpers.vp_default_viewer_state_is_input import default_viewer_state_is_input

CONFIG_KEY = "use_default_viewer_state_as_input"
STUDIO_CONFIG_KEY = "LITTLE_HELPERS_DEFAULT_VIEWER_STATE_IS_INPUT"


def write_config_settings(action):
    configHelper.write_config(CONFIG_KEY, action.isChecked())


# create action
action = QAction("Set Default Viewer State as Input?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addMenu("Viewer").addAction(action)

# initialize when Nuke starts up
configHelper.load_config_settings(action=action, config_key=CONFIG_KEY, studio_config_key=STUDIO_CONFIG_KEY)
default_viewer_state_is_input.start(action)

# set triggers for action
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: default_viewer_state_is_input.start(action))
