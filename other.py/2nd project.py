#конвертер валют 
eur_to_byn = 3.26

eur = float(input("Введите сумму в евро"))
byn = eur * eur_to_byn

print(f"{eur} EUR = {byn:.2f} BYN")