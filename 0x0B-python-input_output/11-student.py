#!/usr/bin/python3
""" Module containing the class """


class Student:
    """ Definition of the class student """

    def __init__(self, first_name, last_name, age):
        """ initializes new object from the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        if type(attrs) is not list or \
           not all(type(attr) == str for attr in attrs):
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs \
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for key, value in json.items():
            setattr(self, key, value)
