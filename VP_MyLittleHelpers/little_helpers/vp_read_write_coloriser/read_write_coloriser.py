import nuke

from little_helpers.vp_little_helpers import userconfigHelper, colorHelpers


def set_tile_color_to_node(node: nuke.Node = None):
    if not node:
        node = nuke.thisNode()

    if node.Class() not in ["Read", "Write"]:
        raise TypeError(f"Node class '{node.Class()}' is not valid. Expected 'Read' or 'Write'.")

    file_value = node["file"].value()
    userconfig = userconfigHelper.parse_userconfig()

    for extension in list(userconfig["READ WRITE COLORS"]):
        color = userconfig["READ WRITE COLORS"][extension]
        r, g, b = [float(val) for val in color.replace(" ", "").split("|")]

        if file_value.endswith(extension):
            hex_color = colorHelpers.rgb_to_hex(r, g, b, True)
            node["tile_color"].setValue(hex_color)


def set_all_read_and_write_to_color(to_default_color: bool = False):
    if to_default_color:
        [node["tile_color"].setValue(0) for node in nuke.allNodes() if node.Class() in ["Read", "Write"]]
    else:
        [set_tile_color_to_node(node) for node in nuke.allNodes() if node.Class() in ["Read", "Write"]]


def colorise_node_on_extension_changed():
    """Executed when changes extension of node"""
    if nuke.thisKnob().name() == "file" and nuke.thisNode().Class() in ["Read", "Write"]:
        set_tile_color_to_node(nuke.thisNode())


ON_CREATE_CALLBACK = set_tile_color_to_node
ON_KNOB_CHANGED_CALLBACK = colorise_node_on_extension_changed


def start(action):
    if action.isChecked():
        set_all_read_and_write_to_color(to_default_color=False)

        nuke.addOnCreate(ON_CREATE_CALLBACK, nodeClass='Read')
        nuke.addOnCreate(ON_CREATE_CALLBACK, nodeClass='Write')

        nuke.addKnobChanged(ON_KNOB_CHANGED_CALLBACK, nodeClass='Read')
        nuke.addKnobChanged(ON_KNOB_CHANGED_CALLBACK, nodeClass='Write')

    else:
        set_all_read_and_write_to_color(to_default_color=True)

        nuke.removeOnCreate(ON_CREATE_CALLBACK, nodeClass='Read')
        nuke.removeOnCreate(ON_CREATE_CALLBACK, nodeClass='Write')

        nuke.removeKnobChanged(ON_KNOB_CHANGED_CALLBACK, nodeClass='Read')
        nuke.removeKnobChanged(ON_KNOB_CHANGED_CALLBACK, nodeClass='Write')
