"""This module calc.py is for implementing Calculator class with 4 operations"""
from functools import reduce


class Calculator:
    """Calculator class for 4 operations"""

    @staticmethod
    def sum_parameters(*args):
        """Returns sum of parameters *args"""
        return sum(args)

    @staticmethod
    def subtract_parameters(*args):
        """Returns subtraction of parameters *args"""
        return args[0] - sum(args[1:])

    @staticmethod
    def multiply_parameters(*args):
        """Returns multiplication value result of parameters *args"""
        return reduce(lambda x, y: x*y, args)

    @staticmethod
    def divide_parameters(*args):
        """Returns division value result of parameters *args"""
        return reduce(lambda x, y: x/y, args)
