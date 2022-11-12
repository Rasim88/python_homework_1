# 2 - Дана последовательность чисел. Получить список уникальных элементов 
# заданной последовательности, список повторяемых и убрать дубликаты из 
# заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

lst = [1, 2, 3, 5, 1, 5, 3, 10] 

first_lst = [i for i in set(lst) if lst.count(i) < 2]
second_lst = [i for i in set(lst) if lst.count(i) > 1]
print(f'You list: {lst}')
print(f'List of unique elements: {first_lst}')
print(f'List of duplicates: {second_lst}')
print(f'List without duplicates: {list(set(lst))}')