import nuke
import re

from vp_little_helpers import qtHelper


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
                    raise


def start():
    if qtHelper.check_action_is_checked(config_key="use_compare_versions_before_render"):
        nuke.addBeforeRender(check_knob_file_version_matches_script_version, nodeClass='Write')
    else:
        nuke.removeBeforeRender(check_knob_file_version_matches_script_version, nodeClass='Write')
