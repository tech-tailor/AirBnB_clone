#!/usr/bin/python3
"""
This module for file storage
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    this class stores json files
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ serializes __objects to json file."""
        serialize_data = {}
        for key, obj in self.__objects.items():
            serialize_data[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialize_data, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                json_dict = json.load(file)

            for value in json_dict.values():
                obj_class = value['__class__']
                self.new(eval('{}({})'.format(obj_class, '**value')))
        except FileNotFoundError:
            pass
