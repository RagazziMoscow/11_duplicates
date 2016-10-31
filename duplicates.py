import sys
import os
import os.path


# Возвращает список всех файлов в заданной папке
def get_all_files_list(path=''):
    start_path = os.getcwd()
    files_list = []
    for item in os.walk(path):
        os.chdir(item[0])
        for file in os.listdir():
            if(os.path.isfile(file)):
                files_list.append({"name": file, "size": os.path.getsize(file)})
        os.chdir(start_path)
    return files_list


# Возвращает список дупликатов файлов
def get_duplicate_files_list(files_list):
    duplicates_list = []
    for file in files_list:
        if(files_list.count(file) > 1):
            # Если ещё не добавляли файл в список дупликатов
            if(duplicates_list.count(file) == 0):
                duplicates_list.append(file)
    return duplicates_list


def main():
    # Если запуск произошёл с параметром
    if(len(sys.argv) > 1):
        all_files_list = get_all_files_list(sys.argv[1])
    else:
        all_files_list = get_all_files_list()

    discovered_duplicates = get_duplicate_files_list(all_files_list)
    if(discovered_duplicates):
        print("Обнаруженные дубликаты файлов:")
        for file in discovered_duplicates:
            print(file["name"])
    else:
        print("Дупликатов не обнаружено")


if __name__ == '__main__':
    main()

