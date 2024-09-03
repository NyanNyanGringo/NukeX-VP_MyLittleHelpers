from PySide2.QtWidgets import QAction

from little_helpers.vp_little_helpers import qtHelper, configHelper

from little_helpers.vp_viewer_beside import viewer_beside

CONFIG_KEY = "use_viewer_beside"
STUDIO_CONFIG_KEY = "LITTLE_HELPERS_VIEWER_BESIDE"


def write_config_settings(action):
    configHelper.write_config(CONFIG_KEY, action.isChecked())


# create action
action = QAction("Place Viewer Next to the Viewed Node?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addMenu("Viewer").addAction(action)

# initialize when Nuke starts up
configHelper.load_config_settings(action=action, config_key=CONFIG_KEY, studio_config_key=STUDIO_CONFIG_KEY)
viewer_beside.start(action)

# set triggers for action
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: viewer_beside.start(action))
