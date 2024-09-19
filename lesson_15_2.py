"""
Задача 2. Работа с текущим временем и датой
Напишите скрипт, который получает текущее время и дату, а затем выводит их в
формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
недели в году"""

from datetime import datetime

# Получаем текущее время и дату
now = datetime.now()

# Форматируем дату и время в формате YYYY-MM-DD HH:MM:SS
formatted_datetime = now.strftime('%Y-%m-%d %H:%M:%S')

# Получаем день недели
day_of_week = now.strftime('%A')

# Получаем номер недели в году
week_number = now.isocalendar()[1]

# Выводим результаты
print(f"Текущая дата и время: {formatted_datetime}")
print(f"День недели: {day_of_week}")
print(f"Номер недели в году: {week_number}")
