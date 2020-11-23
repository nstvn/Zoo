class FoodType:
    Grass = ('Grass', 1, 5)
    Meat = ('Meat', 2, 10)


class Food(FoodType):
    def __init__(self, object):
        pass


class AnimalData:
    # type_food_eating = ("Grass", 'Meat')
    # sizeA = ('Small', "Middle", "Big")
    # food_amount = (5, 10, 15)
    # rare = (1, 2, 3, 4, 5)
    # habitat = ('Water', 'Ground')
    # Tiger = {'type_food': FoodType.Meat, 'sizeA': 'Middle', 'food_amount': 10, 'rare': 5, 'habitat': 'Ground'}
    # Elephant = {'type_food': FoodType.Grass, 'sizeA': 'Big', 'food_amount': 5, 'rare': 3, 'habitat': 'Ground'}

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
        print("Type an integer to choose an animal: \n1.Tiger \n2.Elephant \n3.Shark \n4.Wolf \n")
        answer = input()
        if answer == '1':
            animal = Tiger()
        elif answer == '2':
            animal = Elephant()
        elif answer == '3':
            animal = Shark()
        elif answer == '4':
            animal = Wolf()
        return animal


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
        self.price = 1050
        self.habitat = 'Ground'
