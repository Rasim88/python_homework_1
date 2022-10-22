# 3) Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

nums = input('Set the sequence of number: ')
unique_nums = list(set(nums))
print(unique_nums)