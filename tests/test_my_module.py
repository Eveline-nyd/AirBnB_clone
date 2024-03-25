# File: test_module.py

import unittest
import os
from datetime import datetime
from module import BaseModel, FileStorage

class TestBaseModel(unittest.TestCase):

    def test_base_model_init(self):
        model = BaseModel()
        self.assertIsNone(model.id)
        self.assertIsNone(model.created_at)
        self.assertIsNone(model.updated_at)

    def test_base_model_save(self):
        model = BaseModel()
        model.save()
        self.assertIsNotNone(model.updated_at)

    def test_base_model_str(self):
        model = BaseModel()
        self.assertEqual(str(model), "{}".format(model.__dict__))

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.test_file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.test_file_path

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_file_storage_all(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.assertEqual(len(self.storage.all()), 2)

    def test_file_storage_save(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.test_file_path))

    def test_file_storage_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(len(new_storage.all()), 1)
        self.assertEqual(new_storage.all()["BaseModel.{}".format(obj.id)].__dict__, obj.__dict__)

if __name__ == '__main__':
    unittest.main()

