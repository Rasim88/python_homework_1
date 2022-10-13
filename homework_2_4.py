# 4 - Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

print('Задача №4')
n = int(input('Enter number N: '))
a_list = list(range(-n, n+1))
print("List of N elements: ", a_list)
num_of_elements = int(len(a_list))
print("Number of elements in the a_list: ", num_of_elements)

try:
    file = open("file.txt")

    try:
        s = file.readlines()
        b_list = list(map(int, s))
        print("List from file.txt: ", b_list)
    finally:
        file.close()

except FileNotFoundError:
    print("Unable to open the file")
print("I don't know how to do it next . . . ")
