import nuke

from vp_little_helpers import qtHelper


def disconnect_viewer_inputs():
    for node in nuke.allNodes():
        if node.Class() == 'Viewer':
            for _input in range(0, node.inputs()):
                node.setInput(_input, None)


def start():
    if qtHelper.check_action_is_checked(config_key="use_disconnect_viewer_inputs"):
        nuke.addOnScriptLoad(disconnect_viewer_inputs)
    else:
        nuke.removeOnScriptLoad(disconnect_viewer_inputs)
