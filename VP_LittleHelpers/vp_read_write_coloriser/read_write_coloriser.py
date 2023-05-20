import nuke
from vp_little_helpers import iniHelper, colorHelpers, qtHelper


def set_tile_color_to_node(node):
    if not qtHelper.check_action_is_checked("use_coloriser"):
        return

    file_value = node["file"].value()
    config = iniHelper.get_ini_config()

    for extension in list(config["READ WRITE COLORS"]):
        color = config["READ WRITE COLORS"][extension]
        r, g, b = [float(val) for val in color.replace(" ", "").split("|")]

        if file_value.endswith(extension):
            hex_color = colorHelpers.rgb_to_hex(r, g, b, True)
            node["tile_color"].setValue(hex_color)


def set_all_read_and_write_to_default_tile_color():
    [node["tile_color"].setValue(0) for node in nuke.allNodes() if node.Class() in ["Read", "Write"]]


def set_all_read_and_write_to_custom_tile_color():
    for node in [node for node in nuke.allNodes() if node.Class() in ["Read", "Write"]]:
        set_tile_color_to_node(node)


def set_all_read_and_write_tile_color():
    if qtHelper.check_action_is_checked("use_coloriser"):
        set_all_read_and_write_to_custom_tile_color()
    else:
        set_all_read_and_write_to_default_tile_color()


def colorise_on_node_create():
    if nuke.thisKnob().name() == "file":
        set_tile_color_to_node(nuke.thisNode())
