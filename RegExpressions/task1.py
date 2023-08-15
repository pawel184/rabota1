text = input("Введите информацию о себе
# Используем регулярные выражения для извлечения информации
import re

pattern = r"Hi, my name is (\w+) and surname is (\w+). I am (\d+) years old and I am leaving in (\w+), (\w+)"
match = re.search(pattern, text)

if match:
    name = match.group(1)
    surname = match.group(2)
    age = match.group(3)
    location = f"{match.group(4)}, {match.group(5)}"

    # Выводим информацию
    print(f"Name: {name}")
    print(f"Surname: {surname}")
    print(f"Age: {age}")
    print(f"Location: {location}")
else:
    print("Информация не найдена.")