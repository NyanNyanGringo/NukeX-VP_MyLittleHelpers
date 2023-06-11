import nuke

from little_helpers.vp_little_helpers import qtHelper, nukeHelpers


def activate_smart_autosave():
    nuke.toNode("preferences")["AutoSaveName"].setValue(
"""[
set temp_dir "[getenv NUKE_TEMP_DIR]/autosaves/";

set root_basename [file dirname [value root.name]];
set root_tail [file rootname [file tail [value root.name]]]_autosaves;
set root_dir $root_basename/$root_tail;

set data [date %Y-%m-%d]_[date %H-%M];

if {[value root.name] == ""} {
    set main_dir $temp_dir;
    } else {
    set main_dir $root_dir;
    }

file mkdir $main_dir;

return $main_dir/$data.autosave
]""")
    nukeHelpers.save_preferences_to_file()


def deactivate_smart_autosave():
    nuke.toNode("preferences")["AutoSaveName"].setValue("[firstof [value root.name] [getenv NUKE_TEMP_DIR]/].autosave")
    nukeHelpers.save_preferences_to_file()


def start():
    if qtHelper.check_action_is_checked(config_key="use_smart_autosave"):
        activate_smart_autosave()
    else:
        deactivate_smart_autosave()
