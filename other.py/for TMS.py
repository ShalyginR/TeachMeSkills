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
