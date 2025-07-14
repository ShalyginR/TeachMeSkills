"""
Домашнее задание: Работа с файлами, строками и форматами данных
TeachMeSkills
"""

import os
import re
import json
import csv

from typing import List, Dict, Any
from collections import Counter

# === ЗАДАНИЕ 1 ===
# Работа с модулем os
import os


def task_1_sort_files_by_extension():
    """
    Вывести имя ОС и текущую директорию.
    Отсортировать файлы по расширениям, переместить их в подпапки.
    Переименовать один файл в одной из подпапок.
    """
    # TODO: реализовать функциональность по заданию 1
    # Вывожу имя ОС и текущую директорию
    print(f"Operating System: {os.name}")
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")

    # Создаю тестовые файлы для проверки работы
    with open("test1.txt", "w") as f:
        f.write("Просто текстовый файл.")
    with open("test2.py", "w") as f:
        f.write("print('Hello from Romas')")
    with open("data.csv", "w") as f:
        f.write("name,age\nAlice,30")

    # Получаю список всех файлов в текущей директории
    files = [
        f
        for f in os.listdir(current_dir)
        if os.path.isfile(os.path.join(current_dir, f))
    ]
    print(f"Found files: {files}")

    # Перемещаю каждый файл в папку по его расширению
    for file in files:
        ext = os.path.splitext(file)[1].lower().strip(".")
        if ext == "":
            ext = "no_extension"  # Если файла нет расширения, кладу в отдельную папку

        folder_name = f"{ext}_files"
        folder_path = os.path.join(current_dir, folder_name)

        os.makedirs(folder_path, exist_ok=True)

        old_path = os.path.join(current_dir, file)
        new_path = os.path.join(folder_path, file)

        os.rename(old_path, new_path)
        print(f"Moved file '{file}' to folder '{folder_name}'")

    # Получаю список всех созданных папок (с расширениями)
    folders = [
        f"{ext}_files"
        for ext in set(
            (
                os.path.splitext(f)[1].lower().strip(".")
                if os.path.splitext(f)[1].lower().strip(".") != ""
                else "no_extension"
            )
            for f in files
        )
    ]

    # Переименовываю первый файл в первой папке
    if folders:
        first_folder = folders[0]
        folder_path = os.path.join(current_dir, first_folder)
        files_in_folder = os.listdir(folder_path)

        if files_in_folder:
            old_name = files_in_folder[0]
            old_file_path = os.path.join(folder_path, old_name)

            name, ext = os.path.splitext(old_name)
            new_name = name + "_renamed" + ext
            new_file_path = os.path.join(folder_path, new_name)

            os.rename(old_file_path, new_file_path)
            print(
                f"Renamed file '{old_name}' to '{new_name}' in folder '{first_folder}'"
            )


if __name__ == "__main__":
    task_1_sort_files_by_extension()


# === ЗАДАНИЕ 2 ===
# Замена ФИО в судебном решении
import re


def task_2_replace_names(text: str) -> str:
    """
    Заменить ФИО на 'N'. ФИО начинается с заглавной буквы. Фамилия может быть двойной.
    """
    # TODO: реализовать замену ФИО на "N" с помощью регулярных выражений
    words = text.split()
    result_words = []
    i = 0

    while i < len(words):
        # Проверяем, начинается ли слово с заглавной буквы (русской или английской)
        if words[i][0].isupper():
            # Попытаемся проверить следующего слова и, возможно, третьего
            count = 1
            # Проверяем, есть ли следующие слова с заглавной буквы подряд
            for j in range(i + 1, min(i + 3, len(words))):
                if words[j][0].isupper():
                    count += 1
                else:
                    break
            if count >= 2:
                # Заменяем эти слова на 'N'
                result_words.append("N")
                i += count  # Пропускаем заменённые слова
                continue
            else:
                # Если следующего заглавного слова нет, просто добавляем текущее
                result_words.append(words[i])
                i += 1
        else:
            result_words.append(words[i])
            i += 1

    return " ".join(result_words)

# Пример
if __name__ == "__main__":
    text = "Подсудимая Эверт-Колокольцева Елизавета Александровна пришла в суд."
    print(task_2_replace_names(text))


