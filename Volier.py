class Volier:
    def __init__(self):
        self.habitat = 0
        self.status = 'free'

    def choose_volier(self, zoo):
        type_of_volier = input('type Ground(1) or Water(2)  ')

        if type_of_volier == '1':
            print('ground volier-price: 100')
            choose = input('y-yes, n-no: ')
            if choose == 'y':
                zoo.chek_money(100)
                self.habitat, self.status = GroundVolier.str(self)
                zoo.voliers.append(self)
            elif choose == 'n':
                pass
            

        elif type_of_volier == '2':
            print('water volier-price: 300')
            choose = input('y-yes, n-no: ')
            if choose == 'y':
                zoo.chek_money(300)
                self.habitat, self.status = WaterVolier.str(self)
                zoo.voliers.append(self)
            elif choose == 'n':
                pass
            

    def put_animal(self, object, volier, zoo, price):
        if object.habitat == volier.habitat:
            if zoo.chek_money(price):
                print('the animal is in the volier now')
                volier.status = object
                zoo.animals_amount += 1
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
