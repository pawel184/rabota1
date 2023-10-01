a=1


for a in range( 30):
    if a <= 7:
        print("Это диапазон чисел от 1 до 7")
        for i in range(1, 8):
            print(i)
            a=8
            
    
    elif a <= 15:
        print("Это диапазон чисел от 10 до 15")
        for i in range(10, 16):
            print(i)
            a=16
            
    
    elif a <= 30:
        print("Это диапазон чисел от 25 до 30")
        for i in range(25, 31):
            print(i)
            a=31
            continue
    
        print("Ой, забыли про эти числа")
        for i in range(8, 10):
         print(i)

        for i in range(16, 25):
         print(i)
        break