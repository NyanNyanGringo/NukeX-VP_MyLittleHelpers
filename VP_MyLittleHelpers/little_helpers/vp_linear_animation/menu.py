from PySide2.QtWidgets import QAction

from little_helpers.vp_little_helpers import qtHelper, configHelper

from little_helpers.vp_linear_animation import linear_animation

CONFIG_KEY = "use_linear_animation"
STUDIO_CONFIG_KEY = "LITTLE_HELPERS_LINEAR_ANIMATION"


def write_config_settings(action):
    configHelper.write_config(CONFIG_KEY, action.isChecked())


# create action
action = QAction("Kronos/TimeWarp Linear Animation On Create?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addAction(action)

# initialize when Nuke starts up
configHelper.load_config_settings(action=action, config_key=CONFIG_KEY, studio_config_key=STUDIO_CONFIG_KEY)
linear_animation.start(action)

# set triggers for action
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: linear_animation.start(action))
