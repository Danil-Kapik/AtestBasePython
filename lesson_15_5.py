"""
Задача 5. Запуск из командной строки
Напишите код, который запускается из командной строки и получает на вход путь
до директории на ПК. Соберите информацию о содержимом в виде объектов
namedtuple. Каждый объект хранит: имя файла без расширения или название
каталога, расширение, если это файл, флаг каталога, название родительского
каталога. В процессе сбора сохраните данные в текстовый файл используя
логирование.
"""

import sys
import logging
from collections import namedtuple
from pathlib import Path

if len(sys.argv) < 2:
    print('Укажите путь до директории')
    sys.exit(1)
directory_path = Path(sys.argv[1])

# Описание структуры для хранения информации о файлах и директориях
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent'])

# Сбор информации о содержимом директории
def collect_directory_info(directory_path):
    directory_info = []
    for item in directory_path.iterdir():
        if item.is_dir():
            directory_info.append(FileInfo(item.name, None, True, item.parent))
        else:
            directory_info.append(FileInfo(item.name, item.suffix, False, item.parent))
    return directory_info

# Настройка логгера
logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(message)s')

def log_directory_info(contents):
    for item in contents:
        logging.info(f'Name: {item.name}, Extension: {item.extension}, Is Directory: {item.is_dir}, Parent: {item.parent}')

# Пример использования
if __name__ == "__main__":
    contents = collect_directory_info(directory_path)
    log_directory_info(contents)
