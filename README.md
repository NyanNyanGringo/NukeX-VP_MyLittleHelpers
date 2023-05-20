# LITTLE HELPERS FOR NUKEX:

[YouTube](https://www.youtube.com/)  
[Nukepedia](http://www.nukepedia.com/)  
[LinkedIn](https://www.linkedin.com/in/vladislav-parfentev-7b89b9233/)  

Set of helpers, plugins, and tools for NukeX that will help simplify the life of a compositing artist!

# Helpers

### smart autosave:
- adds a TCL command to Preferences -> Autosave that creates autosaves of the project script in a folder next to the script.

### read write coloriser:
- allows coloring Read and Write nodes based on the file extensions.

### compare versions before render:
- checking the match between the Write node version and the project version before rendering.

### delete temp files after render:
- checks if there are any .tmp files in the sequence folder and deletes them after rendering.

### disconnect viewers inputs after script load:
- disconnects all Inputs for all Viewers after script loading.

### default viewer state is input:
- change default Viewer state from Global to Input.

### config editor:
- helps to open any config files or folders from inside Nuke (relatively to .nuke folder).
- have functionality to restart Nuke.

# Install

### first install:
1) Move "VP_LittleHelpers" folder to "/.nuke/VP_LittleHelpers"
2) To file "/.nuke/init.py" add next code:
> import nuke  
> nuke.pluginAddPath("./VP_LittleHelpers")

### how to update:
1) Copy config files* from "/.nuke/VP_LittleHelpers"
2) Move !new! "VP_LittleHelpers" folder to "/.nuke/VP_LittleHelpers"
3) Paste config files* to "/.nuke/VP_LittleHelpers"

*USERCONFIG.ini and config.json

# USERCONFIG.ini
- Edit USERCONFIG.ini file to change VP_LittleHelpers settings

# P.S.
- If you have any ideas for new helpers - let me know!
- Enjoy!