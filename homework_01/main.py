"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    Функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i**2 for i in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for divisor in range(3, int(num / 2), 2):
        if num % divisor == 0:
            return False
    return True


def filter_numbers(nums, num_type):
    """
    Функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if num_type.upper() == "ODD":
        return [i for i in nums if i % 2 != 0]
    elif num_type.upper() == "EVEN":
        return [i for i in nums if i % 2 == 0]
    elif num_type.upper() == "PRIME":
        return [i for i in nums if is_prime(i)]
    else:
        return []
