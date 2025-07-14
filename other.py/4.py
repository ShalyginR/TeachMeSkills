#касса
cost = float(input("Введите стоимость товара: "))
paid = float(input("Введите сумму оплаты: -"))

if paid >= cost:
   change = paid - cost
   print ("Сдача:" , change)
else:
   print("Недостаточно средств!")
