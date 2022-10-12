print ('Задача №1')
num = int (input ('Enter number form 1 at 7 indicating the day of the week: '))
if num < 6 and num > 0:
    print ('Weekday')
elif num == 6 or num == 7:
    print ('Weekend')
elif num > 7:
        print ('Only 7 days a week)')
else:
        print ('Weekend')

print ('Задача №2')
print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
s = range(2)
result = True

for x in s:
    for y in s:
        for z in s:
            if not(not(x or y or z) == (not x and not y and not z)):
                result = False
                break
print(result)