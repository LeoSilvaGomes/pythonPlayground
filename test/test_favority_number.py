import unittest
from favority_number import open_favority_number

class NumberTestCase(unittest.TestCase):
    '''Testes para a funcao open_favority_number'''

    def test_number(self):
        '''Numero 3 funciona?'''
        number = open_favority_number()
        self.assertEqual(number, '4')

unittest.main()