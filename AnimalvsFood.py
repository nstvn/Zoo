class FoodType:
    Grass = ('Grass', 1, 5)
    Meat = ('Meat', 2, 10)


class Food(FoodType):
    def __init__(self, object):
        pass


class AnimalData:
    def __init__(self):
        self.name = ''
        self.type_food_eating = 0
        self.food_amount = 0
        self.price = 0
        self.habitat = ''


class Animal(AnimalData):
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    def choose_animal(self):
        print("Type an integer to choose an animal: \n1.Tiger \n2.Elephant \n3.Shark \n4.Wolf \n5.Jackal \n6.Giraffe \n7.Octopus \n")
        answer = input()
        answers = [str(i) for i in range(1, 8)]

        if answer in answers:
            if answer == '1':
                animal = Tiger()
            elif answer == '2':
                animal = Elephant()
            elif answer == '3':
                animal = Shark()
            elif answer == '4':
                animal = Wolf()
            elif answer == '5':
                animal = Jackal()
            elif answer == '6':
                animal = Giraffe()
            elif answer == '7':
                animal = Octopus()
            return animal
            
        else:
            print("Incorrect value! \n")
            pass


class Tiger(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Tiger'
        self.type_food_eating = FoodType.Meat
        self.food_amount = 10
        self.price = 100
        self.habitat = 'Ground'


class Elephant(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Elephant'
        self.type_food_eating = FoodType.Grass
        self.food_amount = 5
        self.price = 150
        self.habitat = 'Ground'


class Shark(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Shark'
        self.type_food_eating = FoodType.Meat
        self.food_amount = 15
        self.price = 200
        self.habitat = 'Water'


class Wolf(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Wolf'
        self.type_food_eating = FoodType.Meat
        self.food_amount = 5
        self.price = 1000
        self.habitat = 'Ground'


class Jackal():
    def __init__(self):
        super().__init__()
        self.name = 'Jackal'
        self.type_food_eating = FoodType.Meat
        self.food_amount = 3
        self.price = 50
        self.habitat = 'Ground'


class Giraffe():
    def __init__(self):
        super().__init__()
        self.name = 'Giraffe'
        self.type_food_eating = FoodType.Grass
        self.food_amount = 15
        self.price = 800
        self.habitat = 'Ground'


class Octopus():
    def __init__(self):
        super().__init__()
        self.name = 'Octopus'
        self.type_food_eating = FoodType.Meat
        self.food_amount = 15
        self.price = 500
        self.habitat = 'Water'
