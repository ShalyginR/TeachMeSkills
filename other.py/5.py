cost = float(input("Введите сумму счета: "))
fee = float(input ("Введите процент чаевых: "))

total = cost
fee1 = total * fee / 100
final_amount = cost + fee1
print("Сумма счета" , total)

print("Чаевые:", round(fee1, 2))

print("Общий чек:", round(final_amount, 2))