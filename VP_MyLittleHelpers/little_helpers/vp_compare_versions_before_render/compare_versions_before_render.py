import nuke
import re


def check_knob_file_version_matches_script_version():
    write = nuke.thisNode()

    def get_version(text):
        versions = re.findall(r"_v[0-9]+", text)
        if versions:
            return versions[-1]
        return None

    def get_int_from_ver(version):
        return int(version.replace("_v", ""))

    script_name = nuke.root()["name"].value()

    if script_name:
        script_version = get_version(script_name)
        file_version = get_version(write["file"].value())

        if script_version and file_version:
            if not get_int_from_ver(script_version) == get_int_from_ver(file_version):
                if not nuke.ask("Version of project and version of write node doens't mathces! Continue?"):
                    raise RuntimeError("Version of project and version of write node do not match.")


BEFORE_RENDER_CALLBACK = check_knob_file_version_matches_script_version


def start(action):
    if action.isChecked():
        nuke.addBeforeRender(BEFORE_RENDER_CALLBACK, nodeClass='Write')
    else:
        nuke.removeBeforeRender(BEFORE_RENDER_CALLBACK, nodeClass='Write')
