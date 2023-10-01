current_number = 1

while current_number <= 30:
    if current_number <= 7:
        print("Это диапазон чисел от 1 до 7")
        for i in range(1, 8):
            print(i)
        current_number = 8 
        continue 
    elif  current_number <= 15:
        print("Это диапазон чисел от 10 до 15")
        for i in range(10, 16):
            print(i)
        current_number = 16 
        continue
    elif  current_number <= 30:
        print("Это диапазон чисел от 25 до 30")
        for i in range(25, 31):
            print(i)
        current_number = 31 
        print("Ой, забыли про эти числа")
        for i in range(8, 10):
                print(i)
        for i in range(16, 25):
            print(i)
         