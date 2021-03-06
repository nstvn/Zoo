import random
import time
import math
import threading
from AnimalvsFood import *
from Volier import *


class Zoo:
    def __init__(self):
        self.money = 1000
        self.level = 0
        self.voliers = []
        self.animals_amount = 0
        self.max_visitors = 1

    def check_money(self, price):
        if self.money - price < 0:
            print("You don't have enough money!!! \n")
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
    print()
    print(
        "Type an integer to choose what you want to do: \n1. Information about zoo \n2. Voliers in the zoo \n3. Go to the shop \n4. Exit \n")
    mode = input()
    if mode == '1':
        print(
            f'Level: {zoo.level} \nMoney: {zoo.money} (+{zoo.max_visitors * 5}/min) \nAmount of voliers: {len(zoo.voliers)} \nAmount of animals: {zoo.animals_amount} \n'
            f'Max amount of visitors: {zoo.max_visitors} \n')
        cycle(zoo=zoo)

    elif mode == '2':
        if len(zoo.voliers) == 0:
            print("You don't have any voliers yet :( \n")
        else:
            print("Here is a list of all of your voliers: \n")
            for volier in zoo.voliers:
                print(f'{volier.habitat} volier: {volier.status}')
            print()

    elif mode == '3':
        choose = input("What do you want buy? Volier(1) or animal(2): ")

        if choose == '1':
            volier = Volier()
            volier.choose_volier(zoo)

        elif choose == '2':
            animal = Animal()
            animal = animal.choose_animal()
            try:
                print(f"Animal price is {animal.price}. y - yes, n - no: ")
            except AttributeError:
                cycle(zoo=zoo)
            
            answer = input()
            if answer == 'y':
                if zoo.check_money(animal.price):
                    print("You need a suitable volier for the animal. Let's choose one of yours \n")
                    free_voliers = []
                    for volier in zoo.voliers:
                        if volier.status == 'free':
                            free_voliers.append(volier)
                    if len(free_voliers) == 0:
                        print("You don't have any free voliers for the animal! \n")
                        pass
                    else:
                        for i in range(0, len(free_voliers)):
                            print(f'{i + 1}.{free_voliers[i].habitat}')
                        print()
                        number = input()
                        try:
                            free_voliers[int(number) - 1].put_animal(animal, free_voliers[int(number) - 1], zoo, animal.price)
                        except Exception:
                            print("Incorrect value! \n")
                            pass
                else:
                    pass
            if answer == 'n':
                pass
        
    elif mode == '4':
        print("Goodbye")
        exit()

    else:
        print("That is not a correct value. Try again \n")
        cycle(zoo=zoo)


def add_money(zoo):
    while True:
        zoo.money += (zoo.max_visitors * 10)
        time.sleep(120)


def work_zoo(zoo):
    while True:
        cycle(zoo=zoo)


def main():
    zoo = Zoo()
    print("Hello, this is your new zoo. Your level is 0, and you are given 1010$ for starting")

    thread1 = threading.Thread(target=work_zoo, args=(zoo,))
    thread2 = threading.Thread(target=add_money, args=(zoo,))
    thread2.start()
    thread1.start()
    

if __name__ == '__main__':
    main()
