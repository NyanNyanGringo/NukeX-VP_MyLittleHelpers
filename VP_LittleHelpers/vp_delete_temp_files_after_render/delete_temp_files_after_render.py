import nuke
import os
import re

from vp_little_helpers import qtHelper


def check_knob_file_is_sequence(file):
    if not (file.endswith(".mov") or file.endswith(".mp4")):
        return True
    return False


def delete_temp_files_after_render():
    write = nuke.thisNode()
    file = write["file"].value()

    temp_files = []

    if check_knob_file_is_sequence(file):
        sequence_path = os.path.dirname(file)

        if not os.path.exists(sequence_path):
            return

        for f in os.listdir(sequence_path):
            file_path = os.path.join(sequence_path, f)
            if file_path.endswith(".tmp"):
                os.remove(file_path)
                temp_files.append(f)

        if temp_files:
            nuke.message("\n".join(temp_files) + "\n\nWas deleted, My Lord ^_^")


def set_delete_temp_files_after_render():
    if qtHelper.check_action_is_checked(config_key="use_delete_temp_files_after_render"):
        nuke.addAfterRender(delete_temp_files_after_render, nodeClass='Write')
    else:
        nuke.removeAfterRender(delete_temp_files_after_render, nodeClass='Write')
