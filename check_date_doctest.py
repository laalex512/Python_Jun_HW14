# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.


import doctest


def input_date(data: str) -> bool:
    """
    >>> input_date('05.12.1983')
    True
    >>> input_date('01.01.10000')
    False
    >>> input_date('32.01.2000')
    False
    >>> input_date('29.02.2000')
    True
    >>> input_date('29.02.2001')
    False
    >>> input_date('29.02.1984')
    True
    """
    day, month, year = (int(i) for i in data.split("."))
    if 1 <= year <= 9999 and 0 < day <= max_days(month, year):
        return True
    return False


def max_days(month: int, year: int) -> int:
    DICT_MONTHS = {
        30: [4, 6, 9, 11],
        31: [1, 3, 5, 7, 8, 10, 12],
        28: [2]
        }
    for key, value in DICT_MONTHS.items():
        if month in value:
            if key == 28 and is_leap(year):
                return key + 1
            return key
    return 0


def is_leap(year: int) -> bool:
    CHECK_NORMAL = 4
    CHECK_HUNDRED = 100
    CHECK_4HUNDRED = 400
    if year % CHECK_NORMAL == 0 and (year % CHECK_HUNDRED != 0 or year % CHECK_4HUNDRED == 0):
        return True
    return False


if __name__ == '__main__':
    doctest.testmod(verbose=True)
