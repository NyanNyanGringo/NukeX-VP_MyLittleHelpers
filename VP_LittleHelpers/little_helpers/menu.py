import os

from little_helpers.vp_little_helpers import qtHelper, userconfigHelper, configHelper


# create config folder if it doesn't exist
config_folder = configHelper.get_config_folder()
if not os.path.exists(config_folder):
    os.mkdir(config_folder)

# work with configs
userconfigHelper.check_userconfig_before_start_nuke()
userconfigHelper.update_userconfig_before_start_nuke()

# add apps
qtHelper.create_and_get_helper_menu().addSeparator()
import little_helpers.vp_smart_autosave.menu
import little_helpers.vp_read_write_coloriser.menu
import little_helpers.vp_compare_versions_before_render.menu
import little_helpers.vp_delete_temp_files_after_render.menu
import little_helpers.vp_disconnect_viewers_inputs_after_script_load.menu
import little_helpers.vp_default_viewer_state_is_input.menu
import little_helpers.vp_config_editor.menu
import little_helpers.vp_update_little_helpers.menu
qtHelper.create_and_get_helper_menu().addSeparator()
