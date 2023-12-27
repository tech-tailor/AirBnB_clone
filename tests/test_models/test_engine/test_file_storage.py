#!/usr/bin/python3
""" test module for FileStorage class"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import datetime


class TestFileStorage(unittest.TestCase):
    """ test class for FileStorage"""

    def test_method_for_all(self):
        # create FileStorage instance with some objects
        storage = FileStorage()

        # test all method
        storage_dict = storage.all()
        self.assertIsInstance(storage_dict, dict)
        for obj in storage_dict.values():
            self.assertIsInstance(obj, BaseModel)
