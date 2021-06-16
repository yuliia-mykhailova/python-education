"""Module for disease class"""


class Disease:
    """Class representing disease"""

    def __init__(self, name: str, forbidden_products: list):
        """Constructor"""
        self.__name = name
        self.__forbidden_products = forbidden_products

    def __str__(self):
        """Prints the disease"""
        return f'Name: {self.get_name()}\n' \
               f'Forbidden: {[product.get_name() for product in self.__forbidden_products]}'

    def get_name(self) -> str:
        """Returns the name of disease"""
        return self.__name

    def get_forbidden_products(self) -> list:
        """Returns the list of forbidden products for disease"""
        return self.__forbidden_products
