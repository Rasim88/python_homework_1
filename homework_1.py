# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
print('Задача №1')
num = int(input('Enter number form 1 at 7 indicating the day of the week: '))
if num < 6 and num > 0:
    print('Weekday')
elif num == 6 or num == 7:
    print('Weekend')
elif num > 7:
    print('Only 7 days a week)')
else:
    print('Weekend')

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('Задача №2')
print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
s = range(2)
result = True
for x in s:
    for y in s:
        for z in s:
            if not (not (x or y or z) == (not x and not y and not z)):
                result = False
                break
print(result)

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
print('Задача №3')
x = int(input('Enter the coordinates of the X: '))
y = int(input('Enter the coordinates of the Y: '))
if x > 0 and y > 0:
    print('I quarter')
elif x < 0 and y > 0:
    print('II quarter')
elif x < 0 and y < 0:
    print('III quarter')
elif x > 0 and y < 0:
    print('IV quarter')
elif x == 0 and y != 0:
    print('the ordinate axis')
elif x != 0 and y == 0:
    print('the abscissa axis')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print('Задача №4')
z = int(input('Enter quarter number from 1 to 4: '))
if z == 1:
    print('Coordinates X > 0, Y > 0')
elif z == 2:
    print('Coordinates X < 0, Y > 0')
elif z == 3:
    print('Coordinates X < 0, Y < 0')
elif z == 4:
    print('Coordinates X > 0, Y < 0')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
print('Задача №5')
x_a = int(input('Enter the coordinates X point A: '))
y_a = int(input('Enter the coordinates Y point A: '))
x_b = int(input('Enter the coordinates X point B: '))
y_b = int(input('Enter the coordinates Y point B: '))
print('The distance between the points is equal to: ')
print(round(abs((((x_a - x_b)**2)+((y_a - y_b)**2))**0.5)))
