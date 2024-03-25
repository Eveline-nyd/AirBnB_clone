#!/usr/bin/python3
import unittest
from datetime import datetime
from unittest.mock import MagicMock
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class
    """

    def test_place_initialization(self):
        """
        Test case for initializing a Place instance
        """
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertEqual(place.created_at, place.updated_at)

    def test_place_custom_values(self):
        """
        Test case for initializing a Place instance with custom values
        """
        custom_values = {
            'city_id': '123',
            'user_id': '456',
            'name': 'Test Place',
            'description': 'A test place',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 37.7749,
            'longitude': -122.4194,
            'amenity_ids': ['1', '2', '3']
        }
        place = Place(**custom_values)
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
        for key, value in custom_values.items():
            self.assertEqual(getattr(place, key), value)

    def test_place_to_dict(self):
        """
        Test case for converting a Place instance to a dictionary
        """
        place = Place(city_id='123', user_id='456', name='Test Place')
        _ = place.created_at
        _ = place.updated_at
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn('__class__', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

    # def test_place_save_to_storage(self):
    #     """
    #     Test case for saving a Place instance to storage
    #     """
    #     from models import storage
    #     storage.new = MagicMock()
    #     place = Place()
    #     place.save_to_storage()
    #     storage.new.assert_called_once_with(place)

    def test_place_save(self):
        """
        Test case for saving a Place instance
        """
        place = Place()
        place.save()
        self.assertGreater(place.updated_at, place.created_at)

if __name__ == '__main__':
    unittest.main()
