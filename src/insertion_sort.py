"""Implement an insertion sort in Python."""


def insertion_sort(iterable):
    """Return the input list sorted, left to right."""
    for idx in range(1, len(iterable)):
        new = idx
        while new > 0 and iterable[new - 1] > iterable[new]:
            iterable[new], iterable[new - 1] = iterable[new - 1], iterable[new]
            new = new - 1
    return iterable


if __name__ == '__main__':  # pragma: no cover
    import timeit
    from random import randint

    input1 = [2, 1]
    input2 = [randint(0, 100000) for i in range(1000)]

    print('Insertion sort is a sorting algorith that builds a sorted list from and input string one line at a time.')

    print('Timing for input [2, 1]: \n' +

          str(timeit.timeit(stmt="insertion_sort(input1)",
                            setup='from __main__ import insertion_sort, input1',
                            number=500)) +
          '\naverage time over 500 runs')
    print('Timing for [randint(0, 100000) for i in range(1000)]:\n' +
          str(timeit.timeit(stmt="insertion_sort(input2)",
                            setup='from __main__ import insertion_sort, input2',
                            number=500)) +
          '\naverage time over 500 runs')
