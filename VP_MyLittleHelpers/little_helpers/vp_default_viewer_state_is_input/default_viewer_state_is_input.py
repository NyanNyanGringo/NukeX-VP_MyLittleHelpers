import nuke

from PySide2.QtWidgets import QApplication


def find_viewer(viewer):
    nuke.show(viewer, False)
    for widget in QApplication.allWidgets():
        if widget.windowTitle() == viewer.name():
            return widget

    return False


def find_framerange(qtObject):
    for c in qtObject.children():
        found = find_framerange(c)
        if found:
            return found
        try:
            tt = c.toolTip().lower()
            if tt.startswith("frameslider range"):
                return c
        except:
            pass


def change_viewer_to_input_or_global(viewer_node, state):
    """
    :
    :param viewer_node: Nuke Node with Class Viewer
    :param state: str, Input | Global
    :return: None
    """
    viewer = find_viewer(viewer_node)
    fr = find_framerange(viewer)
    input_action = [act for act in fr.menu().actions() if act.text() == state][0]
    input_action.trigger()


def change_viewerS_to_input():
    for node in nuke.allNodes():
        if node.Class() == "Viewer":
            change_viewer_to_input_or_global(node, state="Input")


def change_viewerS_to_global():
    for node in nuke.allNodes():
        if node.Class() == "Viewer":
            change_viewer_to_input_or_global(node, state="Global")


def change_viewer_to_input_when_widget_opens():
    if nuke.thisKnob().name() == "renderer":
        change_viewer_to_input_or_global(nuke.thisNode(), state="Input")


KNOB_CHANGED_CALLBACK = change_viewer_to_input_when_widget_opens


def start(action):
    if action.isChecked():
        change_viewerS_to_input()
        nuke.addKnobChanged(KNOB_CHANGED_CALLBACK, nodeClass="Viewer")
    else:
        change_viewerS_to_global()
        nuke.removeKnobChanged(KNOB_CHANGED_CALLBACK, nodeClass="Viewer")
