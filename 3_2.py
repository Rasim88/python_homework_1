# 2 - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
one_lst = [random.randint(0, 10) for _ in range(5)]
two_lst = []
multiple = 1
for i in range((len(one_lst) + 1) // 2):
        multiple = one_lst[i] * one_lst[-i-1]
        two_lst.append(multiple)
        print(one_lst)
        print(two_lst)

