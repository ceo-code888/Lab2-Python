# Список пар вхідних даних: [набрані бали (n), максимальні бали (m)]
test_cases = [
    (70, 100)  # згідно з прикладом: набрано 70 зі 100
]

for n, m in test_cases:
    # Рахуємо відсоток набраних балів учня
    percentage = (n / m) * 100
    
    # Визначаємо оцінку за умовами задачі
    if percentage >= 90:
        print(12)
    elif percentage >= 70:
        print(8)
    elif percentage >= 50:
        print(5)
    else:
        print(2)