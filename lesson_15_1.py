"""
Задание 1. Логирование с использованием нескольких файлов
Напишите скрипт, который логирует разные типы сообщений в разные файлы.
Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
WARNING и выше — в warnings_errors.log.
"""

import logging
from pathlib import Path

# Получаем путь к директории, где находится запускаемый скрипт
script_directory = Path(__file__).parent.resolve()

# Создаем логгер
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Создаем обработчики для записи в файлы в директории скрипта
debug_info_handler = logging.FileHandler(script_directory / 'debug_info.log')
warnings_errors_handler = logging.FileHandler(script_directory / 'warnings_errors.log')

# Устанавливаем уровни логирования для обработчиков
debug_info_handler.setLevel(logging.DEBUG)
warnings_errors_handler.setLevel(logging.WARNING)

# Создаем форматтер и добавляем его к обработчикам
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

# Пример логирования сообщений
logger.debug('Это сообщение DEBUG')
logger.info('Это сообщение INFO')
logger.warning('Это сообщение WARNING')
logger.error('Это сообщение ERROR')
logger.critical('Это сообщение CRITICAL')
