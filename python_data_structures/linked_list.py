"""Module for implementing linked list"""


class Node:
    """Class for node of the list"""
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """Class for linked list implementation"""

    def __init__(self):
        """Constructor"""
        self.__first = Node()
        self.__last = Node()
        self.__size = 0

    def add_first(self, data):
        """Adds to the beginning of list"""
        element = Node(data)
        element.next = self.__first
        if not self.__last:
            self.__last = element
        self.__first = element
        self.__size += 1

    def add_last(self, data):
        """Adds to the end of list"""
        element = Node(data)
        if self.__first:
            self.__last.next = element
        else:
            self.__first = element
        self.__last = element
        self.__size += 1

    def remove_first(self):
        """Deletes the first el of list"""
        if self.__first:
            self.__first = self.__first.next
        elif self.__first is self.__last:
            self.__first = None
            self.__last = None
        self.__size -= 1

    def remove_last(self):
        """Deletes the last el of list"""
        before_last = self.__first
        if not self.__first or self.__first is self.__last:
            self.__first = None
            self.__last = None
            self.__size = 0
        else:
            while before_last.next != self.__last:
                before_last = before_last.next
            before_last.next = None
            self.__last = before_last
            self.__size -= 1

    def get_first(self):
        """Returns the first el of list"""
        element = Node(self.__first.data)
        self.remove_first()
        return element

    def get_last(self):
        """Returns the last el of list"""
        element = Node(self.__last.data)
        self.remove_last()
        return element

    def search(self, data):
        """Searches for el in list"""
        iterator = self.__first
        while iterator:
            if iterator.data == data:
                return iterator.data
            iterator = iterator.next
        return None

    def remove(self, data):
        """Deletes the el in list"""
        iterator = self.__first.next
        before_deleted = self.__first
        if self.__first.data == data:
            self.remove_first()
        elif self.__last.data == data:
            self.remove_last()
        else:
            while iterator != self.__last:
                if iterator.data == data:
                    before_deleted.next = iterator.next
                    self.__size -= 1
                iterator = iterator.next
                before_deleted = before_deleted.next

    def clear(self):
        """Clears the list"""
        self.__first = None
        self.__last = None
        self.__size = 0

    def size(self):
        """Returns the size of list"""
        return self.__size
