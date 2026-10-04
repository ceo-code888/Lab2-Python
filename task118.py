import sys

# Зчитуємо дані рядок за рядком зі стандартного вводу
for line in sys.stdin:
    # Пропускаємо порожні рядки, щоб не було помилки перетворення
    if line.strip():
        v = float(line.strip())
        
        # Послідовно перевіряємо діапазони швидкостей
        if v < 7.8:
            print("The device fell to the surface of the Earth.")
        elif 7.8 <= v < 11.2:
            print("The device became a satellite of the Earth.")
        elif 11.2 <= v < 16.4:
            print("The device became a satellite of the Sun.")
        else:
            print("The device left the Solar system.")