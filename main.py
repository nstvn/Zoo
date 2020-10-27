class Player:
    def __init__(self):
        money = 0
        level = 0
        zoo_rating = 0

class FoodType:
    Grass = ('Grass', 1, 5)
    Meat = ('Meat', 2, 10)

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
        self.hj = object[0]


    def str(self):
        str = self.hj
        return str


b = Food(AnimalData.Tiger)
print(b.str())