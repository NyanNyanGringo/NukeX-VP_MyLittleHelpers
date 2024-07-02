# My Little Helpers for NukeX
[Nukepedia](http://www.nukepedia.com/python/nodegraph/vp-my-little-helpers)  
[YouTube](https://www.youtube.com/@parfprod1/videos)  
[LinkedIn](https://www.linkedin.com/in/vladislav-parfentev-7b89b9233/)

## <p align="center"><b>Almost invisible helpers for Compositing artist!</b> </p>

<p align="center"><img src="https://parfprod.com/URLS/little_helpers/my_little_helpers_logo_v001.jpeg" width="525"></p>

# how to use:

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

### viewer beside (update from 2024-07-02)

- place viewer beside selected and views node
- you can modify Viewer position using `./config/USERCONFIG.ini`

### linear animation (update from 2024-07-02)

- as default for Kronos and TimeWarp nodes

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

# p.s.

- If you have any ideas for little helpers - let me know!
- Enjoy!