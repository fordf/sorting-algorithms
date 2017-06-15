"""Implement merge sort in python."""


def merge_sort(iterable):
    """Sort an iterable by dividing into two sublistst."""
    if len(iterable) <= 1:
        return iterable

    left = iterable[:(len(iterable) // 2)]
    right = iterable[(len(iterable) // 2):]

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

    return result + left + right


if __name__ == '__main__':  # pragma: no cover
    import timeit
    from random import randint

    input1 = [2, 1]
    input2 = [randint(0, 100000) for i in range(1000)]

    print('merge sort is an efficient, general-purpose, comparison-based sorting algorithm.')

    print('Timing for input [2, 1]: \n' +

          str(timeit.timeit(stmt="merge_sort(input1)",
                            setup='from __main__ import merge_sort, input1',
                            number=500)) +
          '\naverage time over 500 runs')
    print('Timing for [randint(0, 100000) for i in range(1000)]:\n' +
          str(timeit.timeit(stmt="merge_sort(input2)",
                            setup='from __main__ import merge_sort, input2',
                            number=500)) +
          '\naverage time over 500 runs')
