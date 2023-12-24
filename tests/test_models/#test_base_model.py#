#!/usr/bin/python3

import unittest
from datetime import datetime
from uuid import UUID
from models.base_model import BaseModel


class TestBaseModelInitialization(unittest.TestCase):

    def test_initialization(self):
        model_instance = BaseModel()
        
        # check if the instance is created
        self.assertIsInstance(model_instance, BaseModel)

    def test_id_generation(self):
        model_instance1 = BaseModel()
        model_instance2 = BaseModel()

        # check if the id is unique
        self.assertNotEqual(model_instance1, model_instance2)

        #check if the id is a UUID4 type
        self.assertTrue(UUID(model_instance1.id, version=4), "Invalid uuid4")

    def created_at_and_updated_at(self):
        mode_instance = BaseModel()

        # check if the time is instance of datetime
        self.assertIsInstance(model_instance.created_at, datetime)
        self.assertIsInstance(model_instance.updated_at, datetime)

class String_Representation(unittest.TestCase):

    def test_str_representation(self):
        model_instance = BaseModel()

        #check if the string is generated
        str_representation = str(model_instance)
        self.assertIn(model_instance.__class__.__name__, str_representation)
        self.assertIn(model_instance.id, str_representation)
