def upload_dir_in_disk(YD_token: str, path_to_file: str):
    import yadisk
    '''Функция загружает файл на Яндекс Диск'''
    try:
        path_to_photo_in_pk = path_to_file
        path_to_photo_in_YD = path_to_photo_in_pk[1:]
        name_file = path_to_file.split('/')[-1]

        with yadisk.YaDisk(token=YD_token) as y:
            y.upload(path_to_photo_in_pk, path_to_photo_in_YD)
            print('Download file:', name_file)
    except yadisk.exceptions.ParentNotFoundError:
        print(f'Папки ({path_to_file}) нет на Яндекс Диске. Создай её "y.mkdir(name_folder)", а потом перезапусти код')
    except yadisk.exceptions.PathExistsError:
        print(f'Такой файл ({path_to_photo_in_pk}) на Диске уже существует')
    except yadisk.exceptions.UnauthorizedError:
        print('Ошибка с авторизацией на Диске. Проблема временная или же токен неправильный')
    except FileNotFoundError:
        print(f'Путь к папке ({path_to_file}) не корректен')
    except PermissionError:
        print(f'В качестве аргумента получен путь к папке ({path_to_photo_in_pk}), а требовался путь к файлу')
    except ModuleNotFoundError:
        print('Библиотека yadisk не установлена. Команда для установки: pip install yadisk')
    except NameError as e:
        print(e.__str__())
