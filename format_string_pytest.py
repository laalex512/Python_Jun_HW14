# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# целое положительное число
# вещественное положительное или отрицательное число
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# строку в верхнем регистре в остальных случаях

import pytest


def format_string(input_data):
    if input_data.isdigit():
        result = int(input_data)
    elif (input_data.count(".") == 1 or (input_data.count("-") == 1 and input_data.startswith("-"))) and \
            (input_data.replace("-", "").replace(".", "").isdigit()):
        result = float(input_data)
    elif not input_data.islower():
        result = input_data.lower()
    else:
        result = input_data.upper()
    return result


def test_int():
    assert format_string('524') == 524


def test_float():
    assert format_string('-5.35') == -5.35


def test_upper():
    assert format_string('fDh550') == 'fdh550'


def test_other():
    assert format_string('hello') == 'HELLO'


if __name__ == '__main__':
    pytest.main()
