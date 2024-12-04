import re

from task_manager import TaskManager


# Проверка на корректность ввода даты
def check_date(date: str, message: str) -> str:
    # Условие выхода из цикла ввод корректной даты
    while True:
        if re.fullmatch(r"20\d\d-[01]\d-[0123]\d", date):
            year = int(date[:4])
            month = int(date[5:7])
            day = int(date[8:])
            if 2000 < year < 2100 and 0 < month < 13:
                if month in [1, 3, 5, 7, 8, 10, 12] and 0 < day < 32:
                    return date
                if month in [4, 6, 9, 11] and 0 < day < 31:
                    return date
                if month == 2:
                    if (year % 4 == 0 and 0 < day < 30) or 0 < day < 29:
                        return date
        print("Повторите ввод даты! ошибка формата!")
        date = input(message)


# Проверка на строку, не состоящую из пробелов или цифр
def check_str(s: str, message: str) -> str:
    while True:
        if s.strip().isdigit():
            print("Ошибка! Строка не может состоять только из цифр")
        elif s == "" or s.isspace():
            print("Ошибка! Строка не может быть пустой!")
        else:
            return s
        s = input(message)


# Проверка на ввод id
def check_ids(s: str, message: str, tm: TaskManager) -> int:
    while True:
        if s.isdigit():
            num = int(s)
            if num in tm.ids_list:
                return num
            print("Ошибка! Вы ввели не число!")
            s = input(message)
