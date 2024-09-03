from PySide2.QtWidgets import QAction

from little_helpers.vp_little_helpers import qtHelper, configHelper

import little_helpers.vp_delete_temp_files_after_render.delete_temp_files_after_render as delete_temp_files_after_render

CONFIG_KEY = "use_delete_temp_files_after_render"
STUDIO_CONFIG_KEY = "LITTLE_HELPERS_DELETE_TEMP_FILES_AFTER_RENDER"


def write_config_settings(action):
    configHelper.write_config(CONFIG_KEY, action.isChecked())


# create action
action = QAction("Delete .temp Files After Render?")
action.setCheckable(True)

# add action to menu
qtHelper.create_and_get_helper_menu().addMenu("Render").addAction(action)

# initialize when Nuke starts up
configHelper.load_config_settings(action=action, config_key=CONFIG_KEY, studio_config_key=STUDIO_CONFIG_KEY)
delete_temp_files_after_render.start(action)

# set triggers for action
action.triggered.connect(lambda: write_config_settings(action))
action.triggered.connect(lambda: delete_temp_files_after_render.start(action))
