#!/usr/bin/python3
""" initialization test"""

from models.engine.file_storage import FileStorage
import unittest


class TestInitialization(unittest.TestCase):
    """class for init test"""


    def test_storage(self):
        storage_instance = FileStorage

        self.assertIsInstance(storage_instance, FileStorage)

    def test_reload_method(self):
        storage_instance = FileStorage
        with open(self.test_file_path, 'w') as file:
            file.write("test")
        self.assertEqual(test_file_path, "test")
