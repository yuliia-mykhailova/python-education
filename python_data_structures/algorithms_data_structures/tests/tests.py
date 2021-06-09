import pytest

from algorithms_data_structures.data_structures.queue import Queue
from algorithms_data_structures.data_structures.linked_list import LinkedList
from algorithms_data_structures.data_structures.stack import Stack


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
