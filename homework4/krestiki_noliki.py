
import random

FIELD = {
         1: '-', 2: '-', 3: '-',
         4: '-', 5: '-', 6: '-',
         7: '-', 8: '-', 9: '-',
}

TUPLE_WINS_STR = (
                  (1, 2, 3), (4, 5, 6), (7, 8, 9),
                  (1, 4, 7), (2, 5, 8), (3, 6, 9),
                  (1, 5, 9), (3, 5, 7)
)


def perform_move(field, move):
    try:
        if field[move] != '-':
            raise ValueError('Это поле уже занято.')
        else:
            field[move] = 'X'
    except ValueError as e:
        print(e)

    return field


def perform_comp_move(field):
    print('Ход компьютера')
    new_filed = {}
    for key, values in field.items():
        if values == '-':
            new_filed[key] = values
    comp_move = random.choice(list(new_filed.keys()))
    field[comp_move] = 'O'
    return field


def print_field(field):
    for key, value in field.items():
        if key % 3 != 0:
            print(value, end=' ')
        else:
            print(value, end='\n')


def user_input():
    while True:
        try:
            move = int(input('Ваш ход: '))
            if move not in (range(1, 10)):
                raise ValueError
            else:
                break
        except ValueError:
            print('Пожалуйста пользуйтесь цифрами от 1 до 9, что бы сделать ход')
    return move


def is_game_finished(field, x_or_o):
    moving_set = set()
    for key, value in field.items():
        if value == x_or_o:
            moving_set.add(key)
    for item in TUPLE_WINS_STR:
        if moving_set.issuperset(item):
            return True


def draw_game(field):
    empty_list = []
    for key, value in field.items():
        if value == '-':
            empty_list.append(key)
    if len(empty_list) == 0:
        return True


def main():
    print('Добро пожаловать в игру Крестики&Нолики!')
    print('Ходы осуществляются с помощью клавишь 1-9.')
    print('Для выхода из игры нажмите Ctrl+C')
    game_field = FIELD.copy()
    print_field(game_field)
    while True:
        while True:
            new_game_field = game_field.copy()
            moving = user_input()
            perform_move(game_field, moving)
            print_field(game_field)
            if new_game_field != game_field:
                break
        if is_game_finished(game_field, 'X'):
            print('Вы победили!')
            break
        if draw_game(game_field):
            print('Ничья.')
            break
        game_field = perform_comp_move(game_field)
        print_field(game_field)
        if is_game_finished(game_field, 'O'):
            print('Победил компьютер')
            break
        if draw_game(game_field):
            print('Ничья.')
            break

if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt as e:
            print('Игра закрыта')


