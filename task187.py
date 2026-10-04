# Список трицифрових чисел із вхідних даних задачі
numbers = [184, 244, 111]

for n in numbers:
    # Виділяємо цифри числа
    first = n // 100
    second = (n % 100) // 10
    last = n % 10
    
    # Знаходимо максимальну та мінімальну цифри
    mx = max(first, second, last)
    mn = min(first, second, last)
    
    # Якщо цифри однакові, виводимо лише одну, інакше — максимальну та мінімальну через пропуск
    if mx == mn:
        print(mx)
    else:
        print(f"{mx} {mn}")