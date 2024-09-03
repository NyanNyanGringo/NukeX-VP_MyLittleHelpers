import nuke
from PySide2.QtWidgets import QApplication

# from PySide2.QtWidgets import *
# from PySide2.QtGui import *
# from PySide2.QtCore import *

from little_helpers.vp_little_helpers import configHelper, userconfigHelper


# class CustomQMenu(QMenu):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def mouseReleaseEvent(self, event):
#         action = self.activeAction()
#         if action and action.isEnabled():
#             if not action.menu():
#                 action.trigger()
#             else:
#                 action.menu().exec_(self.mapToGlobal(event.pos()))
#         else:
#             super().mouseReleaseEvent(event)


def check_action_is_checked(config_key):
    """
    Check action is checked by using config key
    :param config_key: string
    :return: bool
    """
    if configHelper.check_key(config_key):
        return configHelper.read_config_key(config_key)
    return False


def create_and_get_helper_menu():
    """
    Create and Get menu for VP_MyLittleHelpers. If exists - return existed
    menu. Get menu name using ini_config
    :return: Nuke Menu
    """
    userconfig = userconfigHelper.parse_userconfig()
    menu_name = userconfig["UI SETTINGS"]["menu_name"].replace("\\", "/")

    menu = nuke.menu("Nuke")
    for m in menu_name.split("/"):
        menu = menu.addMenu(m)

    return menu


def get_node_graph_widget():
    import hiero.ui
    for widget in hiero.ui.windowManager().windows():
        if widget.windowTitle() == "Node Graph":
            if widget.metaObject().className() == "Foundry::UI::LinkedView":
                return widget
    raise Exception("Can't find NodeGraph!")


# def get_widget_methods(widget):
#     meta_object = widget.metaObject()
#     for i in range(meta_object.methodCount()):
#         method = meta_object.method(i)
#         print(method.methodSignature().data().decode())

DAG_OBJECT_NAME = "DAG"


def get_dag_widgets(visible=True):
    """
    Gets all Qt objects with DAG in the object name

    Args:
        visible (bool): Whether or not to return only visible widgets.

    Returns:
        list[QtWidgets.QWidget]
    """
    dags = []
    all_widgets = QApplication.instance().allWidgets()
    for widget in all_widgets:
        if DAG_OBJECT_NAME in widget.objectName():
            if not visible or (visible and widget.isVisible()):
                dags.append(widget)

    return dags


def get_current_dag():
    """
    Returns:
        QtWidgets.QWidget: The currently active DAG
    """
    visible_dags = get_dag_widgets(visible=True)
    for dag in visible_dags:
        if dag.hasFocus():
            return dag

    # IF None had focus, and we have at least one, use the first one
    if visible_dags:
        return visible_dags[0]
    return None
