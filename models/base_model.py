#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class definition
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.save_to_storage()

    def save_to_storage(self):
        """
        Saves the instance to the storage.
        """
        from models import storage
        if not hasattr(storage, 'new') or not hasattr(storage, 'save'):
            raise ImportError("Storage object does not required methods")
        storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Saves the instance.
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """
        Converts the instance to a dictionary.

        Returns:
            Dictionary representing the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
