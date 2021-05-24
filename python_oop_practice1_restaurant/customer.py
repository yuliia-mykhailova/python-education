"""Module for class Customer"""
from person import Person
from restaurant import Restaurant


class Customer(Person):
    """Class representing a customer"""

    def __init__(self, name: str, last_name: str, email: str, diseases: list):
        """Constructor"""
        Person.__init__(self, name, last_name)
        self.__email = email
        self.__diseases = diseases

    def __str__(self):
        """Prints the customer"""
        return f'Full name: {self.get_full_name}\n' \
               f'Email: {self.get_email()}'

    def get_email(self) -> str:
        """Returns email of customer"""
        return self.__email

    def __unpack_disease(self) -> list:
        """Returns all products of each disease of customer"""
        result = []
        for products in self.__diseases:
            result += products.get_forbidden_products()
        return result

    def get_personal_menu(self, restaurant: Restaurant) -> list:
        """Returns dishes that customer can eat, based on diseases"""
        result = []
        products_disease = self.__unpack_disease()
        for dish in restaurant.menu:
            if set(dish.get_ingredients()).intersection(set(products_disease)):
                continue
            result.append(dish)
        return result
