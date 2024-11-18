def upload_dir_in_disk(YD_token: str, path_to_folder: str):
    '''Функция загружает папку с файлами на Яндекс Диск'''
    try:
        list_dir = os.listdir(path_to_folder)
        if len(list_dir) != 0:
            for name_file in list_dir:
                path_to_photo_in_pk = f'{path_to_folder}{name_file}'
                path_to_photo_in_YD = path_to_photo_in_pk[1:]

                with yadisk.YaDisk(token=YD_token) as y:
                    y.upload(path_to_photo_in_pk, path_to_photo_in_YD)
                    print('Download file:', name_file)
        else:
            print('В папке нет файлов. Загружать на Диск нечего')
    except yadisk.exceptions.ParentNotFoundError:
        print(f'Папки {path_to_folder} нет на Яндекс Диске. Создай её "y.mkdir(name_folder)", а потом перезапусти код')
    except yadisk.exceptions.PathExistsError:
        print(f'Такой файл ({path_to_photo_in_pk}) на Диске уже существует')
    except yadisk.exceptions.UnauthorizedError:
        print('Ошибка с авторизацией на Диске. Проблема временная или же токен неправильный')
    except FileNotFoundError:
        print(f'Путь к папке ({path_to_folder}) не корректен')
    except PermissionError:
        print(f'Найдена папа ({path_to_photo_in_pk}). С ней мы ничего делать не будем')