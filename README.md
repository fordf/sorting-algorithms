[![Build Status](https://travis-ci.org/fordf/sorting-algorithms.svg?branch=master)](https://travis-ci.org/fordf/sorting-algorithms)

# Sorting Algorithms

## Merge Sort
Take an unsorted list, recursively slice list segments in half until each item is
on it's own.
```
[4, 2, 8, 1]
 |
 V
[4, 2] [8, 1]
 |
 V
[4] [2]  [8] [1]
```
Go back up stack trace, merging pairs of list segments in sorted order.
```
[4] [2]  [8] [1]
 |
 V
[2, 4] [1, 8]
 |
 V
[1, 2, 4, 8]
```

Module: [merge_sort](https://github.com/fordf/sorting-algorithms/blob/merge/src/merge_sort.py)

Time Complexity:
* best-case: O(n*log(n))
* average-case: O(n*log(n))
* worst-case: O(n*log(n))

## Insertion Sort
For each element in the given list, compare it's value to the previous elements one
at a time. If the current element is smaller than the previous element, swap them,
and compare against the new previous element. Once the previous element is smaller
than the current element, continue on to the next unsorted element.

Module: [insertion_sort](https://github.com/fordf/sorting-algorithms/blob/insertion/src/insertion_sort.py)

Time Complexity: 
* best-case: O(n)
* average-case: O(n<sup>2</sup>)
* worst-case: O(n<sup>2</sup>)



