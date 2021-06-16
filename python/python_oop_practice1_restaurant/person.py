"""Module for class Person"""


class Person:
    """Class representing a person"""

    def __init__(self, name: str, last_name: str):
        """Constructor"""
        self.__name = name
        self.__last_name = last_name

    def get_name(self) -> str:
        """Returns first name of person"""
        return self.__name

    def get_last_name(self) -> str:
        """Returns second name of person"""
        return self.__last_name

    @property
    def get_full_name(self) -> str:
        """Returns full name of person"""
        return self.__name + ' ' + self.__last_name
