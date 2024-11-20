import nuke


def check_before_align() -> bool:
    if not nuke.thisKnob().name() == "inputChange":
        return False

    print("Checked.")

    return True


def align() -> None:
    if not check_before_align():
        return

    print("Aligned.")


DOT_ALIGNER_CALLBACK = align


def start(action):
    if action.isChecked():
        nuke.addKnobChanged(DOT_ALIGNER_CALLBACK)
    else:
        nuke.removeKnobChanged(DOT_ALIGNER_CALLBACK)
