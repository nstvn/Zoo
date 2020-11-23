# class typeVolier:
#     smallVolierGround = ('Small', 'Ground', 'free')
#     middleVolierGround = ('Middle', 'Ground', 'free')
#     bigVolierGround = ('Big', 'Ground', 'free')
#     smallVolierWater = ('Small', 'Water', 'free')
#     middleVolierWater = ('Middle', 'Water', 'free')
#     bigVolierWater = ('Big', 'Water', 'free')

import main

class Volier:
    def __init__(self):
        self.habitat = 0
        self.status = 'free'

    def init_volier(self, object):
        object.voliers.append(self.choose_volier())
        return self

    def choose_volier(self, zoo):
        type_of_volier = input('type Ground(1) or Water(2)  ')
        if type_of_volier == '1':
            print('ground volier-price: 100')
            choose = input('y-yes, n-no')
            if choose == 'y':
                zoo.money -= 100
            elif choose == 'n':
                pass
            self.habitat, self.status = GroundVolier.str(self)
            return self
        elif type_of_volier == '2':
            print('water volier-price: 300')
            choose = input('y-yes, n-no')
            if choose == 'y':
                zoo.money -= 300
            elif choose == 'n':
                pass
            self.habitat, self.status = WaterVolier.str(self)
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


class GroundVolier(Volier):
    def str(self):
        self.habitat = 'Ground'
        return self.habitat, self.status


class WaterVolier(Volier):
    def str(self):
        self.habitat = 'Water'
        return self.habitat, self.status