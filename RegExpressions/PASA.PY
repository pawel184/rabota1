start = 1
end = 30

# Начало цикла while
while start <= end:
    # Проверяем текущий диапазон чисел
    if start >= 1 and start <= 7:
        print("Это диапазон чисел от 1 до 7")
        while start <= 7:
            print(start)
            start += 1
        continue
    elif   start <= 15:
        print("Это диапазон чисел от 10 до 15")
        while start <= 15:
            print(start)
            start += 1
        continue
    elif start >= 25 and start <= 30:
        print("Это диапазон чисел от 25 до 30")
        while start <= 30:
            print(start)
            start += 1
        continue
    else:
        print("Ой забыли про эти числа")
        while start <= 24:
            print(start)
            start += 1
        continue

    

