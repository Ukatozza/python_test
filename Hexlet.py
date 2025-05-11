from capitalize import capitalize

if capitalize("hello") != "Hello":
    raise Exception("Функция работает неверно!")

if capitalize("") != "":
    raise Exception("Функция работает неверно!")

print("Все тесты пройдены!")

#Использование модуля assert

# Тест 1: Проверка обычной строки
assert capitalize("hello") == "Hello", "Функция должна capitalize первую букву"

# Тест 2: Проверка пустой строки
assert capitalize("") == "", "Функция должна возвращать пустую строку"

# Тест 3: Дополнительные проверки (по желанию)
assert capitalize("hello world") == "Hello world", "Должна capitalize только первую букву"
assert capitalize("h") == "H", "Должна работать с одним символом"
assert capitalize("123") == "123", "Должна корректно обрабатывать цифры"