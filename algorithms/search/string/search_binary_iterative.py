'''
Binary Search 

Binary represents a fast way to search through a sorted list using pointers. The area of the list being search is progressively halved until the target is found.

Steps: 
- The value at the middle index will be compared to the target value.
- If the target value is less than the middle index value, the right pointer is moved to the middle index. If the target is more than the middle index value, the left pointer is moved to the middle index.
- The process is repeated until the base case is reached, which is either that the middle index value is equal to the target value, or the left pointer is equal or more than the right pointer (target value not found).

Runtime:
The area of the list being search is progressively halved until the target is found, therefore this search method has a runtime of O log N.

Example:
In this example, we have also included a handy step to omit empty values and reduce the size of the list that is being searched. This is useful for large datasets that have a high percentage of empty values.
'''


def sparse_search(data, search_val):
    print("Data: " + str(data))
    print("Search Value: " + str(search_val))
    first = 0
    last = len(data) - 1
    while first <= last:
        mid = (first + last) // 2
        if not data[mid]:
            left = mid - 1
            right = mid + 1
            while (True):
                if left < first and right > last:
                    print(f"{search_val} is not in the dataset")
                    return
                elif right <= last and data[right]:
                    mid = right
                    break
                elif left >= first and data[left]:
                    mid = left
                    break
                right += 1
                left -= 1
        if data[mid] == search_val:
            print(f"{search_val} found at position {mid}")
            return
        if search_val < data[mid]:
            last = mid - 1
        if search_val > data[mid]:
            first = mid + 1
    print(f"{search_val} is not in the dataset")


sparse_search([""], "Hello")
sparse_search(["A", "", "", "", ""], "A")
sparse_search(["", "", "", "", "Z"], "Z")
sparse_search(["A", "", "", "", "B", "", "", "", "C"], "B")
sparse_search(["A", "", "", "", "B", "", "", "", "C", "", "", "D"], "C")
sparse_search(["A", "B", "", "", "E"], "A")
sparse_search(["", "X", "", "Y", "Z"], "Z")
sparse_search(["A", "", "", "", "B", "", "", "", "C"], "D")
sparse_search(["Apple", "", "Banana", "", "", "", "", "Cow"], "Banana")
sparse_search(["Alex", "", "", "", "", "Devan", "", "", "Elise", "", "", "",
              "Gary", "", "", "Mimi", "", "", "Parth", "", "", "", "Zachary"], "Parth")
