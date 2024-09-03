# My Little Helpers for NukeX
[Nukepedia](http://www.nukepedia.com/python/nodegraph/vp-my-little-helpers)  
[YouTube](https://www.youtube.com/@parfprod1/videos)  
[LinkedIn](https://www.linkedin.com/in/vladislav-parfentev-7b89b9233/)

## <p align="center"><b>Almost invisible helpers for Compositing artist!</b> </p>

<p align="center"><img src="https://parfprod.com/URLS/little_helpers/my_little_helpers_logo_v001.jpeg" width="525"></p>

# instruments:

### [smart autosave](https://parfprod.com/URLS/little_helpers/smart_autosave_v001.gif)

- adds a TCL command to Preferences -> Autosave.
- creates autosaves of the project script in a folder next to the script.

### [default viewer state is input](https://parfprod.com/URLS/little_helpers/default_is_input_v001.png)

- changes default Viewer state from Global to Input.

### [read write colorizer](https://parfprod.com/URLS/little_helpers/read_write_colorizer_v001.gif)

- allows coloring Read and Write nodes based on the file extensions.
- you can modify extensions using `./config/USERCONFIG.ini`
- developed with Igor Baydak.

### [compare versions before render](https://parfprod.com/URLS/little_helpers/check_ver_before_render_v001.gif)

- checks the match between the Write node version and the project version before rendering.

### [disconnect viewers inputs after script load](https://parfprod.com/URLS/little_helpers/disconnect_viewer_inputs_v001.gif)

- disconnects all Inputs for all Viewers after script loading.

### [delete temp files after render](https://parfprod.com/URLS/little_helpers/delete_temp_files_v001.gif)

- checks if there are any .tmp files in the sequence folder after rendering and deletes them.

### [config editor](https://parfprod.com/URLS/little_helpers/config_helper_v001.gif)

- opens .nuke folder.
- helps to open any config files or folders from inside Nuke (relatively to .nuke folder).
- have functionality to restart Nuke (support restarting with open project).
- you can modify config files or folders using `./config/USERCONFIG.ini`

### viewer beside (update from 2 July 2024)

- place viewer beside selected and views node
- you can modify Viewer position using `./config/USERCONFIG.ini`

### linear animation (update from 2 July 2024)

- as default for Kronos and TimeWarp nodes

### show shortcuts in Tab menu (update from 3 September 2024)

### version up reminder (update from 3 September 2024)

- every time script loads - reminds to do version up



# first install:

1) Move "VP_MyLittleHelpers" folder to "/.nuke/VP_MyLittleHelpers"
2) To file "/.nuke/init.py" add next code:

> import nuke  
> nuke.pluginAddPath("./VP_MyLittleHelpers")

# update (manual):

1) Delete folder "little_helpers" ("/.nuke/VP_MyLittleHelpers/little_helpers")
2) Move !new! "little_helpers" folder to "/.nuke/VP_MyLittleHelpers/little_helpers"

# settings:

- Edit `./config/USERCONFIG.ini` file to change VP_MyLittleHelpers settings
- To set up custom config path: use environment variable LITTLE_HELPERS_CONFIG_PATH:

> import os  
> os.environ["LITTLE_HELPERS_CONFIG_PATH"] = "/your/custom/path"

# pipeline integration

```python
"""
Example usage of MyLittleHelpers in a studio pipeline.

Create an init.py file inside the VP_MyLittleHelpers folder (near to menu.py file).

Use the following code as a starting point to configure which instruments will be turned on or off.
"""

import os


class InstrumentState:
    # User can choose whether to use the instrument or not
    USER_DEFAULTS = "user_defaults"

    # User can change the state of the instrument with GUI.
    # Instrument will be automatically enabled/disabled when Nuke starts up.
    ENABLE_AT_STARTUP = "enable_at_startup"
    DISABLE_AT_STARTUP = "disable_at_startup"

    # User cannot change the state of the instrument with GUI (action will be disabled).
    # Instrument will be automatically enabled/disabled when Nuke starts up.
    ALWAYS_ENABLED = "always_enabled"
    ALWAYS_DISABLED = "always_disabled"


# If necessary - set the path to the configuration file for Little Helpers
# os.environ["LITTLE_HELPERS_CONFIG_PATH"] = "/your/studio/config/path"


# Set the initial state for each instrument
os.environ["LITTLE_HELPERS_SMART_AUTOSAVE"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_DEFAULT_VIEWER_STATE_IS_INPUT"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_READ_WRITE_COLORIZER"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_COMPARE_VERSIONS_BEFORE_RENDER"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_DISCONNECT_VIEWERS_INPUTS_WHEN_SCRIPT_LOAD"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_DELETE_TEMP_FILES_AFTER_RENDER"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_CONFIG_EDITOR"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_VIEWER_BESIDE"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_LINEAR_ANIMATION"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_SHOW_SHORTCUTS_IN_TAB_MENU"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_VERSION_UP_REMINDER"] = InstrumentState.USER_DEFAULTS

```

# p.s.

- If you have any ideas for little helpers - let me know!
- Enjoy!