
class Employee():

    def __init__(self, first_name, last_name, salary):
        '''Inicializando a class Employee com o infos basicas'''
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary=5000):
        self.salary += salary

