import nuke
import subprocess


def run_terminal_command(command):
    if nuke.env["WIN32"]:
        if " & exit" not in command:
            command += " & exit"
        subprocess.Popen(['start', 'cmd', '/k', command], shell=True)

    elif nuke.env["MACOS"]:
        # applescript_code += f"""&& osascript -e 'tell application "Terminal" to close first window'""" it is for save
        applescript_code = f'osascript -e \'tell application "Terminal" to do script "{command}"\''
        subprocess.Popen(applescript_code, shell=True)

    else:
        if nuke.ask("Nuke Run Terminal wasn't tested for Linux. Continue?"):
            subprocess.Popen(['x-terminal-emulator', '-e', command])
