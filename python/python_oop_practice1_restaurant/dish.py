"""Module for dish class"""


class Dish:
    """Class representing dish"""

    def __init__(self, name: str, ingredients: list, price: float, tax_percent: float):
        """Constructor"""
        self.__name = name
        self.__ingredients = ingredients
        self.__price = price
        self.__tax_percent = tax_percent

    def __str__(self):
        """Prints the dish"""
        return f'Name: {self.get_name()}\n' \
               f'Ingredients: {[product.get_name() for product in self.__ingredients]}\n' \
               f'Price: {self.get_price()}\n' \
               f'Tax percent: {self.get_tax_percent()}'

    def get_name(self) -> str:
        """Returns the name of dish"""
        return self.__name

    def get_ingredients(self) -> list:
        """Returns the list of ingredients for dish"""
        return self.__ingredients

    def get_price(self) -> float:
        """Returns the price of a dish"""
        return self.__price

    def get_final_price(self) -> float:
        """Returns the price of a dish including taxes"""
        return self.__price + self.__count_tax()

    def __count_tax(self) -> float:
        """Returns the sum of tax percent from price of a dish"""
        return self.__price * self.__tax_percent / 100

    def get_tax_percent(self) -> float:
        """Returns the tax percent of a dish"""
        return self.__tax_percent
