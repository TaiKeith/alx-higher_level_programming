#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Represent a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student"""
        if isinstance(attrs, list):
            my_list = list(filter(lambda x: x in attrs, self.__dict__))
            my_dict = {}
            for key in my_list:
                my_dict[key] = self.__dict__.get(key)
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces attributes of student"""
        for key, value in json.items()
            setattr(self, key, value)
