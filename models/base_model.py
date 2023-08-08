#!usr/bin/python3
"""Defines the BaseModel class"""

from models import storage
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Represents the Base class of the project."""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """Return string representation of BaseModel instance."""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """Updates attribute updated_at with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
