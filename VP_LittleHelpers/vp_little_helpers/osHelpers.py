import nuke


def add_arrow_before_spaces(string):

    result = ""

    for x in range(len(string)):
        if (x < len(string)-1) and (string[x+1] == " "):
            result += string[x] + "^"
        else:
            result += string[x]
            
    return result


def correct_path_to_console_path(input_path: str) -> str:
    path_corrected = str()
    for path_part in input_path.replace("\\", r'/').split("/"):
        if " " in path_part:
            path_corrected += f'"{path_part}"/'
            continue
        path_corrected += f'{path_part}/'

    if path_corrected[-1] == "/":
        path_corrected = path_corrected[:-1]

    return path_corrected


def check_file_path_is_sequence(file):
    if not (file.endswith(".mov") or file.endswith(".mp4")):
        return True
    return False

