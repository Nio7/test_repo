
import random

LIST_OF_WORDS = [
                 'apple', 'orange', 'pear', 'avocado',
                 'banana', 'papaya', 'pineapple', 'kiwi',
                 'lime', 'lemon', 'watermelon', 'mango',
]


def choice_and_return_word(word):
    lise_str = []
    for char in range(len(word)):
        lise_str.append('_')
    return lise_str


def printed_word(list_for_print):
    print_word = ' '.join(list_for_print)
    print(print_word)


def handle_user_input():
    while True:
        choice_char = input('Введите букву: ')
        if not choice_char.isalpha():
            print('Пожалуйста используйте только английские буквы.')
        else:
            break
    return choice_char.lower()


def guess_char(word, char, list_char):
    if char in word:
        for ch in word:
            if ch == char:
                list_char[word.index(ch)] = char
        return list_char
    else:

        return None


def main():
    print('Добро пожаловать в игру висилица!\n'
          'Попытайтесь угадать слово, у вас есть 10 попыток\n'
          'Все загаданные слова это фрукты на английскам\n'
          'Слово: ')
    counter = 10
    mystery_word = random.choice(LIST_OF_WORDS)
    repr_mystery_word = choice_and_return_word(mystery_word)
    while True:
        printed_word(repr_mystery_word)
        print('Осталось попыток {}.'.format(counter))
        try_char = handle_user_input()
        try_guess = guess_char(mystery_word, try_char, repr_mystery_word)
        if not try_guess:
            counter -= 1
        if '_' not in repr_mystery_word:
            print('Вы угадали!')
            printed_word(repr_mystery_word)
            break
        if counter == 0:
            print('Вы проиграли =(')

if __name__ == '__main__':
    main()


