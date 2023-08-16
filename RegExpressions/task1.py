
# Используем регулярные выражения для извлечения информации
import re
text = input("Введите информацию")

match1 = re.search(r'D\w+', text)
match2 = re.search(r'S\w+',text)
match3 = re.search(r'\d+',text)
match4 = re.search(r'G\w+',text)

name = match1.group()
surname = match2.group()
age = match3.group()
location = match4.group()

    # Выводим информацию
print(name)
print(surname)
print(age)
print(location)

