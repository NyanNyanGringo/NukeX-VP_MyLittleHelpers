# My Little Helpers for NukeX

[Nukepedia](http://www.nukepedia.com/)  
[YouTube](https://www.youtube.com/@parfprod1/videos)  
[LinkedIn](https://www.linkedin.com/in/vladislav-parfentev-7b89b9233/)

## <p align="center"><b>Almost invisible helpers for Compositing artist!</b> </p>

<p align="center"><img src="https://parfprod.com/URLS/little_helpers/my_little_helpers_logo_v001.jpeg" width="525"></p>

# how to use:

### [smart autosave](https://parfprod.com/URLS/little_helpers/smart_autosave_v003.gif)

- adds a TCL command to Preferences -> Autosave.
- creates autosaves of the project script in a folder next to the script.

### [read write colorizer](https://parfprod.com/URLS/little_helpers/read_write_colorizer_v001.gif)

- allows coloring Read and Write nodes based on the file extensions.
- you can modify extensions using `./config/USERCONFIG.ini`

### [compare versions before render](https://parfprod.com/URLS/little_helpers/check_ver_before_render_v001.gif)

- checks the match between the Write node version and the project version before rendering.

### [delete temp files after render](https://parfprod.com/URLS/little_helpers/delete_temp_files_v001.gif)

- checks if there are any .tmp files in the sequence folder after rendering and deletes them.

### [disconnect viewers inputs after script load](https://parfprod.com/URLS/little_helpers/disconnect_viewer_inputs_v001.gif)

- disconnects all Inputs for all Viewers after script loading.

### [default viewer state is input](https://parfprod.com/URLS/little_helpers/default_is_input_v001.png)

- change default Viewer state from Global to Input.


### [config editor](https://parfprod.com/URLS/little_helpers/config_helper_v001.gif)

- opens .nuke folder.
- helps to open any config files or folders from inside Nuke (relatively to .nuke folder).
- have functionality to restart Nuke (support restarting with open project).
- you can modify extensions using `./config/USERCONFIG.ini`

# first install:

1) Move "VP_LittleHelpers" folder to "/.nuke/VP_LittleHelpers"*
2) To file "/.nuke/init.py" add next code:

> import nuke  
> nuke.pluginAddPath("./VP_LittleHelpers")

*Do not rename "VP_LittleHelpers" (else auto-update won't work correct)!

# update (manual):
1) Delete folder "little_helpers" ("/.nuke/VP_LittleHelpers/little_helpers")
2) Move !new! "little_helpers" folder to "/.nuke/VP_LittleHelpers/little_helpers"

#  how to set up:
- Edit USERCONFIG.ini file to change VP_LittleHelpers settings

#  P.S.
- If you have any ideas for new helpers - let me know!
- Enjoy!
