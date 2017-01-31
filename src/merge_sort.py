"""Implement merge sort in python."""


def merge_sort(iterable):
    """Sort an iterable."""
    if len(iterable) <= 1:
        return iterable

    # divide list into equal-sublists
    left = iterable[:(len(iterable) // 2)]
    right = iterable[(len(iterable) // 2):]

    # revursively sort both sublists
    left = merge_sort(left)
    right = merge_sort(right)

    return _merge(left, right)


def _merge(left, right):
    """Merge two sorted sublists."""
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while left:
        result.append(left[0])
        left = left[1:]
    while right:
        result.append(right[0])
        right = right[1:]
    return result
