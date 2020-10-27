class Player:
    def __init__(self):
        money = 0
        level = 0
        zoo_rating = 0


class Animal:
    def __init__(self):
        self.type_food_eating = 0


class Food:
    def __init__(self, object):
        self.hj = object.type_food_eating

    def str(self):
        str = self.hj
        return str


class FoodType:
    def __init__(self):
        self.rare = (1, 2)
        self.type = ('Grass', 'Meat')
        self.time = (5, 10)

    def str(self, hj):
        str = f'{self.type[hj]},{self.rare[hj]},{self.time[hj]}'
        return str

c = Animal()
a = FoodType()
b = Food(c)
print(a.str(b.str()))