#!/usr/bin/python3
"""
This module contains class Base
"""
import json


class Base:
    """Represents the base model.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method
        Returns:
            the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list): List of instances who inherits of Base
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(Base.to_json_string(json_string))

    @staticmethod
    def from_json_string(json_string):
        """
        Static method
        Returns:
            the list of the JSON string representation
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method
        Args:
            **dictionary (dict): key/value pairs
        Returns:
            an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    def load_from_file(cls):
        """
        Class method
        Returns:
            a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            pass
        return []
