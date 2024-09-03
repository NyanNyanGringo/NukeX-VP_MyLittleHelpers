import nuke


def disconnect_viewer_inputs():
    for node in nuke.allNodes():
        if node.Class() == 'Viewer':
            for _input in range(0, node.inputs()):
                node.setInput(_input, None)


ON_SCRIPT_LOAD = disconnect_viewer_inputs


def start(action):
    if action.isChecked():
        nuke.addOnScriptLoad(ON_SCRIPT_LOAD)
    else:
        nuke.removeOnScriptLoad(ON_SCRIPT_LOAD)
