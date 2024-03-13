import pytest
import unittest

from main import add, divide, multiply, add_few_values, attraction, update_position

def test_add():
    result = add(number_one=1, number_two=4)
    assert result == 5

def test_sum_values():
    assert add_few_values(1, 2, 3, 4, 5) == 15  # 1 + 2 + 3 + 4 + 5 = 15
    assert add_few_values(10, 20, 30) == 60  # 10 + 20 + 30 = 60
    assert add_few_values(5, 5, 5, 5, 5, 5, 5) == 35  # 5 + 5 + 5 + 5 + 5 + 5 + 5 = 30
#This was never finished.
"""class TestAttraction(unittest.TestCase):

    def test_attraction_with_sun(self):
        # Create instances of AttractionClass or your class with the attraction method
        obj1 = attraction(x=0, y=0, mass=1, G=1)
        obj2 = attraction(x=3, y=4, mass=2, G=1, sun=True)

        force_x, force_y = obj1.attraction(obj2)

        # Assert that the distance to the sun is set correctly
        self.assertEqual(obj1.distance_to_sun, 5)

        # Add more assertions if needed based on your specific requirements

    def test_attraction_without_sun(self):
        # Create instances of AttractionClass or your class with the attraction method
        obj1 = attraction(x=0, y=0, mass=1, G=1)
        obj2 = attraction(x=3, y=4, mass=2, G=1, sun=False)

        force_x, force_y = obj1.attraction(obj2)

        # Assert that the distance to the sun is not set
        self.assertIsNone(obj1.distance_to_sun)

        # Add more assertions if needed based on your specific requirements

    # Add more test cases as needed"""