# 3 - Создайте программу для игры в ""Крестики-нолики"".

print("Game << Крестики - нолики >>")

board = list(range(1, 10))
# рисуем игровое поле


def paint_board(board):
    print("=" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("=" * 13)
# введение значений и их проверка


def input_data(token):
    valid = False
    while not valid:
        answer = input("Where to put " + token+"? ")
        try:
            answer = int(answer)
        except:
            print("Incorrect input. Enter a number from 1 to 9, please")
            continue
        if answer >= 1 and answer <= 9:
            if (str(board[answer-1]) not in "XO"):
                board[answer-1] = token
                valid = True
            else:
                print("This cell is occupied!")
        else:
            print("Incorrect input. Enter a number from 1 to 9, please")
# определяем выйгрышные линии


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
#  функция замены числовых значений символами Х или 0, проверка победы


def main(board):
    counter = 0
    win = False
    while not win:
        paint_board(board)
        if counter % 2 == 0:
            input_data("X")
        else:
            input_data("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "Won!")
                win = True
                break
        if counter == 9:
            print("Draw!")
            break
    paint_board(board)


main(board)

input("Click Enter to exit")
