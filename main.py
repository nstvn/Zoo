import random
from AnimalvsFood import *
import time


class Player:
    def __init__(self):
        self.money = 0
        self.level = 0
        self.zoo_rating = 0


class Zoo:
    def __init__(self):
        self.voliers = []
        self.animals_amount = 0
        self.max_visitors = 1


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


class typeVolier:
    smallVolierGround = ('Small', 'Ground', 'free')
    middleVolierGround = ('Middle', 'Ground', 'free')
    bigVolierGround = ('Big', 'Ground', 'free')
    smallVolierWater = ('Small', 'Water', 'free')
    middleVolierWater = ('Middle', 'Water', 'free')
    bigVolierWater = ('Big', 'Water', 'free')


class Volier(typeVolier):
    def init_volier(self, object):

        object.voliers.append(self.choose_volier())
        return object.voliers

    def choose_volier(self):
        i = input('type  ')
        g = int(input('size  '))
        if i == 'Ground':
            if g == 1:
                return typeVolier.smallVolierGround
            elif g == 2:
                return typeVolier.middleVolierGround
            elif g == 3:
                return typeVolier.bigVolierGround
        elif i == 'Water':
            if g == 1:
                return typeVolier.smallVolierWater
            elif g == 2:
                return typeVolier.middleVolierWater
            elif g == 3:
                return typeVolier.bigVolierWater

    def put_animal(self, object, volier):
        print(volier[0])
        if object.sizeA == volier[0][0]:
            return 'ok'


a = Zoo()
b = Volier()
c = Tiger()
d = b.init_volier(a)
print(b.put_animal(c, d))
