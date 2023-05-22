import shutil
import subprocess
import webbrowser
import tempfile
import time
import zipfile

import nuke
import os
import re

from little_helpers.vp_little_helpers import cmdHelper, osHelpers


def get_nuke_python_path():
    return os.path.join(os.path.dirname(nuke.rawArgs[0]), "python.exe").replace("\\", "/")


def get_program_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_program_version():
    for file_name in os.listdir(get_program_path()):
        if re.fullmatch(r"v\d+.\d+.\d+", file_name):
            return file_name


def get_repository_name():
    # TODO: change repo name!
    return "NukeX-VP_HotkeyManager"


def get_data_from_last_repo_release(data: str, repository: str = get_repository_name()):
    """
    :param data: "zipball_url" -> get URL to download last release (str: "https://api.github.com/...")
                 "tag_name" -> get last release version (str: "v0.0.0")
                 "body" -> get info about updates - what was done in this release (str)
    :param repository: repository to search release
    """
    python_path = get_nuke_python_path()
    python_code = f'''
import urllib.request
import json

url = "https://api.github.com/repos/NyanNyanGringo/{repository}/releases/latest"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
zipball_url = data["{data}"]

print(zipball_url)
    '''

    result = subprocess.run([python_path, '-c', python_code], capture_output=True, text=True)
    result = result.stdout.strip()

    if not result:
        raise Exception("Something went wrong while getting data...")
    return result


def unzip(zip_file_path: str, delete_zip: int = False):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(os.path.dirname(zip_file_path))

    if delete_zip:
        os.remove(zip_file_path)

    return zip_file_path.replace(".zip", "")


def download_repository_by_url(url) -> str:
    # TODO: change download folder
    temppath = tempfile.gettempdir()
    repository_user = url.replace("\\", "/").split("/")[-4]
    repository_name = url.replace("\\", "/").split("/")[-3]
    repository_version = url.replace("\\", "/").split("/")[-1]

    # delete previous temp files if exists
    for file in os.listdir(temppath):
        items = [repository_user, repository_name, repository_version]
        if all([(item in file) for item in items]):
            file_path = os.path.join(temppath, file).replace("\\", "/")
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)

    # download
    command = f"cd {osHelpers.correct_path_to_console_path(temppath)} & curl -LJO -k {url} & exit"
    cmdHelper.run_cmd_command(command)

    # find files after download
    for x in range(22):
        time.sleep(1)
        for file in os.listdir(temppath):
            items = [repository_user, repository_name, repository_version]
            if all([(item in file) for item in items]):
                return os.path.join(temppath, file).replace("\\", "/")

    raise Exception(f"Something went wrong while downloading file by {url}!")


def check_new_version_available(current_version, last_version) -> tuple:
    current_parts = current_version[1:].split('.')
    last_parts = last_version[1:].split('.')

    for current, last in zip(current_parts, last_parts):
        if int(current) < int(last):
            return True, current_version, last_version
        elif int(current) > int(last):
            return False, None, None

    return False, None, None  # Both versions are equal


def open_program_on_github(repository: str = get_repository_name()):
    webbrowser.open(f"https://github.com/NyanNyanGringo/{repository}")


def update_program_files(old_program_path, new_program_path):
    print(old_program_path)
    print(new_program_path)

# https://api.github.com/repos/NyanNyanGringo/NukeX-VP_HotkeyManager/zipball/v1.4.0
# NyanNyanGringo-NukeX-VP_HotkeyManager-v1.4.0-0-gc4f1c46
