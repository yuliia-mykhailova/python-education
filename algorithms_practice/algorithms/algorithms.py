"""Module for binary search, quick sort and factorial realization"""


def binary_search(array: list, value: int) -> int:
    """binary search of element in list"""
    low = 0
    high = len(array) - 1
    while low <= high:
        middle = int((low + high) / 2)
        if array[middle] == value:
            return middle
        elif array[middle] > value:
            high = middle - 1
        else:
            low = middle + 1
    return -1


def quick_sort(array: list) -> list:
    """quick sort of list"""
    i = 0
    j = len(array) - 1
    stack = [[i, j]]
    while stack:
        part = stack.pop()
        low, high = part
        i, j = part
        pivot = int(low + (high - low) / 2)
        while i <= j:

            while array[i] < array[pivot]:
                i += 1
            while array[j] > array[pivot]:
                j -= 1

            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

        if low < j:
            stack.append([low, j])
        if high > i:
            stack.append([i, high])

    return array


def factorial(n: int):
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n - 1)
