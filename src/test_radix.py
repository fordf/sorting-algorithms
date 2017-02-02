"""Tests for radix sort function."""
import pytest
from random import randint


LISTS = [
    ([1.11111], [1.11111]),
    ([], []),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([4, 2, 4, 1, 3, 5, 6, 3], [1, 2, 3, 3, 4, 4, 5, 6]),
    ([3.3, 1.12, 42, 19.999999, 19.999], [1.12, 3.3, 19.999, 19.999999, 42]),
]


@pytest.mark.parametrize('unsorted_lst, sorted_lst', LISTS)
def test_radix_sort(unsorted_lst, sorted_lst):
    """Radix sort should sort lists."""
    from radix_sort import radix_sort
    assert radix_sort(unsorted_lst) == sorted_lst


def test_radix_sort_against_python_sort():
    """Test radix sort against python's sort method."""
    from radix_sort import radix_sort
    input_list = [randint(0, 100000) for i in range(1000)]
    test_list = radix_sort(input_list)
    input_list.sort()
    assert test_list == input_list
