class Volier:
    def __init__(self):
        self.habitat = 0
        self.status = 'free'

    def choose_volier(self, zoo):
        type_of_volier = input('Choose type: Ground(1) or Water(2)  ')

        if type_of_volier == '1':
            print('Ground volier - price: 100 \n')
            choose = input('y - yes, n - no: ')
            if choose == 'y':
                zoo.check_money(100)
                self.habitat, self.status = GroundVolier.str(self)
                zoo.voliers.append(self)
            elif choose == 'n':
                pass
            else:
                print("Incorrect value! \n")
                pass
            
        elif type_of_volier == '2':
            print('Water volier - price: 300 \n')
            choose = input('y - yes, n - no: ')
            if choose == 'y':
                zoo.check_money(300)
                self.habitat, self.status = WaterVolier.str(self)
                zoo.voliers.append(self)
            elif choose == 'n':
                pass
            else:
                print("Incorrect value! \n")
                pass

        else:
            print("Incorrect value! \n")
            pass
            

    def put_animal(self, animal, volier, zoo, price):
        if animal.habitat == volier.habitat:
            if zoo.check_money(price):
                print('The animal is in the volier now \n')
                volier.status = animal
                zoo.animals_amount += 1
        else:
            print('It is not suitable for your animal, try again \n')


class GroundVolier(Volier):
    def str(self):
        self.habitat = 'Ground'
        return self.habitat, self.status


class WaterVolier(Volier):
    def str(self):
        self.habitat = 'Water'
        return self.habitat, self.status
