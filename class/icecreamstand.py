from restaurant import *

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        """Associando a classe pai"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate branco', 'limão', 'uva', 'blue ice', 'baunilha']

    def read_flavors(self):
        """Mostra os sabores da loja"""
        print("Os sabores disponiveis são: ")
        
        for flavor in self.flavors:
            print(flavor.title())