#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    """
    Test cases for City class
    """
    def test_city_default_values(self):
        """
        Test case for checking default attribute values
        """
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertEqual(city.created_at, city.updated_at)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_custom_values(self):
        """
        Test case for custom attribute values
        """
        custom_values = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00.000',
            'updated_at': '2022-01-02T00:00:00.000',
            'state_id': '456',
            'name': 'Test City'
        }
        city = City(**custom_values)
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertEqual(city.id, '123')
        self.assertEqual(city.created_at, datetime(2022, 1, 1, 0, 0, 0))
        self.assertEqual(city.updated_at, datetime(2022, 1, 2, 0, 0, 0))
        self.assertEqual(city.state_id, '456')
        self.assertEqual(city.name, 'Test City')

    def test_city_to_string(self):
        """
        Test case for converting instance to string
        """
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertIsInstance(city.__str__(), str)
        self.assertEqual(city.__str__(), f"[City] ({city.id}) {city.__dict__}")

    def test_city_to_dict(self):
        """
        Test case for converting instance to dictionary
        """
        city = City()
        city_dict = city.to_dict()

        self.assertIsInstance(city_dict, dict)
        self.assertIn('__class__', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)
        self.assertEqual(city_dict['state_id'], "")
        self.assertEqual(city_dict['name'], "")

if __name__ == '__main__':
    unittest.main()
