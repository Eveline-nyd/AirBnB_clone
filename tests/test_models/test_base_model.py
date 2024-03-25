#!/usr/bin/python3
import unittest
from datetime import datetime
from unittest.mock import MagicMock
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """
    def test_base_model_default_values(self):
        """
        Test case for checking default attribute values
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertEqual(base_model.created_at, base_model.updated_at)

    def test_base_model_custom_values(self):
        """
        Test case for custom attribute values
        """
        custom_values = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00.000',
            'updated_at': '2022-01-02T00:00:00.000',
            'custom_attr': 'custom value'
        }
        base_model = BaseModel(**custom_values)
        self.assertIsInstance(base_model, BaseModel)
        self.assertEqual(base_model.id, '123')
        self.assertEqual(base_model.created_at, datetime(2022, 1, 1, 0, 0, 0))
        self.assertEqual(base_model.updated_at, datetime(2022, 1, 2, 0, 0, 0))
        self.assertEqual(base_model.custom_attr, 'custom value')

    def test_base_model_save_to_storage(self):
        """
        Test case for saving instance to storage
        """
        from models import storage
        storage.new = MagicMock()
        base_model = BaseModel()
        storage.new.assert_called_once_with(base_model)

    def test_base_model_update_and_save(self):
        """
        Test case for updating and saving instance
        """
        base_model = BaseModel()
        base_model.save()
        self.assertGreater(base_model.updated_at, base_model.created_at)

    def test_base_model_to_dict(self):
        """
        Test case for converting instance to dictionary
        """
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()

        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('__class__', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
