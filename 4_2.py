# 2 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math  # импортируем математический модуль

def simple_mult(num):  # печать числа
    while num % 2 == 0:  # цикл выявления четных чисел
        print(2,)
        num = num / 2
    for i in range(3, int(math.sqrt(num)) + 1, 2): # вычисляем квадратный корень из оставшихся нечетных чисел
        while num % i == 0:
            print(i,)
            num = num / i
    if num > 2:
        print(num)

num = int(input('Enter any number: '))
simple_mult(num)
