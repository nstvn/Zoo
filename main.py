class Player:
    def __init__(self):
        money = 0
        level = 0
        zoo_rating = 0


class Food:
    def __init__(self):
        pass


class FoodType:
    def __init__(self, type='', rare=0, time=1):
        self.rare = rare
        self.type = type
        self.time = time

    def grass(self):
        self.type = 'Grass'
        self.rare = 1
        self.time = 5

    def meat(self):
        self.type = 'Meat'
        self.rare = 2
        self.time = 10
