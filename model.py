import re


def show_dict():
    with open('phone.txt', 'r') as file:
        print(file.read())


def enter_cont():
    id = input('Введите id контакта: ')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    birthday = input('Укажите дату рождения: ')
    work = input('Укажите место работы: ')
    phone_book = f'\n{id} {first_name} {last_name} {phone} {birthday} {work}'
    with open('phone.txt', 'a+', encoding='utf-8') as file:
        file.write(phone_book)
    print(f'Добавлен новый контакт:{phone_book}')


def find_cont():
    value = input('Введите значение для поиска: ')
    with open(r'phone.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(value) != -1:
                print(value, 'Контакт существует в телефонной книге')
                print('Вывод:', line)


def del_cont():
    with open('phone.txt') as file:
        lines = file.readlines()
    str = input('Введите значение для удаления контакта: ')
    pattern = re.compile(re.escape(str))
    with open('phone.txt', 'w') as file:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                file.write(line)


def del_all(): 
    with open("phone.txt",'w') as file: 
        pass
