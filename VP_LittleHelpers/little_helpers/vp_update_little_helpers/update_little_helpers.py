import nuke, os

from little_helpers.vp_little_helpers import updateHelper


def ask_error_message(reason: str):
    return nuke.ask(f"""
My Lord,
I can't update VP_LittleHelpers - {reason}

Be sure:
1. You are connected to the internet;
2. Nuke Python and Terminal not blocked by FireWall.

Do you want to update manually?
""")


def start(action, start_when_initialize=False):
    if start_when_initialize:
        try:
            current_version = updateHelper.get_program_version()
            last_version = updateHelper.get_data_from_last_repo_release("tag_name")
            if updateHelper.check_new_version_available(current_version, last_version):
                action.setText(f"Update VP_LittleHelpers from {current_version} to {last_version}")
                nuke.message(f"Available update for VP_LittleHelpers from {current_version} to {last_version}! ^_^")
        except:
            pass
        finally:
            return

    # Проверяем обновления и спрашиваем установить ли
    # Получаем ссылку на последнюю версию
    # Скачиваем
    # Распаковываем
    # Удаляем .zip
    # Заменяем файлы
    # Перезагружаем Nuke
    # Выводим сообщение, что программа обновлена успешно с такой-то на такую-то версию! И
    # выдаем список обновлений

    current_version = updateHelper.get_program_version()
    if not current_version:
        nuke.message(f"I can't find version file in {updateHelper.get_program_path()}!")
        return

    last_version = str()
    try:
        last_version = updateHelper.get_data_from_last_repo_release("tag_name")
    except:
        if ask_error_message("can't check last release version."):
            updateHelper.open_program_on_github()
        return

    download_url = str()
    try:
        download_url = updateHelper.get_data_from_last_repo_release("zipball_url")
    except:
        if ask_error_message("can't get url to download last release."):
            updateHelper.open_program_on_github()
        return

    if updateHelper.check_new_version_available(current_version, last_version):
        if nuke.ask(f"My Lord,\n\nVP_LittleHelpers_{last_version} available!\n\nUpdate?"):
            zip_path = str()
            try:
                zip_path = updateHelper.download_repository_by_url(download_url)
            except:
                if ask_error_message("can't download last release .zip file from GitHub."):
                    updateHelper.open_program_on_github()
                return

            new_program_path = updateHelper.unzip(zip_path, delete_zip=True)
            program_path = updateHelper.get_program_path()

            updateHelper.update_program_files(program_path, new_program_path)



    else:
        nuke.message("My Lord,\n\nYou have the latest version of VP_LittleHelpers ^_^")
        return
