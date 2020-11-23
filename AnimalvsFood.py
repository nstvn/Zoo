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
        self.sizeA = ''
        self.food_amount = 0
        self.rare = 0
        self.habitat = ''


class Animal(AnimalData):
    def __init__(self):
        pass


class Tiger(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Tiger'
        self.type_food_eating = FoodType.Meat
        self.sizeA = 'Middle'
        self.food_amount = 10
        self.rare = 5
        self.habitat = 'Ground'


class Elephant(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Elephant'
        self.type_food_eating = FoodType.Grass
        self.sizeA = 'Big'
        self.food_amount = 5
        self.rare = 3
        self.habitat = 'Ground'
