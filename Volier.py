# class typeVolier:
#     smallVolierGround = ('Small', 'Ground', 'free')
#     middleVolierGround = ('Middle', 'Ground', 'free')
#     bigVolierGround = ('Big', 'Ground', 'free')
#     smallVolierWater = ('Small', 'Water', 'free')
#     middleVolierWater = ('Middle', 'Water', 'free')
#     bigVolierWater = ('Big', 'Water', 'free')


class Volier:
    def __init__(self):
        self.habitat = 0
        self.sizeV = 0
        self.status = 'free'

    def init_volier(self, object):
        object.voliers.append(self.choose_volier())
        return self

    def choose_volier(self):
        type_of_volier = input('type  ')
        size_of_volier = int(input('size 1 if you want a small volier, size 2 for middle, and 3 for big '))
        if type_of_volier == 'Ground':
            if size_of_volier == 1:
                self.sizeV, self.habitat, self.status = smallGroundVolier.str(self)
                return self
            elif size_of_volier == 2:
                self.sizeV, self.habitat, self.status = middleGroundVolier.str(self)
                return self
            elif size_of_volier == 3:
                self.sizeV, self.habitat, self.status = bigGroundVolier.str(self)
                return self
        elif type_of_volier == 'Water':
            if size_of_volier == 1:
                self.sizeV, self.habitat, self.status = smallWaterVolier.str(self)
                return self
            elif size_of_volier == 2:
                self.sizeV, self.habitat, self.status = middleWaterVolier.str(self)
                return self
            elif size_of_volier == 3:
                self.sizeV, self.habitat, self.status = bigWaterVolier.str(self)
                return self

    def put_animal(self, object, volier):
        if object.habitat == volier.habitat:
            if object.sizeA == volier.sizeV:
                print('the animal is in the volier now')
                volier.status = object
            else:
                print('it is not suitable for your animal, try again')
        else:
            print('it is not suitable for your animal, try again')


class smallGroundVolier(Volier):
    def str(self):
        self.habitat = 'Ground'
        self.sizeV = 'Small'
        return self.sizeV, self.habitat, self.status


class smallWaterVolier(Volier):
    def str(self):
        self.habitat = 'Water'
        self.sizeV = 'Small'
        return self.sizeV, self.habitat, self.status


class middleGroundVolier(Volier):
    def str(self):
        self.habitat = 'Ground'
        self.sizeV = 'Middle'
        return self.sizeV, self.habitat, self.status


class middleWaterVolier(Volier):
    def str(self):
        self.habitat = 'Water'
        self.sizeV = 'Middle'
        return self.sizeV, self.habitat, self.status


class bigGroundVolier(Volier):
    def str(self):
        self.habitat = 'Ground'
        self.sizeV = 'Big'
        return self.sizeV, self.habitat, self.status


class bigWaterVolier(Volier):
    def str(self):
        self.habitat = 'Water'
        self.sizeV = 'Big'
        return self.sizeV, self.habitat, self.status
