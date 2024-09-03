from PySide2.QtWidgets import QAction

from little_helpers.vp_little_helpers import qtHelper, configHelper

from little_helpers.vp_disconnect_viewers_inputs_after_script_load import disconnect_viewers_inputs_after_script_load

CONFIG_KEY = "use_disconnect_viewer_inputs"
STUDIO_CONFIG_KEY = "LITTLE_HELPERS_DISCONNECT_VIEWERS_INPUTS_WHEN_SCRIPT_LOAD"


def write_config_settings(action):
    configHelper.write_config(CONFIG_KEY, action.isChecked())


# create action
action = QAction("Disconnect Viewer Inputs After Script Load?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addMenu("Viewer").addAction(action)

# initialize when Nuke starts up
configHelper.load_config_settings(action=action, config_key=CONFIG_KEY, studio_config_key=STUDIO_CONFIG_KEY)
disconnect_viewers_inputs_after_script_load.start(action)

# set triggers for action
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: disconnect_viewers_inputs_after_script_load.start(action))
