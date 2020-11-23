import random
import time
import math
from AnimalvsFood import *
from Volier import *


class Zoo:
    def __init__(self):
        self.money = 1000
        self.level = 0
        self.voliers = []
        self.animals_amount = 0
        self.max_visitors = 1


class VisitorData:
    Child = frozenset(i for i in range(1, 7))
    Adult = frozenset(i for i in range(7, 50))
    Old = frozenset(i for i in range(50, 110))


class Visitor(VisitorData):
    def __init__(self):
        age = random.randint(1, 60)
        if age in VisitorData.Child:
            self.ticket_price = 0
        elif age in VisitorData.Adult:
            self.ticket_price = 100
        elif age in VisitorData.Old:
            self.ticket_price = 50


def cycle(zoo):
    zoo.level = math.floor((len(zoo.voliers) + zoo.animals_amount) / 2)
    zoo.max_visitors = zoo.level * 10
    print(
        "Type an integer to choose what you want to do: \n1. Information about zoo \n2. Voliers in the zoo \n3. Go to the shop \n4. Exit")
    mode = input()
    if mode == '1':
        print(f'Level: {zoo.level} \nMoney: {zoo.money} \nAmount of voliers: {len(zoo.voliers)} \nAmount of animals: {zoo.animals_amount} \n'
              f'Max amount of visitors: {zoo.max_visitors} \n')
        cycle(zoo=zoo)
    elif mode == '2':
        for volier in zoo.voliers:
            print(f'{volier.habitat} volier: {volier.status.name}')
    elif mode == '3':
        return True
    elif mode == '4':
        print("Goodbye")
        exit()
    else:
        print("That is not a correct value. Try again \n")
        cycle(zoo=zoo)


def main():
    zoo = Zoo()
    print("Hello, this is your new zoo. Your level is 1, and you are given 1000$ for starting")

    animal = str(input("Do you want a Tiger or an Elephant? We don't have any other animals \n"))
    if animal == 'Tiger':
        a = Tiger()
    elif animal == 'Elephant':
        a = Elephant()
    else:
        print('the name is wrong, try to start the program again')

    b = Volier()

    print("Let's buy a volier for the new animal. You can choose Ground or Water type")
    while b.status == 'free':
        b.put_animal(a, b.init_volier(zoo))

    while True:
        cycle(zoo=zoo)


if __name__ == '__main__':
    main()
