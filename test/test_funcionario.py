import unittest
from funcionario import *

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.my_survey = Employee('Leo', 'Gomes', 15000)

    def test_give_default_raise(self):
        self.my_survey.give_raise()
        self.assertEqual(20000, self.my_survey.salary)
        
    def test_give_custom_raise(self):
        self.my_survey.give_raise(7000)
        self.assertEqual(22000, self.my_survey.salary)

unittest.main()