try:
    one = input("Введите значение для переменной one: ")
    two = input("Введите значение для переменной two: ")
    three = input("Введите значение для переменной three: ")
    total_sum = int(one)/int(two)/int(three)
except ValueError as e:
    print(f"Ошибка: {e}")
else:
    print(f"Сумма введенных чисел: {total_sum}")
finally:
    print("Мы хорошо поработали")
