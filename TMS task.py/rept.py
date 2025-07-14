def binary_search_recursive(arr, target, left, right):
    """
    Рекурсивная реализация бинарного поиска.

    :param arr: отсортированный список чисел
    :param target: искомое число
    :param left: левая граница поиска
    :param right: правая граница поиска
    :return: индекс элемента или -1, если не найден
    """
    if left > right:
        return -1  # Базовый случай: элемент не найден

    mid = (left + right) // 2  # Находим середину

    if arr[mid] == target:
        return mid  # Нашли элемент
    elif target < arr[mid]:
        # Ищем в левой половине
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        # Ищем в правой половине
        return binary_search_recursive(arr, target, mid + 1, right)


#Пример использования

numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

#Вызываем бинарный поиск
result = binary_search_recursive(numbers, target, 0, len(numbers) - 1)

#Выводим результат
if result != -1:
    print(f"Число {target} найдено на позиции {result}")
else:
    print(f"Число {target} не найдено в списке")
