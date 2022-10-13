# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Задача №2')
N = int(input('Введите число '))
a_list = list(range(1, N+1, 1))
fact_1 = a_list[0]
fact_2 = a_list[0] * a_list[1]
fact_3 = a_list[0] * a_list[1] * a_list[2]
fact_4 = a_list[0] * a_list[1] * a_list[2] * a_list[3]
b_list = [fact_1, fact_2, fact_3, fact_4]
print(b_list)
print(f"({a_list[0]}, {a_list[0]}*{a_list[1]}, {a_list[0]}*{a_list[1]}*{a_list[2]}, {a_list[0]}*{a_list[1]}*{a_list[2]}*{a_list[3]})")
