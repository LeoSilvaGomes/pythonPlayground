from user import *
from privileges import Privileges

class Admin(User):

    def __init__(self, first_name, last_name, birthday, username):
        """Associando a classe pai"""
        super().__init__(first_name, last_name, birthday, username)
        self.privileges = Privileges()