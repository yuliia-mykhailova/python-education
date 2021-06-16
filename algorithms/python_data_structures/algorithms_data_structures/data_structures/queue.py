"""Module for implementing queue"""

from algorithms_data_structures.data_structures.linked_list import LinkedList


class Queue(LinkedList):
    """Class for queue implementation"""

    def __init__(self):
        """Constructor"""
        super().__init__()

    def enqueue(self, data):
        """Adds node to the queue"""
        self.append(data)

    def dequeue(self):
        """Deletes node from the queue"""
        self.delete(0)

    def peek(self):
        """Returns the end of queue"""
        return self.tail.data
