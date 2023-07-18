'''
Binary search recursive

Binary search represents a fast way to search through a sorted list using pointers demarking the section of the list that is being searched, and recursion to gradually reduce this section until finding the target. Steps:

- left pointer for the start of the list, right pointer for the end.
- add left index to right index and divide by two to get middle index, and subsequently middle value.
- compare middle value to target, return middle index if a match.
- most likely it won't match. if target is lower, move right pointer to middle index, if higher, move left pointer to middle index.
- repeat process until a match has been found and index returned.
- if the target is not present in the list, the recursion will a base case to stop the recursion.
'''


def binary_search(sorted_list, left_pointer, right_pointer, target):
    # this condition indicates we've reached an empty "sub-list"
    if left_pointer >= right_pointer:
        return "value not found"

    # We calculate the middle index from the pointers now
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx
    if mid_val > target:
        # we reduce the sub-list by passing in a new right_pointer
        return binary_search(sorted_list, left_pointer, mid_idx, target)
    if mid_val < target:
        # we reduce the sub-list by passing in a new left_pointer
        return binary_search(sorted_list, mid_idx + 1, right_pointer, target)


values = [77, 80, 102, 123, 288, 300, 540]
target = 288

start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, target)


print(f"element {target} is located at index {result}.")
