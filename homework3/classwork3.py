import random
def err_func():
    list_err = (ValueError(), TypeError(), RuntimeError())
    raise list_err[random.randint(0, 2)]
try:
    err_func()
except ValueError:
    print('Catch ValueError!')
except TypeError:
    print('Catch TypeError')
except RuntimeError:
    print('Catch RuntimeError')


def sort_list_func(s_list):
    try:
        for item in s_list:
            if not isinstance(item, int):
                raise ValueError()
    except TypeError as e:
        print(e)
    s_list.sort()
    return s_list
print(sort_list_func([1, 6, 4, 9]))


def key_to_str(some_dict):
    new_dict = {}
    for key, value in some_dict.items():
        new_dict[str(key)] = value
    return new_dict
print(key_to_str({1: '1', 3: 2}))

def mul_items_func(some_list):
    n = 1
    for item in some_list:
        n *= item
    return n

print(mul_items_func([1,2,3]))