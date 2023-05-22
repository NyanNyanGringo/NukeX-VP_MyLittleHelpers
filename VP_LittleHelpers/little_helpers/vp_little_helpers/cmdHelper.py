import nuke
import subprocess
import platform


def run_cmd_command(command):
    # TODO: return result
    operatingSystem = platform.system()

    if operatingSystem == "Windows":
        subprocess.Popen(['start', 'cmd', '/k', command], shell=True)

    elif operatingSystem == "Darwin":
        if nuke.ask("Nuke Restart wasn't tested for MacOs. Continue?"):
            subprocess.Popen(['open', '-a', 'Terminal', '-e', command])

    else:
        if nuke.ask("Nuke Restart wasn't tested for Linux. Continue?"):
            subprocess.Popen(['x-terminal-emulator', '-e', command])
