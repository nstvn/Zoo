class Player:
    def __init__(self):
        money = 0
        level = 0
        zoo_rating = 0


class Food:
    def __init__(self, type_food):
        type_food = grass
        self.food_type = FoodType()
        self.type, self.rare, self.time = self.food_type.type_food()


class FoodType:
    def __init__(self, type='', rare=0, time=1):
        self.rare = rare
        self.type = type
        self.time = time

    def grass(self):
        self.type = 'Grass'
        self.rare = 1
        self.time = 5
        return self.type, self.rare, self.time

    def meat(self):
        self.type = 'Meat'
        self.rare = 2
        self.time = 10


a = Food()
print(a.type)