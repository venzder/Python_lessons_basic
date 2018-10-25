# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil
#
# i = 1
# while i <= 9:
#     str_1 = "dir_{}".format(i)
#     dir_path = os.path.join(os.getcwd(), str_1)
#     try:
#         os.mkdir(dir_path)
#         print(f"Дирректория {str_1} успешно создана")
#     except FileExistsError:
#         print("Такая директория уже существует")
#     i += 1
#
# i = 1
# while i <= 9:
#     str_del = "dir_{}".format(i)
#     dir_path = os.path.join(os.getcwd(), str_del)
#     try:
#         os.rmdir(dir_path)
#         print(f"Дирректория {str_del} успешно удалена")
#     except FileNotFoundError:
#         print("Дирректория уже удалена или не существует")
#     i += 1

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# dir_path = os.path.join(os.getcwd())
# list_dir = [i for i in os.listdir(dir_path) if os.path.isdir(i)]
# print(list_dir)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# dir_path = os.path.join(__file__)
# path_copy = os.path.join(os.getcwd(), "newfile.py")
# shutil.copy2(dir_path, path_copy)

def change_dir(direct):
    try:
        path = os.path.join(os.getcwd(), direct)
        os.chdir(path)
        print("Успешно перешел")
    except FileNotFoundError:
        print("Дирректория не найдена")

def list_dir():
    path_dir = os.path.join(os.getcwd())
    list_direct = os.listdir(path_dir)
    print(list_direct)

def del_dir(direct):
    dir_path = os.path.join(os.getcwd(), direct)
    try:
        os.rmdir(dir_path)
        print(f"Дирректория {direct} успешно удалена")
    except FileNotFoundError:
        print("Дирректория уже удалена или не существует")

def add_dir(direct):
    dir_path = os.path.join(os.getcwd(), direct)
    try:
        os.mkdir(dir_path)
        print(f"Дирректория {direct} успешно создана")
    except FileExistsError:
        print("Такая директория уже существует")


if __name__ == "__main__":
    main()
