"""
Блок 2. Домашнее задание (TeachMeSkills.by)

Задания:
1. Преобразовать список чисел в список строк с помощью map()
2. Отфильтровать только положительные числа с помощью filter()
3. Отфильтровать палиндромы из списка строк с помощью filter()
4. Реализовать декоратор времени выполнения функции
5. С помощью map() и reduce() посчитать площадь всех комнат
"""

from functools import reduce
import time
from typing import List, Dict, Callable, Any


def task_1(numbers: list[int]) -> list[str]:
    """
    Преобразовать список чисел в список строк.

    :param numbers: список целых чисел
    :return: список строковых представлений чисел
    """
    # TODO: Использовать map() для преобразования каждого числа в строку
    return list(map(str, numbers))  



def task_2(numbers: list[int]) -> list[int]:
    """
    Вернуть только положительные числа из списка.

    :param numbers: список целых чисел
    :return: новый список только с положительными числами (> 0)
    """
    # TODO: Использовать filter() для отбора положительных значений
    return list(filter(lambda x: x > 0, numbers))
    



def task_3(words: list[str]) -> list[str]:
    """
    Вернуть только палиндромы из списка слов.

    :param words: список строк
    :return: список строк-палиндромов
    """
    # TODO: Использовать filter() и условие word == word[::-1]
    palindromes = list(filter(lambda word: word == word[::-1], words))
    return palindromes
print(task_3(['abcba', 'level', 'test', '12321', 'python']))

import time 
from typing import Callable, Any
def timing_decorator(func: Callable) -> Callable:
    """
    Декоратор, измеряющий время выполнения функции.

    :param func: функция, которую нужно обернуть
    :return: обёрнутая функция
    """
    # TODO: Использовать time.time() до и после вызова функции
    def wrapper(*args, **kwargs) -> any:
        # Подсказка: start = time.time()
        #            result = func(...)
        #            end = time.time()
        #            print(f"Execution time: {end - start:.4f} seconds")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print (f" Execution time: {end - start:.4f} seconds")
        return result
    return wrapper
@timing_decorator
def test_funs():
    for _ in range(1000000):
        pass

test_funs()


@timing_decorator
def task_4(n: int = 100_000) -> int:
    """
    Пример функции для замера времени — суммирование чисел от 0 до n.

    :param n: верхняя граница диапазона (не включительно)
    :return: сумма чисел от 0 до n-1
    """
    total = 0
    for i in range(n):
        total += i
    return total
print("Сумма:", task_4())

from functools import reduce
def task_5(rooms: list[dict[str, float]]) -> float:
    """
    Вычислить общую площадь квартиры на основе списка комнат.

    :param rooms: список словарей, каждый с ключами 'length' и 'width'
    :return: общая площадь квартиры
    """
    # TODO: Сначала использовать map(), чтобы получить площади
    # TODO: Затем reduce(), чтобы просуммировать их
    
    areas = map(lambda room: room['length'] * room['width'], rooms)
    total_area = 0.0
    total_area = reduce(lambda a, b: a + b, areas)
    return total_area


test_rooms = [
        {"name": "Kitchen", "length": 6, "width": 4},
        {"name": "Room 1", "length": 5.5, "width": 4.5},
        {"name": "Room 2", "length": 5, "width": 4},
        {"name": "Room 3", "length": 7, "width": 6.3},
    ]

print(f"Total area: {task_5(test_rooms):.2f} m**2")

# ==== Тесты для проверки решений ====
if __name__ == "__main__":
    print("=== Запуск тестов ===")

    assert task_1([1, 2, 3]) == ['1', '2', '3']
    assert task_1([]) == []

    assert task_2([-2, 0, 1, 4, -5, 7]) == [1, 4, 7]
    assert task_2([]) == []

    assert task_3(['abcba', 'level', 'test', '12321', 'python']) == ['abcba', 'level', '12321']
    assert task_3(['abc', 'def']) == []

    task_4()  # просто вызывается, выводит время

    test_rooms = [
        {"name": "Kitchen", "length": 6, "width": 4},
        {"name": "Room 1", "length": 5.5, "width": 4.5},
        {"name": "Room 2", "length": 5, "width": 4},
        {"name": "Room 3", "length": 7, "width": 6.3},
    ]
    expected_area = 6 * 4 + 5.5 * 4.5 + 5 * 4 + 7 * 6.3
    assert round(task_5(test_rooms), 2) == round(expected_area, 2)

    print("✅ Все тесты прошли!")