# Список номерів із вхідних даних задачі 
numbers = [24, 34, 10, 42]

for n in numbers:
    # 1. Перевіряємо, чи виходить число за межі діапазоеу від 0 до 36
    if n < 0 or n > 36:
        print(f"The bet will not play!")
    elif n ==0:
        print("Green")

    # Діпазон від 1 до 10
    elif 1 <= n <=10:
        if n % 2 == 0: # парне
            print("Black")
        else: # непарне
            print("Red")

    # Діапазон від 11 до 18
    elif 11 <= n <= 18:
        if n % 2 == 0: # парне
            print("Red")
        else: # непарне
            print("Black")

    # Діапазон від 19 до 28
    elif 19 <= n <= 28:
        if n % 2 == 0: # парне
            print("Black")
        else: # непарне
            print("Red")

    # Діапазон від 29 до 36 
    elif 29 <= n <= 36:
        if n % 2 == 0: # парне
            print("Red")
        else: # непарне
            print("Black")