"""Module for Tree realization"""


class Node:
    """Class for binary search tree node implementation"""

    def __init__(self, data):
        """Constructor"""
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Class for binary search tree implementation"""

    def __init__(self):
        """Constructor"""
        self.root = None

    @staticmethod
    def is_leaf(node):
        """Returns if node is a leaf in tree"""
        if node.left and node.right:
            return False
        return True

    @staticmethod
    def set_node(prev, node, before=None):
        """Sets the value of the node before deleted"""
        if prev.right is node:
            prev.right = before
        else:
            prev.left = before

    def insert(self, data):
        """Inserts the element into binary search tree"""
        node = Node(data)
        if not self.root:
            self.root = node
            return
        current = self.root
        while not self.is_leaf(current):
            if data > current.data:
                current = current.right
            elif data < current.data:
                current = current.left
            else:
                raise ValueError('Element is already exists')
        if data > current.data:
            current.right = node
        else:
            current.left = node

    def lookup(self, data):
        """Returns the node with data value"""
        if data == self.root.data:
            return self.root
        current = self.root
        while current:
            if current.data == data:
                return current
            if data > current.data:
                current = current.right
            elif data < current.data:
                current = current.left
        return -1

    def __find_previous(self, data):
        """Returns the deleted element and element before"""
        if data == self.root.data:
            return self.root
        current = self.root
        while current:
            if current.right.data == data:
                return current, current.right
            elif current.left.data == data:
                return current, current.left
            if data > current.data:
                current = current.right
            elif data < current.data:
                current = current.left
        return -1

    def delete_root(self):
        """Deletes root element from tree"""
        right_tree = self.root.right
        left_tree = self.root.left

        # deal with leaves
        if not right_tree:
            self.root = left_tree
            return
        elif not left_tree:
            self.root = right_tree
            return

        # deal with pre-leaves
        if not right_tree.right and right_tree.left:
            self.root = right_tree
            self.root.left = left_tree
            return
        elif not left_tree.right and left_tree.left:
            self.root = left_tree
            self.root.right = right_tree
            return

        # deal with post trees
        current = self.root.right
        before = current
        while current.left or current.right:
            before = current
            if current.left:
                current = current.left
            else:
                current = current.right

        if before.right is current:
            self.root = before
            before.left = left_tree
        else:
            before.left = None
            self.root = current
            current.right = right_tree
            current.left = left_tree

    def delete(self, data):
        """Deletes the element from tree by value"""
        if data == self.root.data:
            self.delete_root()
            return
        prev, node = self.__find_previous(data)
        left_tree = node.left
        right_tree = node.right

        # deal with leaves
        if not node.left and not node.right:
            self.set_node(prev, node)
            return

        # deal with pre-leaves
        if left_tree:
            if not left_tree.right and not left_tree.left:
                self.set_node(prev, node, left_tree)
                left_tree.right = right_tree
                return
        elif not right_tree.right and not right_tree.left:
            self.set_node(prev, node, right_tree)
            right_tree.right = left_tree
            return

        # deal with post trees
        current = right_tree
        before = current
        while current.left or current.right:
            before = current
            if current.left:
                current = current.left
            else:
                current = current.right

        if before.right is current:
            self.set_node(prev, node, before)
            before.left = left_tree
        else:
            before.left = None
            self.set_node(prev, node, current)
            current.right = right_tree
            current.left = left_tree
