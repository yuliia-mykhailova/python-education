"""Module for class Restaurant"""
from building import Building


class Restaurant(Building):
    """Class representing a restaurant"""

    def __init__(self, name: str, address: str):
        """Constructor"""
        Building.__init__(self, name, address)
        self.__menu = []
        self.__orders = []
        self.__waiters = []

    def __str__(self):
        """Prints the restaurant"""
        return f'Name: {self.get_name()}\n' \
               f'Address: {self.get_address()}'

    @property
    def menu(self) -> list:
        """Returns the menu of restaurant"""
        return self.__menu

    @menu.setter
    def menu(self, value: list):
        """Sets menu of restaurant"""
        self.__menu = value

    @property
    def orders(self) -> list:
        """Returns the list of orders"""
        return self.__orders

    @orders.setter
    def orders(self, value: list):
        """Sets the list of orders in a restaurant"""
        self.__orders = value

    @property
    def waiters(self) -> list:
        """Returns the list of waiters"""
        return self.__waiters

    @waiters.setter
    def waiters(self, value: list):
        """Sets the list of waiters in a restaurant"""
        self.__waiters = value

