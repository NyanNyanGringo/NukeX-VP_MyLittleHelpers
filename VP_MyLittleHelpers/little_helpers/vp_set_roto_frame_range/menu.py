import nuke
from little_helpers.vp_set_roto_frame_range.set_roto_frame_range import set_roto_frame_range

nuke.menu("Properties").addCommand('Set Auto FrameRange', set_roto_frame_range)
