import nuke

from little_helpers.vp_little_helpers import userconfigHelper


def viewer_beside():
    viewer = nuke.thisNode()
    kn = nuke.thisKnob()
    # input_number когда меняется номер 1 2 3...
    # inputChange если номер не поменялся, а перескочили на другую ноду
    if kn.name() in ['input_number', 'inputChange']:
        activeViewer = nuke.activeViewer()
        if kn.name() == 'input_number':
            inpt = int(kn.value())
        elif activeViewer and activeViewer.node() == viewer:  # на всякий случаем делаем проверку что активный вьювер тот у которого вызван колбэк
            inpt = activeViewer.activeInput()
        else:
            inpt = None
        # проверяем что удалось получить номер инпута у которого нужно посмотреть ноду
        # и что он не отрицательный, при загрузке нюка input_number отрабатывает с отрицательным значением
        if inpt != None and inpt >= 0:
            viewingNode = viewer.input(inpt)
            if viewingNode:
                x = viewingNode.xpos()
                y = viewingNode.ypos()
                userconfig = userconfigHelper.parse_userconfig()
                x_offset = userconfig["VIEWER OFFSET"]['x_offset']
                y_offset = userconfig["VIEWER OFFSET"]['y_offset']
                viewer.setXYpos(x + int(x_offset), y + int(y_offset))


KNOB_CHANGED_CALLBACK = viewer_beside


def start(action):
    if action.isChecked():
        nuke.addKnobChanged(KNOB_CHANGED_CALLBACK, nodeClass='Viewer')
    else:
        nuke.removeKnobChanged(KNOB_CHANGED_CALLBACK, nodeClass='Viewer')
