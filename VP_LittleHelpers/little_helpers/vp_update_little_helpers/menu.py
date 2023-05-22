import webbrowser

from PySide2.QtWidgets import QAction

import little_helpers.vp_update_little_helpers.update_little_helpers as update_little_helpers

from little_helpers.vp_little_helpers import qtHelper, configHelper


# create action
action = QAction("Check VP_LittleHelper updates...")

# add action to menu
qtHelper.create_and_get_helper_menu().addAction(action)

# set triggers for action
action.triggered.connect(lambda: update_little_helpers.start(action))

update_little_helpers.start(action, start_when_initialize=True)
