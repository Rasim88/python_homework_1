# 3 - Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

print('Задача №3')
n = int(input('Enter the number: '))
a_list = list(range(1, n+1, 1))
print(a_list)
b_list = [(((1+1/i))**i) for i in a_list]
print(b_list)
print(sum(b_list))
