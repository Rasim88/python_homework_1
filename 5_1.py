# 1 - Напишите программу, удаляющую из текста все слова,
# в которых присутствуют все буквы "абв".

text = input("Enter any text: ")


def delete_words(text):
    # фильтруем -> анонимная функция возвращает True -> разбиваем строку по разделителю
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)  # объединение списка строк


text = delete_words(text)
print(text)
