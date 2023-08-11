import nuke
from set_roto_frame_range import set_roto_frame_range

nuke.menu("Properties").addCommand('Set Auto FrameRange', set_roto_frame_range)
