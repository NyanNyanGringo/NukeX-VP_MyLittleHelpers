import re
import os

import nuke


# returns default script for TimeWarp from toolbars.py
def getDefaultTimeWarpScript():
    toolbars = os.path.dirname(nuke.env['ExecutablePath']) + '/plugins/nukescripts/toolbars.py'
    if os.path.isfile(toolbars):
        with open(toolbars) as file:
            for line in file:
                if line.lstrip().startswith('m.addCommand("TimeWarp", "'):
                    script = line.split('"')[3]
                    if script:
                        return script.replace('\\n', '\n')
    return 'nukescripts.create_time_warp()'


def create_time_warp():
    t = nuke.createNode("TimeWarp")
    a = nuke.value(t.name() + ".first_frame")
    e = nuke.value(t.name() + ".last_frame")
    if float(e) <= float(a):
        a = nuke.value("root.first_frame")
        e = nuke.value("root.last_frame")
    cmd = "{curve L x" + a + " " + a + " x" + e + " " + e + "}"  # {curve L x1 1 x100 100}
    t.knob("lookup").fromScript(cmd)


def setup_time_warp_to_linear():
    timewarp = nuke.thisNode()
    if timewarp["lookup"].isAnimated():
        script = timewarp["lookup"].toScript().replace("curve", "curve L")
        timewarp["lookup"].fromScript(script)


def kronos_linear_animation():
    kn = nuke.thisKnob()
    if kn.name() == 'timingFrame2':
        animation = kn.toScript()
        pattern = r'^\{curve x\d+ \d+(\.\d+)?\}$'
        if re.match(pattern, animation):
            kn.fromScript(animation.replace('curve ', 'curve L '))


TIMEWARP_KNOB_CHANGED_CALLBACK = setup_time_warp_to_linear
KRONOS_KNOB_CHANGED_CALLBACK = kronos_linear_animation


def start(action):
    if action.isChecked():
        spl = os.path.splitext(__file__)[0].replace('\\', '/').split('/')
        create_time_warp_function = '.'.join(
            spl[-3:] + ['create_time_warp()'])  # little_helpers.vp_linear_animation.linear_animation.create_time_warp()
        nuke.menu('Nodes').menu('Time').findItem('TimeWarp').setScript(create_time_warp_function)

        nuke.addKnobChanged(TIMEWARP_KNOB_CHANGED_CALLBACK, nodeClass='TimeWarp')  # for VP Lord of Nodes support

        nuke.addKnobChanged(KRONOS_KNOB_CHANGED_CALLBACK, nodeClass='Kronos')

    else:
        nuke.menu('Nodes').menu('Time').findItem('TimeWarp').setScript(getDefaultTimeWarpScript())

        nuke.removeKnobChanged(TIMEWARP_KNOB_CHANGED_CALLBACK, nodeClass='TimeWarp')  # for VP Lord of Nodes support

        nuke.removeKnobChanged(KRONOS_KNOB_CHANGED_CALLBACK, nodeClass='Kronos')
