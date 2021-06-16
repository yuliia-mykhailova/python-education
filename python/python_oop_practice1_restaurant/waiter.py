"""Module for class Waiter"""
from person import Person
from order import Order
from customer import Customer


class Waiter(Person):
    """Class representing a waiter"""

    def __init__(self, name: str, last_name: str, salary: float):
        """Constructor"""
        Person.__init__(self, name, last_name)
        self.__salary = salary
        self.__orders_bring = []
        self.__orders_brought = []

    def __str__(self):
        """Prints the waiter"""
        return f'Full name: {self.get_full_name}\n' \
               f'Salary: {self.get_salary()}$'

    def get_salary(self) -> float:
        """Returns salary of waiter"""
        return self.__salary + self.__count_tips_from_payment()

    def __count_tips_from_payment(self) -> float:
        """Returns the sum of tips from brought orders"""
        result = sum([order.get_paid_sum() - order.get_full_price() for order in self.__orders_brought])
        self.clear_orders_brought()
        return result

    def clear_orders_brought(self):
        """Clears orders_brought"""
        self.__orders_brought.clear()

    def take_order(self, customer: Customer, ordered_dishes: list) -> Order:
        """Creates and adds order to orders_bring"""
        order = Order(customer, ordered_dishes)
        self.__orders_bring.append(order)
        return order

    def bring_order(self, order: Order):
        """Deletes order from orders_bring and adds to orders_brought"""
        self.__orders_bring.remove(order)
        self.__orders_brought.append(order)
