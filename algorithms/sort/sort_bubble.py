'''
Bubble Sort

Process:
- Consists of an outer and inner loop over the range of the sequence.
- The inner loop starts at index 0 of the array every time.
- It compares the value at the index it is on, with that of the next index in the sequence. if the next in the sequence is smaller, it switches their positions.
- It then moves onto the next index (which could be the same value as last time) and repeats.
- Essentially this progressively moves the larger values towards the end of the array.
- Once the loop is finished, it starts the process again at index 0.
- This process will repeat for every iteration of the outer loop, guaranteeing enough iterations to move every value to its correct position.

Optimisation:
- As each progressive inner loop guarantees that one large value will make it to its final position at or near the end, the length of each inner loop can be reduced by one each time, best achieved by subtracting the current value of the outer loop in the inner loop range (see below).
- If an inner loop doesn't switch any values, all values are in the correct position. you can detect this and break out of the process early, to avoid needless cycles.

Note the range of the inner loop:
1) Has a -1. This avoids an index error when comparing the value with the value at [index + 1] when the end of the list is reached.
2) Has a -i. this is the main function of the outer loop. after each iteration of the inner loop, the largest values have progressively found their place at the end of the array. it is therefore wasteful to compare them again.
'''


# best case - 8 iterations. breaks after first loop
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# worst case - 36 iterations (8 + 7 + 6...)
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 26 iterations
nums = [3, 1, 2, 4, 5, 7, 6, 8, 5]

print("PRE SORT: {0}".format(nums))


def bubble_sort(arr):
    iteration_count = 0
    for i in range(len(arr)):
        swap_count = 0
        for j in range(len(arr) - i - 1):
            iteration_count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
        if swap_count == 0:
            break

    print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))


bubble_sort(nums)
print("POST SORT: {0}".format(nums))
