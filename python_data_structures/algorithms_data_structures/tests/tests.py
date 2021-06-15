import pytest

from algorithms_data_structures.data_structures.queue import Queue
from algorithms_data_structures.data_structures.linked_list import LinkedList
from algorithms_data_structures.data_structures.stack import Stack
from algorithms_data_structures.data_structures.hash_table import HashTable
from algorithms_data_structures.data_structures.binary_search_tree import BinarySearchTree
from algorithms_data_structures.data_structures.graph import Graph


# linked list tests
@pytest.fixture()
def empty_list():
    """Returns empty Linked list"""
    return LinkedList()


@pytest.fixture()
def list_numbers():
    """Returns Linked list of numbers"""
    list_num = LinkedList()
    for i in range(1, 7):
        list_num.append(i)
    return list_num


def test_linked_list_append(empty_list):
    empty_list.append(2)
    assert empty_list.head.data == empty_list.get(0)
    empty_list.prepend(1)
    empty_list.append(3)
    assert empty_list.tail.data == 3
    assert len(empty_list) == 3


def test_linked_list_insert_lookup(list_numbers):
    list_numbers.insert(4, 3)
    assert list_numbers.lookup(4) == 3
    assert list_numbers.lookup(6) == 6
    assert list_numbers.lookup(1) == 0


def test_linked_list_delete(list_numbers):
    list_numbers.delete(0)
    assert list_numbers.head.data == 2
    list_numbers.delete(2)
    assert not list_numbers.get(4)
    list_numbers.delete(3)
    assert list_numbers.tail.data == 5


# queue tests
@pytest.fixture()
def empty_queue():
    """Returns empty Queue"""
    return Queue()


@pytest.fixture()
def queue_numbers():
    """Returns Queue of numbers"""
    queue = Queue()
    for i in range(1, 7):
        queue.enqueue(i)
    return queue


def test_queue_enqueue(empty_queue):
    empty_queue.enqueue(1)
    assert empty_queue.head.data == empty_queue.get(0)
    empty_queue.enqueue(2)
    empty_queue.enqueue(3)
    assert empty_queue.tail.data == 3
    assert len(empty_queue) == 3


def test_queue_dequeue_peek(queue_numbers):
    queue_numbers.dequeue()
    assert queue_numbers.head.data == 2
    assert queue_numbers.peek() == 6


# stack
@pytest.fixture()
def empty_stack():
    """Returns empty Stack"""
    return Stack()


@pytest.fixture()
def stack_numbers():
    """Returns Stack of numbers"""
    stack = Stack()
    for i in range(1, 7):
        stack.push(i)
    return stack


def test_stack_push(empty_stack):
    empty_stack.push(1)
    assert empty_stack.head.data == empty_stack.get(0)
    empty_stack.push(2)
    empty_stack.push(3)
    assert empty_stack.tail.data == 3
    assert len(empty_stack) == 3


def test_stack_pop_peek(stack_numbers):
    stack_numbers.pop()
    assert stack_numbers.tail.data == 5
    assert stack_numbers.peek() == 5


# hash table
@pytest.fixture()
def empty_hash_table():
    """Returns empty Hash Table"""
    return HashTable()


@pytest.fixture()
def some_hash_table():
    """Returns some Hash Table"""
    table = HashTable()
    table.insert(34, 'She')
    table.insert(456, 'sells')
    table.insert(33, 'seashells')
    table.insert(68, 'by')
    table.insert(101, 'the')
    table.insert(56, 'seashore')
    return table


def test_hash_table_insert(empty_hash_table):
    empty_hash_table.insert(1, 234)
    empty_hash_table.insert(16, '234')
    empty_hash_table.insert(34, 'qwerty')
    assert len(empty_hash_table) == 3


def test_hash_table_delete_lookup(some_hash_table):
    assert some_hash_table.lookup(33) == 'seashells'
    some_hash_table.delete(33)
    assert some_hash_table.lookup(33) == -1
    assert some_hash_table.lookup(456) == 'sells'
    some_hash_table.delete(456)
    assert some_hash_table.lookup(456) == -1
    assert some_hash_table.lookup(56) == 'seashore'
    some_hash_table.delete(56)
    assert some_hash_table.lookup(56) == -1


# binary search tree
@pytest.fixture()
def empty_binary_search_tree():
    """Returns empty Binary Search Tree"""
    return BinarySearchTree()


@pytest.fixture()
def some_binary_search_tree():
    """Returns some Binary Search Tree"""
    tree = BinarySearchTree()
    tree.insert(15)
    tree.insert(10)
    tree.insert(20)
    tree.insert(8)
    tree.insert(12)
    tree.insert(18)
    tree.insert(25)
    tree.insert(16)
    tree.insert(19)
    tree.insert(30)
    tree.insert(24)
    return tree


def test_tree_insert_lookup(empty_binary_search_tree):
    empty_binary_search_tree.insert(8)
    empty_binary_search_tree.insert(5)
    empty_binary_search_tree.insert(10)
    empty_binary_search_tree.insert(2)
    empty_binary_search_tree.insert(6)
    empty_binary_search_tree.insert(14)
    assert empty_binary_search_tree.lookup(8).right.data == 10
    assert empty_binary_search_tree.lookup(8).left.data == 5
    assert empty_binary_search_tree.lookup(5).left.data == 2
    assert empty_binary_search_tree.lookup(5).right.data == 6
    assert empty_binary_search_tree.lookup(10).right.data == 14
    with pytest.raises(ValueError):
        empty_binary_search_tree.insert(5)


def test_tree_delete_lookup(some_binary_search_tree):
    some_binary_search_tree.delete(25)
    assert some_binary_search_tree.lookup(20).right.data == 24
    assert some_binary_search_tree.lookup(20).left.data == 18
    some_binary_search_tree.delete(20)
    assert some_binary_search_tree.lookup(15).right.data == 24
    assert some_binary_search_tree.lookup(24).right.data == 30
    assert some_binary_search_tree.lookup(24).left.data == 18
    some_binary_search_tree.delete(12)
    assert some_binary_search_tree.lookup(10).right is None
    assert some_binary_search_tree.lookup(10).left.data == 8


# graph
@pytest.fixture()
def empty_graph():
    """Returns empty Graph"""
    return Graph()


@pytest.fixture()
def some_graph():
    """Returns some Graph"""
    graph = Graph()
    graph.insert(1, [2, 3, 4, 5])
    graph.insert(2, [3, 5])
    graph.insert(3, [6, 7])
    return graph


def test_graph_insert_lookup(empty_graph):
    empty_graph.insert(1, [3, 4, 5])
    empty_graph.insert(2, [1, 3, 4])
    empty_graph.insert(5, [6, 7])
    assert empty_graph.lookup(1).data == 1
    assert len(empty_graph.lookup(1).edges) == 4
    assert len(empty_graph.lookup(2).edges) == 3
    assert len(empty_graph.lookup(5).edges) == 3


def test_graph_delete_lookup(some_graph):
    some_graph.delete(4)
    assert len(some_graph.lookup(1).edges) == 3
    some_graph.delete(3)
    assert len(some_graph.lookup(1).edges) == 2
    assert len(some_graph.lookup(2).edges) == 2
    some_graph.delete(1)
    some_graph.print_graph()
    assert len(some_graph.lookup(2).edges) == 1
    assert len(some_graph.lookup(5).edges) == 1
    assert len(some_graph.lookup(6).edges) == 0
    assert len(some_graph.lookup(7).edges) == 0
