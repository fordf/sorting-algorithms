"""Implement Radix sort in python."""


def radix_sort(lst):
    """Sort a list of numbers from lowest to highest."""
    max_digit = max([len(str(num)) for num in lst])

    for digit in range(max_digit):
        buckets = [[] for x in range(10)]

        for num in lst:
            idx = num % (10 ** (digit + 1)) // (10 ** digit)
            buckets[idx].append(num)

        lst = []

        [lst.extend(bucket) for bucket in buckets]

    return lst
