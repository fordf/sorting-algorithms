"""Quick sort implementation."""


def quick_sort(lst):
    """Sort all the things."""
    if len(lst) > 1:

        pivot = partition(lst)
        return quick_sort(lst[:pivot]) + [lst[pivot]] + quick_sort(lst[pivot + 1:])
    return lst


def partition(lst):
    """."""
    pivot = lst[-1]
    swap_at = 0
    for i in range(len(lst) - 1):
        if lst[i] <= pivot:
            lst[i], lst[swap_at] = lst[swap_at], lst[i]
            swap_at += 1
    lst[-1], lst[swap_at] = lst[swap_at], lst[-1]
    return swap_at
