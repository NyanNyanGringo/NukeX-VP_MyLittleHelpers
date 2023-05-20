import nuke

from PySide2.QtWidgets import QApplication

from vp_little_helpers import qtHelper


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


def change_viewer_to_input_or_global(viewer_node, close_viewer=True, state="Input"):
    viewer = find_viewer(viewer_node)
    fr = find_framerange(viewer)
    input_action = [act for act in fr.menu().actions() if act.text() == state][0]
    input_action.trigger()

    # if "1" in viewer_node.name():
    #     return

    # if close_viewer:
    #     viewer.close()


def change_viewerS_to_input():
    for node in nuke.allNodes():
        if node.Class() == "Viewer":
            change_viewer_to_input_or_global(node)


def change_viewerS_to_global():
    for node in nuke.allNodes():
        if node.Class() == "Viewer":
            change_viewer_to_input_or_global(node, state="Global")


def change_viewer_to_input_when_user_create():
    change_viewer_to_input_or_global(nuke.thisNode(), close_viewer=False)


def change_viewer_to_input_when_script_load():
    nuke.removeOnCreate(change_viewer_to_input_when_user_create, nodeClass="Viewer")
    change_viewerS_to_input()
    nuke.addOnCreate(change_viewer_to_input_when_user_create, nodeClass="Viewer")


def change_viewer_to_input_when_widget_opens():
    if nuke.thisKnob().name() == "renderer":
        change_viewer_to_input_or_global(nuke.thisNode(), close_viewer=False)


def start(called_from_user=False):
    # if qtHelper.check_action_is_checked(config_key="use_default_viewer_state_as_input") and called_from_user:
        # change_viewer_to_input_when_script_load()
    if qtHelper.check_action_is_checked(config_key="use_default_viewer_state_as_input"):
        # nuke.message("Nuke Started!")
        # nuke.addOnScriptLoad(change_viewer_to_input_when_script_load)
        change_viewerS_to_input()
        nuke.addKnobChanged(change_viewer_to_input_when_widget_opens, nodeClass="Viewer")
    else:
        change_viewerS_to_global()
        nuke.removeKnobChanged(change_viewer_to_input_when_widget_opens, nodeClass="Viewer")
        # nuke.removeOnScriptLoad(change_viewer_to_input_when_script_load)
        # nuke.removeOnCreate(change_viewer_to_input_when_user_create, nodeClass="Viewer")
