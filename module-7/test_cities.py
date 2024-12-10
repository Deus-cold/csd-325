import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        """Test with city and country only."""
        result = city_country('tokyo', 'japan')
        self.assertEqual(result, 'Tokyo, Japan')


    def test_city_country_with_population(self):
        """Test with city, country, and population."""
        result = city_country('tokyo', 'japan', 13929286)
        self.assertEqual(result, 'Tokyo, Japan - population 13929286')

    def test_city_country_with_population_and_language(self):
        """Test with city, country, population, and language."""
        result = city_country('tokyo', 'japan', 13929286, 'japanese')
        self.assertEqual(result, 'Tokyo, Japan - population 13929286, Japanese')

    def test_city_country_with_language_only(self):
        """Test with city, country, and language(no population)."""
        result = city_country('tokyo', 'japan', language='japanese')
        self.assertEqual(result, 'Tokyo, Japan, Japanese')



if __name__ == '__main__':
    unittest.main()


