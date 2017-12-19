
class Basket(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.area = []

    def put_in(self, some):
        if self.capacity < some.capacity:
            print('{} to big for basket\n'.format(some))
            print('Left capacity {}\n'.format(self.capacity))
        else:
            self.area.append(some)
            self.capacity = self.capacity - some.capacity
            print('{} placed to basket \n'.format(some))
            print('Left capacity {}\n'.format(self.capacity))


class Package(Basket):
    pass


class Paper(object):
    def __init__(self, capacity):
        self.capacity = capacity


class Polygon(object):
    def __init__(self, polygon):
        self.len = len(polygon)
        self.polygon = polygon
        self.area = None
        self.perimeter = None

    def calculate_area_perimeter(self):
        if self.len == 1:
            self.area = self.polygon[0] ** 2
            self.perimeter = self.polygon[0] * 4
        elif self.len == 2:
            self.area = self.polygon[0] * self.polygon[1]
            self.perimeter = self.polygon[0] * 2 + self.polygon[1] * 2
        elif self.len == 3:
            self.perimeter = self.polygon[0] + self.polygon[1] + self.polygon[2]
        elif self.len >= 4:
            y = 0
            for x in self.polygon:
                y += x
            self.perimeter = y
        print('Perimeter = {}'.format(self.perimeter))
        if self.area:
            print('Area = {}'.format(self.area))
        else:
            print('Few data to calculate area.')


list_numbers = []
data = input('Please input number: ')
for i in data:
    if i.isdigit():
        list_numbers.append(int(i))
print(list_numbers)
polyg = Polygon(list_numbers)
polyg.calculate_area_perimeter()


