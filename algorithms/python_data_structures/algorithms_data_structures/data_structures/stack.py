"""Module for implementing stack"""
from algorithms_data_structures.data_structures.linked_list import LinkedList


class Stack(LinkedList):
    """Class for stack implementation"""

    def __init__(self):
        """Constructor"""
        super().__init__()

    def push(self, data):
        """Adds element to the stack"""
        self.append(data)

    def pop(self):
        """Deletes element from the stack"""
        self.delete(len(self)-1)

    def peek(self):
        """Returns the end of the stack"""
        return self.tail.data
