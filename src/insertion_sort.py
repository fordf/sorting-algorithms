"""Implement an insertion sort in Python."""


def insertion_sort(iterable):
    """Return the input list sorted, left to right."""
    for idx in range(1, len(iterable)):
        new = idx
        while new > 0 and iterable[new - 1] > iterable[new]:
            iterable[new], iterable[new - 1] = iterable[new - 1], iterable[new]
            new = new - 1
    return input
