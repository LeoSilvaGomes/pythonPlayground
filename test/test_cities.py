from city_functions import get_city_country
import unittest

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        city_country = get_city_country('santiego', 'chile')
        self.assertEqual(city_country, 'Santiego Chile')

    def test_city_country_population(self):
        city_country_population = get_city_country('santiego', 'chile', '50000')
        self.assertEqual(city_country_population, 'Santiego Chile - populacao 50000')

unittest.main()