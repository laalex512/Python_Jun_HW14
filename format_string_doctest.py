# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# целое положительное число
# вещественное положительное или отрицательное число
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# строку в верхнем регистре в остальных случаях

import doctest


def format_string(input_data):
    """
    >>> format_string('524')
    524
    >>> format_string('-5.35')
    -5.35
    >>> format_string('fDh550')
    fdh550
    >>> format_string('hello')
    HELLO
    """
    if input_data.isdigit():
        result = int(input_data)
    elif (input_data.count(".") == 1 or (input_data.count("-") == 1 and input_data.startswith("-"))) and \
            (input_data.replace("-", "").replace(".", "").isdigit()):
        result = float(input_data)
    elif not input_data.islower():
        result = input_data.lower()
    else:
        result = input_data.upper()
    print(result)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
