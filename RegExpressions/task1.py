
# Используем регулярные выражения для извлечения информации
import re
text = input("Введите информацию")
match1 = re.search(r'D\w+', text)
match2 = re.search(r'S\w+',text)
match3 = re.search(r'\d+',text)
match4 = re.search(r'\d\d.\d\d.\d+',text)
match5 = re.search(r'p\w+',text)
match6 = re.search(r'g\w+',text)

name = match1.group()
surname = match2.group()
age = match3.group()
date= match4.group()
location = match5.group()
location2=match6.group()
print(name)
print(surname)
print(age)
print(date)
print(location)
print(location2)

