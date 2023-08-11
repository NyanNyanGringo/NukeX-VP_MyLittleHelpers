import nuke


def get_selected_node():
    try:
        return nuke.selectedNode()
    except ValueError:  # no node selected
        pass


def set_roto_frame_range():
    selected_node = get_selected_node()

    if selected_node is None:
        nuke.message('My Lord, select one Roto/RotoPaint node.')
        return

    if selected_node.Class() in ["Roto", "RotoPaint"]:

        for selShape in selected_node['curves'].getSelected():
            key_frames = [int(i) for i in selShape[0].center.getControlPointKeyTimes()]

            selected_node['lifetime_type'].setValue(4)  # set life as 'frame_range'
            selected_node['lifetime_start'].setValue(min(key_frames))  # set 'from' range
            selected_node['lifetime_end'].setValue(max(key_frames))  # set 'to' range
