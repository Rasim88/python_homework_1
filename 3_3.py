# 3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.2

from decimal import *
lst = [1.1, 1.2, 3.1, 5.0001, 10.01]
min, max = 1, 0
for element in lst:
    element = str(element)
    element = element.split('.') if '.' in element else ['0', '0']
    fract = int(element[1]) / 10 ** len(element[1])
    if fract > max:
        max = fract
    elif fract < min:
        min = fract
print(f"\nMin = {min}, Max = {max}")
print(f"Difference = {Decimal(str(max)) - Decimal(str(min))}")
