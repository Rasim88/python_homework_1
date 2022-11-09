# 4 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и
# восстановления данных

# rle = input("Enter any symbol for Run-length encoding: ")

with open('words.txt', 'w') as file:
    file.write(input('Write the text for compression: '))
with open('words.txt', 'r') as file:
    new_txt = file.readline()
    compr_txt = new_txt.split()

print(new_txt)


def file_rle(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


compr_txt = file_rle(new_txt)

with open('new_words.txt', 'w') as file:
    file.write(f'{compr_txt}')
print(compr_txt)
