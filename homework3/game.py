import random

EMPTY_MARK = 'X'
MOVES = {
         'w': -4,
         's': 4,
         'a': -1,
         'd': 1
}


def shuffle_field():
    field = {
        1: 1, 2: 2, 3: 3, 4: 4,
        5: 5, 6: 6, 7: 7, 8: 8,
        9: 9, 10: 10, 11: 11, 12: 12,
        13: 13, 14: 14, 15: 15, 16: EMPTY_MARK
    }
    field_ok = False
    while not field_ok:
        rand_list = random.sample(range(1, 16), 15)
        for key in field:
            if field[key] == 'X':
                break
            else:
                field[key] = rand_list[key - 1]
        n = 0
        for key in field:
            if field[key] == key:
                n += 1
        if n % 2 == 0 and n != 0:
            field_ok = True
    return field


def perform_move(field, key):
    for square in field:
        if field[square] == 'X':
            try:
                if key == 1 and square in (4, 8, 12, 16):
                    raise KeyError
                elif key == -1 and square in (1, 5, 9, 13):
                    raise KeyError
                field[square] = field[square + key]
                field[square + key] = 'X'
                break
            except KeyError as e:
                print('Не верный ход. Попыдка выйти за рамки поля!')
    return field


def handle_user_input():
    try_moving = False
    moving = None
    while not try_moving:
        moving = input('Пожалуйста делайте свой ход: ')
        if moving.lower() not in ('w', 'a', 's', 'd'):
            print('Пользуйтесь, командами (w, a, s, d)')
        else:
            try_moving = True

    return MOVES[moving.lower()]


def print_field(field):
    for key, value in field.items():
        if key % 4 != 0:
            print(value,' ', end=' ')
        else:
            print(value, end='\n')
    print('\n')


def is_game_finished(field):
    list_cells = []
    win_list = list(range(1, 16))
    for key in range(1, 16):
        list_cells.append(field[key])
    if list_cells == win_list:
        print('<<<Ура, вы победили!!!>>>')
        return True
    else:
        return False


def main():
    count = 0
    over_game = False
    start_field = shuffle_field()
    print_field(start_field)
    new_field = start_field

    while not over_game:
        count += 1
        moving = handle_user_input()
        new_field = perform_move(new_field, moving)
        print_field(new_field)
        over_game = is_game_finished(new_field)
    print('Вы сделали {} ходов.'.format(count))
    print('Конец игры')


print('<<< Добро пожаловать в игру "Пятнашки" ! >>>')
print('Управление происходи с помощью клавишь WASD.')
print('Если хотите выйти из игры нажмите сочетание клавишь Ctrl+C.\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print('Игра закрыта')

