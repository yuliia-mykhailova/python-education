"""Module for hash table realization"""

from algorithms_data_structures.data_structures.linked_list import LinkedList


class Node:
    """Class for node for hash table implementation"""

    def __init__(self, key, value):
        """Constructor"""
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """Class for hash table implementation"""

    def __init__(self):
        """Constructor"""
        self.hash_keys = LinkedList()
        for i in range(10):
            self.hash_keys.append(LinkedList())
        self.size = 0

    def __len__(self):
        return self.size

    @staticmethod
    def hashing(key):
        """Returns the hash of the key"""
        return key % 10

    def insert(self, key, value):
        """Inserts the element into hash table"""
        hashed = self.hashing(key)
        node = Node(key, value)
        self.hash_keys.get(hashed).append(node)
        self.size += 1

    def lookup(self, key):
        """Returns the value of element in hash table by key"""
        hashed = self.hashing(key)
        key_list = self.hash_keys.get(hashed)
        current = key_list.head
        while current:
            if current.data.key == key:
                return current.data.value
            current = current.next
        return -1

    def delete(self, key):
        """Deletes an element from hash table by key"""
        hashed = self.hashing(key)
        key_list = self.hash_keys.get(hashed)
        current = key_list.head
        index = 0
        while current:
            if current.data.key == key:
                print(key_list.delete(index))
                self.size -= 1
                return True
            current = current.next
            index += 1
        return False
