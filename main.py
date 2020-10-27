import random
from AnimalvsFood import *
from Volier import *
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


a = Zoo()
b = Volier()
c = Tiger()
print(b.put_animal(c,b.init_volier(a)))
