# 5 - Реализуйте алгоритм перемешивания списка.

import random
print('Задача №5')
n = int(input('Enter number N: '))
a_list = list(range(-n, n+1))
print("List of N elements: ", a_list)
a_list.reverse()
print("Reverse a_list: ", a_list)
random.shuffle(a_list)
print("Random a_list: ", a_list)
