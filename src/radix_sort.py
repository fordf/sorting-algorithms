"""Implement Radix sort in python."""


def radix_sort(lst):
    """Sort a list of numbers from lowest to highest."""
    if lst == []:
        return []
    max_digit = max([len(str(num)) for num in lst])

    for digit in range(max_digit):
        buckets = [[] for x in range(10)]

        for num in lst:
            idx = num % (10 ** (digit + 1)) // (10 ** digit)
            buckets[idx].append(num)

        lst = []

        [lst.extend(bucket) for bucket in buckets]

    return lst


if __name__ == '__main__':  # pragma: no cover
    import timeit
    from random import randint

    input1 = [2, 1]
    input2 = [randint(0, 100000) for i in range(1000)]

    print('Radix sort is a non comparative method of sorting a list of integers.')

    print('Timing for input [2, 1]: \n' +

          str(timeit.timeit(stmt="radix_sort(input1)",
                            setup='from __main__ import radix_sort, input1',
                            number=500)) +
          '\naverage time over 500 runs')
    print('Timing for [randint(0, 100000) for i in range(1000)]:\n' +
          str(timeit.timeit(stmt="radix_sort(input2)",
                            setup='from __main__ import radix_sort, input2',
                            number=500)) +
          '\naverage time over 500 runs')