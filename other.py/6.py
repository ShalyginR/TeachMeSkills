# Ввод данных
cost = float(input("Введите сумму счета: "))
fee = float(input("Введите процент чаевых: "))
people = int(input("Введите количество человек: "))

# Проверка на некорректное количество человек
if people < 1:
    print("Ошибка: деление на ноль или некорректное число человек")
else:
    # Расчёт чаевых и общей суммы
    fee_amount = cost * fee / 100
    final_amount = cost + fee_amount

    # Вывод общей информации
    print("Сумма счета:", round(cost, 2))
    print("Чаевые:", round(fee_amount, 2))
    print("Общий чек:", round(final_amount, 2))

    # Проверка — один человек или больше
    if people == 1:
        print("Один человек — делить не нужно")
    else:
        # Делим сумму на всех (обычное деление)
        per_person = final_amount / people
        # Если хочешь округление вверх:
        # per_person = math.ceil(final_amount / people * 100) / 100
        print(f"Количество человек: {people}")
        print(f"Сумма на каждого человека: {round(per_person, 2)}")