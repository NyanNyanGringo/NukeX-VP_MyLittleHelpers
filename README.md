# LITTLE HELPERS FOR NUKEX:

[YouTube](https://www.youtube.com/)  
[Nukepedia](http://www.nukepedia.com/)  
[LinkedIn](https://www.linkedin.com/in/vladislav-parfentev-7b89b9233/)

## Almost invisible helpers for compositing artist!

# <span style="color: #86A8E7;">how to use:

### <span style="color: #9CCB9A;">smart autosave:
- adds a TCL command to Preferences -> Autosave that creates autosaves of the project script in a folder next to the script.

### <span style="color: #9CCB9A;">read write coloriser:
- allows coloring Read and Write nodes based on the file extensions.

### <span style="color: #9CCB9A;">compare versions before render:
- checking the match between the Write node version and the project version before rendering.

### <span style="color: #9CCB9A;">delete temp files after render:
- checks if there are any .tmp files in the sequence folder and deletes them after rendering.

### <span style="color: #9CCB9A;">disconnect viewers inputs after script load:
- disconnects all Inputs for all Viewers after script loading.

### <span style="color: #9CCB9A;">default viewer state is input:
- change default Viewer state from Global to Input.

### <span style="color: #9CCB9A;">config editor:
- helps to open any config files or folders from inside Nuke (relatively to .nuke folder).
- have functionality to restart Nuke.

# <span style="color: #86A8E7;"> how to install

### <span style="color: #9CCB9A;">first install:
1) Move "VP_LittleHelpers" folder to "/.nuke/VP_LittleHelpers"
2) To file "/.nuke/init.py" add next code:
> import nuke  
> nuke.pluginAddPath("./VP_LittleHelpers")

### <span style="color: #9CCB9A;">update manually**:
1) Delete folder "little_helpers" ("/.nuke/VP_LittleHelpers/little_helpers")
2) Move !new! "little_helpers" folder to "/.nuke/VP_LittleHelpers/little_helpers"

**VP_LittleHelpers require auto-update from inside Nuke ^_^

# <span style="color: #86A8E7;"> how to set up:
- Edit USERCONFIG.ini file to change VP_LittleHelpers settings

# <span style="color: #86A8E7;"> P.S.
- If you have any ideas for new helpers - let me know!
- Enjoy!