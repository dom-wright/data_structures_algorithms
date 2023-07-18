'''
Merge Sort

Merge sort works by recursively halving a list by index until each value exists on its own, and then merging them back together, ordering them as you proceed. This approach makes merge sort considered a 'Divide & Conquer' algorithm. 

The thinking behind this strategy is that as the remerged lists get longer, they are already somewhat sorted, therefore ordering will be quicker.

Runtime: 
O(N log N)
- log N because the list is recursively halved on the way down.
- N x (log N) on the way back up as all elements need to be scanned as they are merged into order.
'''


def merge_sort(items):

    # base case
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []

    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

    return result
