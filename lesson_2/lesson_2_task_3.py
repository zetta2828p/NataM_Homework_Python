# Площадь квадрата округляя вверх, если сторона не является целым числом
import math

def square(side):
    area = side * side

    if not isinstance(side, int) or isinstance(side, float):  # Проверяем, является ли сторона целым числом
        area = math.ceil(area)  # Округляем вверх, если число не целое

    return area

num_side = float(input("Укажите размер стороны квадрата: "))
print(f"Площадь квадрата равна: {square(num_side)}")
