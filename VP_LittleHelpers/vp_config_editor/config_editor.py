import nuke
import subprocess
import platform
import os

from vp_little_helpers.osHelpers import correct_path_to_console_path


def open_nuke_in_new_terminal(script_path=None):
    """
    Opens NukeX or NukeStudio in new terminal
    :param script_path: string, path to script for open
    :return: None
    """

    operatingSystem = platform.system()
    nuke_path = ((nuke.rawArgs)[0])
    start_mode = (nuke.rawArgs)[1]

    command = ""

    # change disk if Windows
    if script_path and operatingSystem == "Windows":
        command += script_path.replace("\\", "/").split("/")[0] + " & "

    # change dir to script dir
    if script_path:
        command += "cd " + correct_path_to_console_path(os.path.dirname(script_path)) + " & "
    
    # run nuke in sertain mode
    command += correct_path_to_console_path(nuke_path) + " " + start_mode

    # open script
    if script_path:
        command += " " + os.path.basename(script_path)

    # add command to close cmd after close nuke
    command += " " + "& exit"

    # nuke.message(command)
    
    if operatingSystem == "Windows":
        subprocess.Popen(['start', 'cmd', '/k', command], shell=True)
        
    elif operatingSystem == "Darwin":
        if nuke.ask("Nuke Restart wasn't tested for MacOs. Continue?"):
            subprocess.Popen(['open', '-a', 'Terminal', '-e', command])
    
    else:
        if nuke.ask("Nuke Restart wasn't tested for Linux. Continue?"):
            subprocess.Popen(['x-terminal-emulator', '-e', command])


def restart_any_nuke():
    """
    Restart NukeX or NukeStudio (support script reopening)
    :return: None
    """
    script_path = nuke.Root().name()
    
    if script_path == "Root" and nuke.ask("My Lord, script isn't saved!\n\nRestart anyway?"):
        open_nuke_in_new_terminal()
        nuke.scriptExit()
        
    elif not script_path == "Root" and nuke.ask("My Lord,\n\nRestarn Nuke?"):
        open_nuke_in_new_terminal(script_path=script_path)
        nuke.scriptSave(nuke.Root().name()) 
        nuke.scriptExit()
