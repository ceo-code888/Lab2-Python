# Список трицифрових чисел із вхідних даних задачі
numbers = [122, 121, 263]

for n in numbers:
    # Виділяємо цифри числа
    first = n // 100       # перша цифра
    second = (n % 100) // 10  # друга цифра
    last = n % 10          # остання цифра
    
    # Знаходимо суму першої та останньої цифри
    total_sum = first + last
    
    # Порівнюємо суму з другою цифрою та виводимо результат
    if total_sum > second:
        print(">")
    elif total_sum < second:
        print("<")
    else:
        print("=")