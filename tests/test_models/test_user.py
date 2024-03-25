import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def test_user_initialization(self):
        """
        Test case for initializing a User instance.
        """
        user = User(email="test@example.com", password="password123", first_name="John", last_name="Doe")
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_to_dict(self):
        """
        Test case for converting a User instance to a dictionary.
        """
        user = User(email="test@example.com", password="password123", first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")

    def test_user_str(self):
        """
        Test case for converting a User instance to a string.
        """
        user = User(email="test@example.com", password="password123", first_name="John", last_name="Doe")
        user_str = str(user)
        self.assertIsInstance(user_str, str)
        self.assertIn("User", user_str)
        self.assertIn(user.id, user_str)
        self.assertIn("email", user_str)
        self.assertIn("password", user_str)
        self.assertIn("first_name", user_str)
        self.assertIn("last_name", user_str)

if __name__ == '__main__':
    unittest.main()

