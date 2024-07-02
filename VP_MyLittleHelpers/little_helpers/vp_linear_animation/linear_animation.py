import nuke
import re, os
from little_helpers.vp_little_helpers import qtHelper


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
    cmd = "{curve L x" + a + " " + a + " x" + e + " " + e + "}"
    t.knob("lookup").fromScript(cmd)


def kronos_linear_animation():
    kn = nuke.thisKnob()
    if kn.name() == 'timingFrame2':
        animation = kn.toScript()
        pattern = r'^\{curve x\d+ \d+(\.\d+)?\}$'
        if re.match(pattern, animation):
            kn.fromScript(animation.replace('curve ', 'curve L '))


def start():
    if qtHelper.check_action_is_checked(config_key="use_linear_animation"):
        spl = os.path.splitext(__file__)[0].replace('\\', '/').split('/')
        create_time_warp_function = '.'.join(
            spl[-3:] + ['create_time_warp()'])  # little_helpers.vp_linear_animation.linear_animation.create_time_warp()
        nuke.menu('Nodes').menu('Time').findItem('TimeWarp').setScript(create_time_warp_function)
        nuke.addKnobChanged(kronos_linear_animation, nodeClass='Kronos')
    else:
        nuke.menu('Nodes').menu('Time').findItem('TimeWarp').setScript(getDefaultTimeWarpScript())
        nuke.removeKnobChanged(kronos_linear_animation, nodeClass='Kronos')
