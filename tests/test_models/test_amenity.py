import unittest
from unittest.mock import patch
from datetime import datetime

from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.amenity = Amenity()

    def test_init(self):
        """
        Test the initialization of an Amenity instance.
        """
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_name_attribute(self):
        """
        Test setting and getting the name attribute.
        """
        self.amenity.name = "Complimentary WiFi"
        self.assertEqual(self.amenity.name, "Complimentary WiFi")

    def test_save_to_storage(self):
        """
        Test saving an Amenity instance to storage.
        """
        with patch('models.base_model.BaseModel.save_to_storage') as mock_save:
            self.amenity.save_to_storage()
            mock_save.assert_called_once()

    def test_save(self):
        """
        Test saving an Amenity instance.
        """
        with patch('models.base_model.BaseModel.save') as mock_save:
            self.amenity.save()
            mock_save.assert_called_once()

    def test_to_dict(self):
        """
        Test converting an Amenity instance to a dictionary.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('__class__', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()