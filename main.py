import random
import time
from AnimalvsFood import *
from Volier import *


class Player:
    def __init__(self):
        self.money = 0
        self.level = 0


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


def main():
    c = Zoo()
    state = True
    while state:
        print("Type an integer to choose what you want to do: \n1. Information about zoo \n2. Voliers in the zoo \n3. Go to the shop \n4. Exit")
        mode = input()
        if mode == '1':
            pass
        elif mode == '2':
            pass
        elif mode == '3':
            pass
        elif mode == "4":
            print("Goodbye")
            state = False
        else:
            print("That is not a correct value. Try again \n")
            main()
        # print("Hello! Let's buy an animal to your new zoo")
        # animal = str(input("Do you want a Tiger or an Elephant? We don't have any other animals \n"))
        # if animal == 'Tiger':
        #     a = Tiger()
        # elif animal == 'Elephant':
        #     a = Elephant()
        # else:
        #     print('the name is wrong, try to start the program again')

        # b = Volier()

        # print("Let's buy a volier for the new animal. You can choose Ground or Water type")
        # while b.status == 'free':
        #     b.put_animal(a, b.init_volier(c))


if __name__ == '__main__':
    main()