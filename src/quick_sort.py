"""Quick sort implementation."""


def quick_sort(lst):
    """Sort all the things."""
    if len(lst) > 1:
        pivot = partition(lst)
        return quick_sort(lst[:pivot]) + [lst[pivot]] + quick_sort(lst[pivot + 1:])
    return lst


def partition(lst):
    """Divide list into two sublists and sort around a pivot point."""
    pivot = lst[-1]
    swap_at = 0
    for i in range(len(lst) - 1):
        if lst[i] <= pivot:
            lst[i], lst[swap_at] = lst[swap_at], lst[i]
            swap_at += 1
    lst[-1], lst[swap_at] = lst[swap_at], lst[-1]
    return swap_at


if __name__ == '__main__':   # pragma: no cover
    import timeit
    from random import randint

    input1 = [2, 1]
    input2 = [randint(0, 100000) for i in range(1000)]

    print('Quick sort is an efficient, general-purpose, comparison-based sorting algorithm.')

    print('Timing for input [2, 1]: \n' +

          str(timeit.timeit(stmt="quick_sort(input1)",
                            setup='from __main__ import quick_sort, input1',
                            number=500)) +
          '\naverage time over 500 runs')
    print('Timing for [randint(0, 100000) for i in range(1000)]:\n' +
          str(timeit.timeit(stmt="quick_sort(input2)",
                            setup='from __main__ import quick_sort, input2',
                            number=500)) +
          '\naverage time over 500 runs')