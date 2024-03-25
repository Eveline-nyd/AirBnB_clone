#!/usr/bin/python3
import unittest
from datetime import datetime

from unittest.mock import patch

from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """
    Test cases for State class
    """
    def test_state_initialization(self):
        """
        Test case for initializing a State instance
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertEqual(state.created_at, state.updated_at)
        self.assertEqual(state.name, "")

    def test_state_name_attribute(self):
        """
        Test case for setting and getting the name attribute
        """
        state = State()
        state.name = "New York"
        self.assertEqual(state.name, "New York")

    def test_state_save_to_storage(self):
        """
        Test case for saving a State instance to storage
        """
        with patch('models.base_model.BaseModel.save_to_storage') as mock_save_to_storage:
            state = State(skip_save_to_storage=True)
            state.save_to_storage()
            mock_save_to_storage.assert_called_once()
    def test_state_to_dict(self):
        """
        Test case for converting a State instance to a dictionary
        """
        state = State()
        state.name = "New York"
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('__class__', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('name', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)
        self.assertEqual(state_dict['name'], "New York")

if __name__ == '__main__':
    unittest.main()