# === ЗАДАНИЕ 3 ===
# Самое частое слово в каждой строке
from collections import Counter
def task_3_most_frequent_words(input_file: str, output_file: str):
    """
    Считать строки из файла, найти самое частое слово в каждой строке,
    записать его и количество повторений в новый файл.
    """
    # TODO: реализовать функциональность по заданию 3
    with open(input_file, "r", encoding="utf-8") as fin, \
         open(output_file, "w", encoding="utf-8") as fout:

        for line in fin:
            # Убираю пробелы по краям и перевожу строку в нижний регистр
            clean_line = line.strip().lower()

            # Разбиваю строку на отдельные слова
            words = clean_line.split()

            if not words:
                continue  # Если строка пустая, просто пропускаю

            # Считаю, сколько раз каждое слово встречается
            counter = Counter(words)

            # Получаю самое частое слово и его количество
            most_common_word, count = counter.most_common(1)[0]

            # Записываю в файл в формате: слово - количество
            fout.write(f"{most_common_word} - {count}\n")


# === ЗАДАНИЕ 4 ===
# Не обязательно к выполнению !!!
# Цензура текста
def task_4_censorship(input_file: str, stop_words_file: str):
    """
    Заменить запрещённые слова в файле звездочками.
    Замену делать без учёта регистра, даже если слово часть другого.
    """
    # TODO: реализовать функциональность по заданию 4
    pass


# === ЗАДАНИЕ 5 ===
# Вывод студентов с оценкой ниже 3
def task_5_low_scores(file_path: str) -> list[str]:
    """
    Прочитать файл с фамилиями и оценками. Вывести студентов с оценкой < 3.
    """
    low_score_students = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            parts = clean_line.split()

            # Проверяем, что строка содержит ровно 3 части (Фамилия Имя Оценка)
            if len(parts) == 3:
                surname, name, grade_str = parts

                # Проверяем, что оценка - число
                if grade_str.isdigit():
                    grade = int(grade_str)

                    # Если оценка меньше 3, добавляем строку в результат
                    if grade < 3:
                        low_score_students.append(f"{surname} {name} {grade}")

    return low_score_students
if __name__ == "__main__":
    result = task_5_low_scores("grades.txt")
    print("Студенты с оценкой ниже 3:")
    for student in result:
        print(student)

# === ЗАДАНИЕ 6 ===
# Сумма чисел в тексте
import re
def task_6_sum_numbers(file_path: str) -> int:
    """
    Найти сумму всех чисел (последовательностей цифр) в файле.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        total = 0 #начальное значение 0 
        for line in file:
            numbers = re.findall(r'\d+', line)
            total += sum(map(int, numbers)) #прописываем новый "total"
    return total 
result = task_6_sum_numbers("c:/MyPythonProjects/my projects/other.py/numbers.txt") #прописал путь к папке с файлом "numbers.txt"
print(result)

# === ЗАДАНИЕ 7 ===
# Не обязательно к выполнению !!!
# Шифр Цезаря с шагом по номеру строки
def task_7_caesar_cipher(file_path: str):
    """
    Зашифровать каждую строку файла шифром Цезаря, шаг зависит от номера строки.
    """
    # TODO: реализовать функциональность по заданию 7
    pass


# Пути к файлам
DATA_JSON = "employees.json"
DATA_CSV = "employees.csv"


def load_json_data(path: str) -> List[Dict[str, Any]]:
    """
    Считать данные из JSON-файла.

    :param path: путь к JSON-файлу
    :return: список сотрудников
    """
    # TODO: Открыть файл и считать данные через json.load()
    # Подумайте, что возвращать, если файл пустой или не существует
    return []


def save_to_csv(data: List[Dict[str, Any]], path: str) -> None:
    """
    Сохранить список сотрудников в CSV-файл.

    :param data: список словарей-сотрудников
    :param path: путь к CSV-файлу
    """
    # TODO: Открыть файл на запись
    # Используйте csv.writer
    # Не забудьте записать заголовок (name, age, birth_year, height, languages)
    # Языки можно объединить через ";"
    pass


def get_employee_from_input() -> Dict[str, Any]:
    """
    Запрашивает данные о сотруднике с клавиатуры.

    :return: словарь с данными сотрудника
    """
    name = input("Имя сотрудника: ").strip()
    age = int(input("Возраст: "))
    birth_year = int(input("Год рождения: "))
    height = int(input("Рост (в см): "))
    languages = input("Знание языков программирования (через запятую): ")
    languages_list = [lang.strip() for lang in languages.split(",")]

    return {
        "name": name,
        "age": age,
        "birth_year": birth_year,
        "height": height,
        "languages": languages_list,
    }


def add_employee_json(path: str) -> None:
    """
    Добавить нового сотрудника в JSON-файл.

    :param path: путь к JSON-файлу
    """
    # TODO: Сначала загрузите данные из JSON
    # Используйте get_employee_from_input() чтобы получить нового сотрудника
    # Добавьте в список и сохраните обратно в JSON
    pass


def add_employee_csv(path: str) -> None:
    """
    Добавить нового сотрудника в CSV-файл.

    :param path: путь к CSV-файлу
    """
    # TODO: Используйте get_employee_from_input()
    # Добавьте сотрудника как новую строку в CSV-файл
    # Преобразуйте список языков в строку через ";"
    pass


def find_employee_by_name(name: str, data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Найти сотрудника по имени.

    :param name: имя для поиска
    :param data: список сотрудников
    :return: найденный словарь или пустой словарь
    """
    # TODO: Пройдитесь по списку сотрудников и сравните имя
    # Используйте .lower() для нечувствительности к регистру
    return {}


