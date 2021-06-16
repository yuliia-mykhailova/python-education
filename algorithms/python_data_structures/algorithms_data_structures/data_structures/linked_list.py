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
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        element = self.head
        while element:
            yield element.data
            element = element.next

    def prepend(self, data):
        """Adds to the beginning of list"""
        element = Node(data)
        if not self.head:
            self.head = element
            return
        element.next = self.head
        self.head = element
        self.size += 1

    def append(self, data):
        """Adds to the end of list"""
        element = Node(data)
        if self.head:
            self.tail.next = element
        else:
            self.head = element
        self.tail = element
        self.size += 1

    def lookup(self, data):
        """Returns the index of node data"""
        result = 0
        element = self.head
        while element:
            if element.data == data:
                return result
            element = element.next
            result += 1
        return -1

    def insert(self, data, index):
        """Inserts data into the list by index"""
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
        count = 0
        element = self.head
        while element:
            if count + 1 == index:
                node.next = element.next
                element.next = node
                return True
            element = element.next
            count += 1
        return False

    def delete(self, index):
        """Deletes node from list by index"""
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
        count = 0
        element = self.head
        while count < len(self) - 1:
            if count + 1 == index:
                temp = element.next
                if temp is self.tail:
                    self.tail = element
                else:
                    element.next = temp.next
                self.size -= 1
                return True
            element = element.next
            count += 1
        return False

    def get(self, index):
        """Returns the data of node in list by index"""
        count = 0
        element = self.head
        while element:
            if count == index:
                return element.data
            element = element.next
            count += 1
        return False
