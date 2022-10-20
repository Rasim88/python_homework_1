# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_odd(lst):  # прописываем функцию
    summ = 0
    for i in range(len(lst)):
        if i % 2 != 0:  # выявляем нечетные элементы
            summ = summ + lst[i]
    print(f"Sum is equal to: {summ}")

lst = []
sum_odd(lst)
lst = list(map(int, input("Enter numbers:\n").split()))
sum_odd(lst)
