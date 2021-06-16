"""Module for order class"""
from customer import Customer


class Order:
    """Class representing order"""

    def __init__(self, customer: Customer, ordered_dishes: list):
        """Constructor"""
        self.__customer = customer
        self.__ordered_dishes = ordered_dishes
        self.__paid_sum = 0

    def __str__(self):
        """Prints the order"""
        return f'Customer: {self.__customer.get_full_name}\n' \
               f'Ordered dishes: {[product.get_name() for product in self.get_ordered_dishes()]}\n' \
               f'Paid sum: {self.get_paid_sum()}'

    def get_customer(self) -> str:
        """Returns the name of customer"""
        return self.__customer.get_full_name

    def get_ordered_dishes(self) -> list:
        """Returns the list of ordered dishes"""
        return self.__ordered_dishes

    def get_full_price(self) -> float:
        """Returns the full price for all dishes in an order"""
        return sum([dish.get_final_price() for dish in self.__ordered_dishes])

    def pay_for_order(self, value: float):
        """Sets the paid sum value"""
        self.__paid_sum = value

    def get_paid_sum(self) -> float:
        """Returns paid sum for order"""
        return self.__paid_sum
