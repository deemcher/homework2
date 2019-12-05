"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_today = date.today()
    date_yesterday = date.today() - timedelta(days=1)
    date_month = date.today() - timedelta(days=30)
    print(date_today)
    print(date_yesterday)
    print(date_month)
    #return date_today, date_yesterday, date_month
    
    
def str_2_datetime():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_string = "01/01/17 12:10:03.234567"
    date_dt = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    print(date_dt)

if __name__ == "__main__":
    print_days()
    str_2_datetime()
