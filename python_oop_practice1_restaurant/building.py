"""Module for class Building"""


class Building:
    """Class representing a building"""

    def __init__(self, name: str, address: str):
        """Constructor"""
        self.__name = name
        self.__address = address

    def get_name(self) -> str:
        """Returns first name of building"""
        return self.__name

    def get_address(self) -> str:
        """Returns second name of address"""
        return self.__address
