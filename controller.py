import view
import model


def run():
    num = 1
    while num > 0:
        view.input_data()
        num = int(input('Выберите действие из меню: '))
        if num == 1:
            model.show_dict()
        elif num == 2:
            model.enter_cont()
        elif num == 3:
            model.find_cont()
        elif num == 4:
            model.del_cont()
        elif num == 5:
            model.del_all()
        elif num == 0:
            pass
