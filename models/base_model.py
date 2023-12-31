#!/usr/bin/python3
"""
This Module it the base module provides the base model for the web project
when it is initialised, id, created_at and updated are created

Usage:
>>> import from models.base_model import BaseModel

"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    the class of the base model
    """

    def __init__(self, *args, **kwargs):
        """
        function to initialize the class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'
                        )
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict_result = dict(self.__dict__)
        dict_result['__class__'] = self.__class__.__name__

        # covert created_at and updated_at to an ISO format
        dict_result['created_at'] = self.created_at.isoformat()
        dict_result['updated_at'] = self.updated_at.isoformat()
        return dict_result
