
class Person(object):
    def __init__(self, age, name):
        self.age = age
        self. name = name
        self.list_of_friends = []

    def know(self, person):
        if person not in self.list_of_friends:
            self.list_of_friends.append(person)

    def is_know(self, person):
        if person in self.list_of_friends:
            print('Yes')
        else:
            print('No')


class Printer(object):
    def log(self, *value):
        for item in value:
            print(item)


class FormattedPrinter(Printer):
    def log(self, *value):
        for item in value:
            print('* {} *'.format(item))



class Animal(object):
    def __init__(self, name, kind, features):
        self.name = name
        self.kind = kind
        self.features = features


class Human(object):
    def is_dangerous(self, animal):
        if animal.features in ['poisonous', 'raptorial']:
            print('The {} animal is dangerous for human because '
                  'his is a {}'.format(animal.name, animal.features))
        else:
            print('The {} animal safe'.format(animal.name))

