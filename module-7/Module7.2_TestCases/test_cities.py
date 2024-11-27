#Usiel Figueroa
#Module 7.2Assignment: Test Cases
# CSD325 - A311 Advanced Python
# November 26, 2024

# References
# (n.d.). Unittest — Unit testing framework. Python. Retrieved November 18, 2024, from https://docs.python.org/3/library/unittest.html
# Matthes, E. (2019). Python crash course : a hands-on, project-based introduction to programming (2nd edition.). No Starch Press.




# test_cities.py

import unittest
from city_functions import city_country


class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        """Test the function with city and country."""
        self.assertEqual(city_country("Santiago", "Chile"), "Santiago, Chile")

    def test_city_country_population(self):
        """Test the function with city, country, and population."""
        self.assertEqual(city_country("Tokyo", "Japan", 13929286), "Tokyo, Japan - population 13929286")

    def test_city_country_population_language(self):
        """Test the function with city, country, population, and language."""
        self.assertEqual(city_country("Paris", "France", 2161000, "French"),
                         "Paris, France - population 2161000, French")


if __name__ == "__main__":
    unittest.main()
