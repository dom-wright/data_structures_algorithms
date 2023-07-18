'''
Quick Sort

Similar to merge sort, in that it is Divide and Conquer, but introduces the concept of a pivot number. Once the pivot value is selected, the list items are sorted in place so that lower numbers are positioned before and higher numbers positioned after the pivot. 

The full list and indexes for the first half are put through the function again, the same is done with the second half, until all items have been fully sorted in place.

Pivot number:
For the quick sort to be efficient, you need a fairly even halving of the array each time, therefore the pivot number is important. Choosing the first value in the list could run into problems if the list is already fairly well sorted, therefore often a mean of first, middle and last value is taken, or a random index each time. This also prevents an array being setup specifically to cause resource issues.

Runtime:
O(N log N)
worst case runtime is O(n^2), potentially where the list is already sorted and the pivot is chosen as the first number each time, but the average case is O(N log N).
'''

from random import randrange, shuffle


def quicksort(lst, start, end):

    if start >= end:
        return

    pivot_idx = randrange(start, end + 1)
    pivot_element = lst[pivot_idx]

    # put the pivot value at the end of the list.
    lst[end], lst[pivot_idx] = lst[pivot_idx], lst[end]

    # will track iteration through list.
    lt_pointer = start

    for i in range(start, end):
        if lst[i] < pivot_element:
            lst[i], lst[lt_pointer] = lst[lt_pointer], lst[i]
            lt_pointer += 1

    lst[end], lst[lt_pointer] = lst[lt_pointer], lst[end]

    # nothing is returned as the list is sorted in place.
    quicksort(lst, start, lt_pointer - 1)
    quicksort(lst, lt_pointer + 1, end)


lst = [5, 3, 1, 7, 4, 6, 2, 8]
shuffle(lst)
print("PRE SORT: ", lst)
print(quicksort(lst, 0, len(lst) - 1))
print("POST SORT: ", lst)


'''
HOW IT WORKS:
The 'lesser than pointer' will remain on an element larger than the pivot until it is replaced by a smaller element further on. Only then will the 'lesser than pointer' progress to the next element.

[5, 6, 2, 3, 1, 4]
# we randomly select "3" and swap with the last element
[5, 6, 2, 4, 1, 3]
 
# We'll use () to mark our "lesser than" pointer
# We'll use {} to mark our progress through the list
 
[{(5)}, 6, 2, 4, 1, 3]
# {5} is not less than 3, so the "lesser than" pointer doesn't move
 
[(5), {6}, 2, 4, 1, 3]
# {6} is not less than 3, so the "lesser than" pointer doesn't move
 
[(5), 6, {2}, 4, 1, 3]
# {2} is less than 3, so we SWAP the values...
[(2), 6, {5}, 4, 1, 3]
# Then we increment the "lesser than" pointer
[2, (6), {5}, 4, 1, 3]
 
[2, (6), 5, {4}, 1, 3]
# {4} is not less than 3, so the "lesser than" pointer doesn't move
 
[2, (6), 5, 4, {1}, 3]
# {1} is less than 3, so we SWAP the values...
[2, (1), 5, 4, {6}, 3]
# Then we increment the "lesser than" pointer
[2, 1, (5), 4, {6}, 3]
 
# We've reached the end of the non-pivot values
[2, 1, (5), 4, 6, {3}]
# Finally, swap the "lesser than" pointer with the pivot so the pivot lies in the middle.
[2, 1, (3), 4, 6, {5}]
'''
