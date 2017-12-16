import random

# task1


def number_err_func():
    try:
        number = int(input('Введите число: '))
        if number < 0:
            raise TypeError('Меньше 0')
        elif number > 10:
            raise IndexError('Больше 10')
        elif number % 2 == 0:
            raise ValueError('Четное число')
    except TypeError as ex:
        print(ex)
    except IndexError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


# task2
def err_index_func():
    try:
        r_list = random.sample(range(1, 10), random.choice(range(1, 10)))
        print(r_list)
        input_index = int(input('Введите индекс списка '))
        item = r_list[input_index]
        print(item)
    except IndexError as ex:
        print('Ups', ex)
    except ValueError as ex:
        print('Ouu', ex)

# task3


def easy_mat_func(x, y):
    if x > 0 and y > 0:
        return x + y
    elif x < 0 and y < 0:
        return x - y
    elif x < 0 < y or x > 0 > y:
        return 0


# task4


def two_max_numbers(x, y, z):
    list_ = [x, y, z]
    list_.remove(min(list_))
    return list_[0], list_[1]


# task5


def sort_list_numbers(some_list, flag):
    new_list = []
    for item in some_list:
        if flag and item % 2 != 0:
            new_list.append(item)
        elif not flag and item % 2 == 0:
            new_list.append(item)
    return new_list


# task6

def max_min_func(*args):
    return max(list(args)), min(list(args))

# task7


def upper_lower_func(string, case=True):
    if case:
        new_string = string.upper()
    else:
        new_string = string.upper()
    return new_string

# task8


def join_string_func(*args, glue=':'):
    list_string = []
    for string in args:
        if len(string) < 3:
            list_string.append(string)
    print(glue.join(list_string))




