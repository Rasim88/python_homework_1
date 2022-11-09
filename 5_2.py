# 2 - Создайте программу для игры с конфетами человек против
# человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты
# оппонента достаются сделавшему последний ход. Сколько конфет
# нужно взять первому игроку, чтобы забрать все конфеты у своего
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

print('Total 2021 candies. In one move, you can take no more than 28 candies')

messages = ['Your move...']


def candy_game(a, b, players, messages):
    count = 0
    while a > 0:
        print(f'{players[count%2]}, {random.choice(messages)}')
        move = int(input())
        if move > a or move > b:
            print(
                f'You can take no more than {b} candies, we have {a} candies')
            attempt = 3
            while attempt > 0:
                if a >= move <= b:
                    break
                print(f'Try again, you have {attempt} attempts')
                move = int(input())
                attempt -= 1
            else:
                return print(f'You dont have any attempts!')
        a = a - move
        if a > 0:
            print(f'There are {a} candies')
        else:
            print('There are no more sweets.')
        count += 1
    return players[not count % 2]


player1 = input('First player?\n')
player2 = input('Second player?\n')
players = [player1, player2]

a = int(input('Please, enter total 2021 candies:\n '))
b = int(input('Please, enter the number of candies is not more than 28:\n '))

winer = candy_game(a, b, players, messages)
if not winer:
    print('We dont have a winner.')
else:
    print(f'This time {winer} won!')
