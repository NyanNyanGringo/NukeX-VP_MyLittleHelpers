import nuke


def set_smart_autosave():
    nuke.message("1")


def remove_smart_autosave():
    nuke.message("0")


"""
[
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
]
"""
