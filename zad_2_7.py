import math

def f(x, y, z):
    #вычисляем значение функции F
    numerator = math.sqrt(math.tan(z**2) + 1 / math.tan(y**2))  #числитель
    denominator = z**2 - math.pi * x * y #знаменатель
    
    #проверка на деление на ноль
    if denominator == 0:
        raise ValueError("Деление на ноль: z^2 - pi * x * y равно нулю.")
    
    return numerator / denominator

#запрос координат у пользователя
try:
    x = float(input("Введите значение x (вещественное или целое число): "))
    y = float(input("Введите значение y (вещественное или целое число): "))
    z = float(input("Введите значение z (вещественное или целое число): "))

    #вычисление значения функции
    result = f(x, y, z)

    #вывод результата
    print(f"Значение функции F({x}, {y}, {z}) = {result}")

#проверка правильности введенных данных (орицательное подкоренное выражение/аргумент tan кратен pi/2)
except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
