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

    def chek_money(self, price):
        if self.money - price < 0:
            print('You dont have enough money!!!')
            return False
        elif self.money - price >= 0:
            self.money -= price
            return True


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
        print(
            f'Level: {zoo.level} \nMoney: {zoo.money} \nAmount of voliers: {len(zoo.voliers)} \nAmount of animals: {zoo.animals_amount} \n'
            f'Max amount of visitors: {zoo.max_visitors} \n')
        cycle(zoo=zoo)
        # zoo.money += 100

    elif mode == '2':
        print("Here is a list of all of your voliers: \n")
        for volier in zoo.voliers:
            print(f'{volier.habitat} volier: {volier.status}')
        # zoo.money += 100

    elif mode == '3':
        choose = input("What do you want buy? Volier(1) or animal(2): ")

        if choose == '1':
            volier = Volier()
            volier.choose_volier(zoo)
            # zoo.money += 100

        elif choose == '2':
            animal = Animal()
            animal = animal.choose_animal()
            print(f"Animal price is {animal.price}. y - yes, n - no: ")
            
            answer = input()
            if answer == 'y':
                print("You need a suitable volier for the animal. Let's choose one of yours")
                free_voliers = []
                for volier in zoo.voliers:
                    if volier.status == 'free':
                        free_voliers.append(volier)
                for i in range(0, len(free_voliers)):
                    print(f'{i + 1}.{free_voliers[i].habitat}')
                number = input()
                free_voliers[int(number) - 1].put_animal(animal, free_voliers[int(number) - 1], zoo, animal.price)
            if answer == 'n':
                pass
        # zoo.money += 100
    elif mode == '4':
        print("Goodbye")
        exit()
    else:
        print("That is not a correct value. Try again \n")
        cycle(zoo=zoo)


def main():
    zoo = Zoo()
    print("Hello, this is your new zoo. Your level is 0, and you are given 1000$ for starting")

    while True:
        cycle(zoo=zoo)


if __name__ == '__main__':
    main()
