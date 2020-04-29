class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos name and cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.restaurant_open = 0
        self.number_served = 0

    def describe_restaurant(self):
        """Mostra uma mensagem de descrição do restaurante"""
        print("O restaurante " + self.restaurant_name + " tem uma das melhores cozinhas já vistas, a cozinha " 
        + self.cuisine_type)

    def status_restaurant(self):
        """Mostra se o restaurante está a aberto ou não"""
        if self.restaurant_open:
            print("O restaurante " + self.restaurant_name + " está aberto")

        else:
            print("O restaurante " + self.restaurant_name + " está fechado")

    def open_restaurant(self):
        """Abre o restaurante"""
        if not self.restaurant_open:
            self.restaurant_open = 1
        else :
            print("O restaurente já está aberto")

    def close_restaurant(self):
        """Fecha o restautante"""
        if self.restaurant_open:
            self.restaurant_open = 0
        else :
            print("O restaurante já está fechado")

    def read_number_served(self):
        """Mostra o numero de pessoas que foram servidas"""
        print("O restaurante serviu " + str(self.number_served) + " de clientes")

    def set_number_served(self, number):
        """Muda o valor de pessoas servidas"""
        self.number_served = number

    def increment_number_served(self):
        self.number_served += 1