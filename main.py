class Player:
    def __init__(self):
        money = 0
        level = 0
        zoo_rating = 0


class AnimalData:
    # type_food_eating = ("Grass", 'Meat')
    # sizeA = ('Small', "Middle", "Big")
    # food_amount = (5, 10, 15)
    # rare = (1, 2, 3, 4, 5)
    # habitat = ('Water', 'Ground')


    Tiger = ('Meat', 'Middle', 10, 5, 'Ground')
    Elephant = ('Grass', 'Big', 5, 3, 'Ground')


class Animal(AnimalData):
    def __init__(self):
        pass



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
