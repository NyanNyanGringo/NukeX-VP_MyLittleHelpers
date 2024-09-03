from PySide2.QtWidgets import QAction

from little_helpers.vp_little_helpers import qtHelper, configHelper

import little_helpers.vp_compare_versions_before_render.compare_versions_before_render as compare_versions_before_render

CONFIG_KEY = "use_compare_versions_before_render"
STUDIO_CONFIG_KEY = "LITTLE_HELPERS_COMPARE_VERSIONS_BEFORE_RENDER"


def write_config_settings(action):
    configHelper.write_config(CONFIG_KEY, action.isChecked())


# create action
action = QAction("Compare Versions Before Render?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addMenu("Render").addAction(action)

# initialize when Nuke starts up
configHelper.load_config_settings(action=action, config_key=CONFIG_KEY, studio_config_key=STUDIO_CONFIG_KEY)
compare_versions_before_render.start(action)

# set triggers for action
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: compare_versions_before_render.start(action))
