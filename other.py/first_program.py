#Первый клалькулятор


num1 = float(input("Введите первое число: "))
operation = input("Выберете операцию(+, -, *, /): ")
num2 =  float(input("Выберите второе число: ",))

#выбираем что делаем
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result =  num1 * num2
elif operation == '/':
    if num2 !=0:
        result = num1 / num2
    else:
        result = "Ошибка: деление на ноль"
else:

    result = "Неизвестная операция"

#выводим результат
print('Результат:', result)
