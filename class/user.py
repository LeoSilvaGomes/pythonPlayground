from datetime import date

class User():

    def __init__(self, first_name, last_name, birthday, username):
        """Inicializa os atributos first_name, last_name, birthday, username"""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.username = username
        self.login_attempts = 0
        self.age = self.set_birthday()
    
    def describe_user(self):
        """Mostra uma resumo das informações do user"""
        print(self.username + " perfil:")
        print("Nome: " + self.first_name.title() + ' ' + self.last_name.title())
        print('Data de nascimento: ' + self.birthday)
        print('Idade: ' + str(self.age))

    def greet_user(self):
        """Mostra uma saudação para o user"""
        print('Bem-vindo ao meu sistema ' + self.username)

    def increment_login_attempts(self):
        """Incrementa em 1 a tentativa de login (login_attempts)"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reseta a tentativa de login (login_attempts)"""
        self.login_attempts = 0

    def set_birthday(self):
        day, month, year = self.birthday.split('/')
        current_date = date.today().strftime("%d/%m/%Y")
        current_day, current_month, current_year = current_date.split('/')

        current_day = int(current_day)
        current_month = int(current_month)
        current_year = int(current_year)
        day = int(day)
        month = int(month)
        year = int(year)

        if month > current_month or day > current_day:
            return (current_year - year - 1)
        else:
            return (current_year - year)
