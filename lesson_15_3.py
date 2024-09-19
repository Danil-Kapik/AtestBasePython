"""
Задача 3. Планирование задач
Напишите функцию, которая принимает количество дней от текущей даты и
возвращает дату, которая наступит через указанное количество дней. Дополнительно,
выведите эту дату в формате YYYY-MM-DD.
"""

from datetime import datetime, timedelta

def get_future_date(num_days):
    future_date = datetime.now() + timedelta(days=num_days)
    return future_date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    num_days = int(input("Enter the number of days: "))
    future_date = get_future_date(num_days)
    print(f"The future date is: {future_date}")