def filter_by_language(
    language: str, data: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Фильтр сотрудников по языку программирования.

    :param language: язык программирования
    :param data: список сотрудников
    :return: список подходящих сотрудников
    """
    # TODO: Используйте list comprehension
    # Сравнивайте язык в нижнем регистре
    return []


def average_height_before_year(year: int, data: List[Dict[str, Any]]) -> float:
    """
    Средний рост сотрудников, родившихся до указанного года.

    :param year: граничный год
    :param data: список сотрудников
    :return: средний рост
    """
    # TODO: Отберите сотрудников с birth_year < year
    # Найдите их рост, затем вычислите среднее значение
    # Обработайте случай, когда таких сотрудников нет
    return 0.0


def task_8_json_csv_menu() -> None:
    """
    Меню пользователя для работы с JSON/CSV-файлами.
    """
    while True:
        print("\n=== Меню сотрудников ===")
        print("1. Показать всех сотрудников (из JSON)")
        print("2. Добавить сотрудника (в JSON)")
        print("3. Добавить сотрудника (в CSV)")
        print("4. Найти сотрудника по имени")
        print("5. Фильтр по языку программирования")
        print("6. Средний рост сотрудников, рождённых до заданного года")
        print("0. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            # TODO: Загрузите данные и выведите каждого сотрудника
            pass

        elif choice == "2":
            # TODO: Вызовите add_employee_json
            pass

        elif choice == "3":
            # TODO: Вызовите add_employee_csv
            pass

        elif choice == "4":
            # TODO: Спросите имя, найдите сотрудника, выведите его
            pass

        elif choice == "5":
            # TODO: Спросите язык, выведите всех сотрудников с этим языком
            pass

        elif choice == "6":
            # TODO: Введите год, найдите средний рост
            pass

        elif choice == "0":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


# Пример вызова функций (можно закомментировать)
if __name__ == "__main__":
    print("=== Домашнее задание Python ===")
    task_1_sort_files_by_extension()

    text_task_2 = (
        "Подсудимая Эверт-Колокольцева Елизавета Александровна"
        "в судебном заседании вину инкриминируемого правонарушения"
        "признала в полном объёме и суду показала, что 14 сентября"
        "1876 года, будучи в состоянии алкогольного опьянения"
        "от безысходности, в связи с состоянием здоровья позвонила"
        "со своего стационарного телефона в полицию, сообщив о том, что"
        "у неё в квартире якобы заложена бомба"
    )
    result_task_2 = task_2_replace_names(text_task_2)
    print(result_task_2)

    task_3_most_frequent_words("input.txt", "output.txt")
    """
    Expected output.txt:
        python - 2
        hello - 3
        three - 3
        this - 1
    """

    # Не обязательно к выполнению
    # task_4_censorship("text_to_censor.txt", "stop_words.txt")

    expected = ["Petrova Olga 2", "Lee Min 1", "Kowalski Adam 2"]
    result_task_5 = task_5_low_scores("grades.txt")
    assert result_task_5 == expected, f"Expected {expected}, but got {result_task_5}"

    result_task_6 = task_6_sum_numbers("numbers.txt")
    assert 244 == result_task_6

    # Не обязательно к выполнению !!!
    # task_7_caesar_cipher("lines.txt")

    task_8_json_csv_menu()
