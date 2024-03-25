# test_review.py
import unittest
from datetime import datetime
from unittest.mock import MagicMock
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """
    def test_review_initialization(self):
        """
        Test case for initializing a Review instance.
        """
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertEqual(review.created_at, review.updated_at)

    def test_review_attributes(self):
        """
        Test case for setting and getting attributes of a Review instance.
        """
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great place!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great place!")

    def test_review_to_dict(self):
        """
        Test case for converting a Review instance to a dictionary.
        """
        review = Review(place_id="123", user_id="456", text="Great place!")
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn('__class__', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('place_id', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('text', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)
        self.assertEqual(review_dict['place_id'], "123")
        self.assertEqual(review_dict['user_id'], "456")
        self.assertEqual(review_dict['text'], "Great place!")

    # def test_review_save_to_storage(self):
    #     """
    #     Test case for saving a Review instance to storage.
    #     """
    #     from models import storage
    #     storage.new = MagicMock()
    #     review = Review()
    #     review.save_to_storage()
    #     storage.new.assert_called_once_with(review)

    def test_review_save(self):
        """
        Test case for saving a Review instance.
        """
        review = Review()
        review.save()
        self.assertGreater(review.updated_at, review.created_at)

if __name__ == '__main__':
    unittest.main()
