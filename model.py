import re
import logger as lg
import csv


def show_dict():
    lg.logging.info("The user has selected item number 1")
    with open('data.csv', 'r+') as file:
        lg.logging.info('User looked at the data of all employees')
        print(file.read())


def enter_cont():
    lg.logging.info('The user has selected item number 2')
    id = input('Введите id контакта: ')
    lg.logging.info('User entered: {id}')
    first_name = input('Введите имя: ')
    lg.logging.info('User entered: {first_name}')
    last_name = input('Введите фамилию: ')
    lg.logging.info('User entered: {last_name}')
    phone = input('Введите номер телефона: ')
    lg.logging.info('User entered: {phone}')
    birthday = input('Укажите дату рождения: ')
    lg.logging.info('User entered: {birthday}')
    work = input('Укажите должность: ')
    lg.logging.info('User entered: {work}')
    phone_book = f'\n{id} {first_name} {last_name} {phone} {birthday} {work}'
    with open('data.csv', 'a', encoding='utf-8') as file:
        file.write(phone_book)
    print(f'Добавлен новый сотрудник:{phone_book}')
    lg.logging.info('User added an employee: {phone_book}')


def find_cont():
    lg.logging.info('The user has selected item number 3')
    value = input('Введите значение для поиска: ')
    lg.logging.info('User entered: {value}')
    with open(r'data.csv', 'r') as file:
        for line in file:
            if line.find(value) != -1:
                print(value, 'Данный сотрудник есть в базе данных')
                print('Информация о сотруднике:', line)
                lg.logging.info('User looked at the employees data')


def edit_cont(): 
    lg.logging.info('The user has selected item number 4')
    info = input('Введите информацию о сотруднике, которую хотите редактировать: ')
    new_info = input('Введите новое значение: ')
    lg.logging.info('User entered: {new_info}')
    fin = open("data.csv", "rt")
    data = fin.read()
    data = data.replace(info, new_info)
    fin.close()
    fin = open("data.csv", "wt")
    fin.write(data)
    fin.close

def del_cont():
    lg.logging.info('The user has selected item number 5')
    with open('data.csv') as file:
        lines = file.readlines()
    str = input('Введите значение для удаления информации о сотруднике: ')
    lg.logging.info('User deleted: {str}')
    pattern = re.compile(re.escape(str))
    with open('data.csv', 'w') as file:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                file.write(line)


def del_all(): 
    lg.logging.info('The user has selected item number 6')
    open("data.csv", "w", encoding='utf-8').close()
    lg.logging.info('The user has delete all contacts')
