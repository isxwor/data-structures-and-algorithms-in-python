''' R-2.4
Write a Python class, Flower, that has three instance variables of type str, int,
and ﬂoat, that respectively represent the name of the ﬂower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
'''

class Flower:
    ''' Initializing Flower class '''
    def __init__(self, name, petals, price):
        self.__name = str(name)
        self.__petals = int(petals)
        self.__price = float(price)
    
    @property
    def name(self):
        ''' Returns name '''
        return self.__name
    
    @name.setter
    def name(self, new_name):
        ''' Sets name '''
        self.__name = str(new_name)
    
    @property
    def no_of_petals(self):
        ''' Returns number of petals '''
        return self.__petals
    
    @no_of_petals.setter
    def no_of_petals(self, new_petals):
        ''' Sets number of petals '''
        self.__petals = int(new_petals)
    
    @property
    def price(self):
        ''' Returns price '''
        return self.__price
    
    @price.setter
    def price(self, new_price):
        ''' Sets price '''
        self.__price = float(new_price)


if __name__ == '__main__':
    # ------ [ Tests ] ------
    flowers = []
    flowers.append(Flower('Rose', 25, 40))
    flowers.append(Flower('Jasmine', 9, 35))
    
    for flower in flowers:
        print(f'{flower.name}, {flower.no_of_petals}, {flower.price}')
    
    changes = {
        'one': {
            'name': 'Red rose',
            'petals': 20,
            'price': 50,
        },
        'two': {
            'name': 'Sunflower',
            'petals': 80,
            'price': 30,
        },
    }
    
    print('\n[ Changing values with setters ]')
    for i, key in enumerate(changes):
        flowers[i].name = changes[key]['name']
        flowers[i].no_of_petals = changes[key]['petals']
        flowers[i].price = changes[key]['price']
    for flower in flowers:
        print(f'{flower.name}, {flower.no_of_petals}, {flower.price}')
