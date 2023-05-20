import nuke
from vp_little_helpers import configHelper
import __userconfig_little_helpers__ as userconfig


def rgb_to_hex(r, g, b, zero_to_one_range):
    # zero_to_one_range True - R, G, B in range 1 to 0
    # zero_to_one_range False - R, G, B in range 0 to 255

    if zero_to_one_range:
        mult = 255
    else:
        mult = 1

    r = int(r * mult)
    g = int(g * mult)
    b = int(b * mult)
    hex = int("%02x%02x%02x%02x" %(r,g,b,1),16)

    return hex


def hex_to_rgb(hex):
    # use binar python operators to convert HEX to RGB
    
    hex = int(hex)
    r = (0xFF & hex >> 24) / 255.0
    g = (0xFF & hex >> 16) / 255.0
    b = (0xFF & hex >> 8) / 255.0
    
    return r,g,b


def check_coloriser_is_active():
    if configHelper.check_key("use_coloriser"):
        return configHelper.read_config_key("use_coloriser")
    return False


def set_tile_color_to_node(node):
    if not check_coloriser_is_active():
        return

    file_value = node["file"].value()

    for extension, rgb_color in userconfig.coloriser_colors.items():
        if file_value.endswith(extension):
            hex_color = rgb_to_hex(rgb_color[0], rgb_color[1], rgb_color[2], True)
            node["tile_color"].setValue(hex_color)


def set_all_read_and_write_to_default_tile_color():
    [node["tile_color"].setValue(0) for node in nuke.allNodes() if node.Class() in ["Read", "Write"]]


def set_all_read_and_write_to_custom_tile_color():
    for node in [node for node in nuke.allNodes() if node.Class() in ["Read", "Write"]]:
        set_tile_color_to_node(node)


def set_all_read_and_write_tile_color():
    if check_coloriser_is_active():
        set_all_read_and_write_to_custom_tile_color()
    else:
        set_all_read_and_write_to_default_tile_color()


def colorise_on_node_create():
    node = nuke.thisNode()
    knob = nuke.thisKnob()
    
    if knob.name() == "file":
        set_tile_color_to_node(node)
