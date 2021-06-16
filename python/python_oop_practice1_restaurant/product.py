"""Module for product class"""


class Product:
    """Class representing product"""

    def __init__(self, name: str):
        """Constructor"""
        self.__name = name

    def __str__(self):
        """Prints the product"""
        return self.get_name()

    def get_name(self) -> str:
        """Returns the name of disease"""
        return self.__name
