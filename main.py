import random
import time


class Player:
    def __init__(self):
        self.money = 0
        self.level = 0
        self.zoo_rating = 0


class Zoo:
    def __init__(self):
        self.voliers_amount = 0
        self.animals_amount = 0
        self.max_visitors = 1


class FoodType:
    Grass = ('Grass', 1, 5)
    Meat = ('Meat', 2, 10)


class VisitorData:
    Child = frozenset(i for i in range(1, 7))
    Adult = frozenset(i for i in range(7, 60))


class Visitor(VisitorData):
    def __init__(self):
        age = random.randint(1, 60)
        if age in VisitorData.Child:
            self.ticket_price = 0
        elif age in VisitorData.Adult:
            self.ticket_price = 100


class AnimalData:
    # type_food_eating = ("Grass", 'Meat')
    # sizeA = ('Small', "Middle", "Big")
    # food_amount = (5, 10, 15)
    # rare = (1, 2, 3, 4, 5)
    # habitat = ('Water', 'Ground')

    Tiger = (FoodType.Meat, 'Middle', 10, 5, 'Ground')
    Elephant = (FoodType.Grass, 'Big', 5, 3, 'Ground')


class Animal(AnimalData):
    def __init__(self):
        pass


class Food(FoodType):
    def __init__(self, object):
        self.hj = AnimalData.Tiger[0]

    def str(self):
        str = self.hj
        return str



class typeVolier:
    smallVolierGround = ('Small', 'Ground')
    middleVolierGround = ('Middle', 'Ground')
    bigVolierGround = ('Big', 'Ground')
    smallVolierWater = ('Small', 'Water')
    middleVolierWater = ('Middle', 'Water')
    bigVolierWater = ('Big', 'Water')

class Volier(typeVolier):
    pass
