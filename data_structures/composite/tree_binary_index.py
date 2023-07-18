'''
Binary Index Trees (BIT)

A binary index tree (or fenwick tree), is a data structure used to efficiently compute accumulations (such as sums or frequencies) in an array. The key idea behind a BIT is to represent the cumulative frequencies of prefix sums of elements using a binary tree structure.

Description:
https://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a

Characteristics:
- The size of the binary indexed tree is equal to n, where n represents the size of the input array.
- The BIT has two operations, update() and get_sum().
- First you initialise all values in the BIT as 0, then call update() for all indexes to insert values according to the input array.
- Note the accumulate values will not be in the same order as the input array, but rather use a complex system involving BITWISE calculations to place and update figures accordingly.

Runtime:
It takes O log(n) time to find the sum of the first i elements, and also to update a value of a specified element.
'''


arr = [1, 8, -13, 4, 7, -6, 12, 14, 2, -8, 16, 3]
binary_indexed_tree = [1, 8, -13, 4, 7, -6, 12, 14, 2, -8, 16, 3]

i = 1

nxt = i + (i & -1)
binary_indexed_tree[nxt - 1] += binary_indexed_tree[i - 1]

for i in range(2, len(binary_indexed_tree)):
    nxt = i + (i & -i)
    if nxt - 1 >= len(binary_indexed_tree):
        continue
    binary_indexed_tree[nxt - 1] += binary_indexed_tree[i - 1]

print(binary_indexed_tree)
