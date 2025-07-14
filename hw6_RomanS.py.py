# TeachMeSkills.by - Блок 2: Домашнее задание (упрощённая версия)
# Выполни задачи ниже, каждая проверяется с помощью assert

from typing import List, Tuple
import random

# 1. Рекурсивный бинарный поиск
# Вход: отсортированный список и целевое число
# Выход: индекс элемента или -1, если не найден

def binary_search_recursive(arr: List[int], target: int, left=0, right=None) -> int:
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1  # элемент не найден

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
print(binary_search_recursive([1, 3, 5, 7, 9], 7))  #  3
assert binary_search_recursive([1, 3, 5, 7, 9], 7) == 3

print(binary_search_recursive([1, 3, 5, 7, 9], 4))  # -1
assert binary_search_recursive([1, 3, 5, 7, 9], 4) == -1


# 2. Перевод десятичного в двоичную систему (итеративно)
def decimal_to_binary(n: int) -> str:
  if n == 0:
      return "0"
  result = ""
  while n > 0:
      result = str(n % 2) + result
      n = n // 2
  return result  
assert decimal_to_binary(10) == '1010'
assert decimal_to_binary(0) == '0'
print(decimal_to_binary(10))  # 1010
print(decimal_to_binary(0))   # 0



# 3. Проверка на простое число
def is_prime(n: int) -> bool:
    # TODO: проверь, является ли число простым
    pass

assert is_prime(7) is True
assert is_prime(8) is False


# 4. НОД (алгоритм Евклида)
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

# Проверки
assert gcd(12, 18) == 6
assert gcd(25, 5) == 5

print(gcd(12, 18))  # 6
print(gcd(25, 5))   # 5



# 5. Шифр Цезаря (только зашифровка)
def caesar_encrypt(message: str, shift: int) -> str:
    result = []
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            offset = (ord(ch) - base + shift) % 26  # вот тут переменная называется offset
            result.append(chr(base + offset))
        else:
            result.append(ch)
    return "".join(result)

assert caesar_encrypt("hello", 3) == "khoor"
assert caesar_encrypt("Hello, World!", 5) == "Mjqqt, Btwqi!"
print(caesar_encrypt("hello", 3))           # khoor
print(caesar_encrypt("Hello, World!", 5))  # Mjqqt, Btwqi!


# 6. Генерация матрицы + поиск min и max элементов
from typing import List, Tuple
import random

def generate_matrix_and_find_min_max(m: int, n: int) -> Tuple[List[List[int]], Tuple[int, int], Tuple[int, int]]:
    matrix = [[random.randint(0, 100) for _ in range(n)] for _ in range(m)]

    min_val = matrix[0][0]
    max_val = matrix[0][0]
    min_pos = (0, 0)
    max_pos = (0, 0)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_pos = (i, j)
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_pos = (i, j)

    return matrix, min_pos, max_pos
# пример вызова:
# matrix, min_pos, max_pos = generate_matrix_and_find_min_max(3, 3)
matrix, min_pos, max_pos = generate_matrix_and_find_min_max(3, 3)
print("Матрица:")
for row in matrix:
    print(row)
print(f"Минимальный элемент в позиции: {min_pos}")
print(f"Максимальный элемент в позиции: {max_pos}")


# 7. Сумма по главной диагонали
# Работает только для квадратных матриц
from typing import List

def main_diagonal_sum(matrix: List[List[int]]) -> int:
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

# Проверка:
matrix_7 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
assert main_diagonal_sum(matrix_7) == 15
print(main_diagonal_sum(matrix_7))  # Выведет 15
