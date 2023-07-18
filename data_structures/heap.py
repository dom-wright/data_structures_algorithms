'''
Heap / heapsort

A heap is a data structure that allows you to efficiently maintain a collection of elements in order (typically stored in an array), with the primary purpose to enable the efficient retrieval and update of the max/min value in the array. The below example is for a max-heap.

The order of the data in the array follows the concept of a binary tree. The root (maximum value) starts at index 1 (None at index 0), with the 2nd and 3rd largest values (its children) at index 2 and 3. Index 1's children nodes are then placed at 4 and 5, index 2's children at 6 and 7, and so on. This develops a sort of tree structure as you progress down the list.

Every child must be smaller than its parent, therefore when new values are appended to the end of the list, they must be transferred to the correct position. This is achieved by repeatedly comparing its value to that of its parent, and swapping the two positions until it has reached its correct place. This process is called 'heapifying up'. 'Heapifying down' is where the root node is removed and is replaced with another value. This value must subsequently be compared with its children and swapped to its rightful place.

Heapsort:
Heaps can be used to sort a list of values into a new list. Process:
- Build max-heap to store data from an unsorted list.
- Extract the largest value from the heap and place it into a sorted list.
- Replace the root with the last element in the list (as the last element has no children).
- Rebalance the heap.
- Once the max-heap is empty, return the sorted list.
'''


class MaxHeap:

    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    def add(self, element):
        self.count += 1
        print(f"Adding: {element} to {self.heap_list}")
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Heapifying up")
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent < child:
                print(f"swapping {parent} with {child}")
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        print(f"Heap Restored {self.heap_list}")

    def retrieve_max(self):
        if self.count == 0:
            print("No items in heap")
            return None
        max_value = self.heap_list[1]
        print(f"Removing: {max_value} from {self.heap_list}")
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print(f"Last element moved to first: {self.heap_list}")
        self.heapify_down()
        return max_value

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            print("Heapifying down!")
            larger_child_idx = self.get_larger_child_idx(idx)
            child = self.heap_list[larger_child_idx]
            parent = self.heap_list[idx]
            if parent < child:
                self.heap_list[idx] = child
                self.heap_list[larger_child_idx] = parent
            idx = larger_child_idx
        print(f"HEAP RESTORED! {self.heap_list}")
        print("")

    def get_larger_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child > right_child:
                print("Left child " + str(left_child) +
                      " is larger than right child " + str(right_child))
                return self.left_child_idx(idx)
            else:
                print("Right child " + str(right_child) +
                      " is larger than left child " + str(left_child))
                return self.right_child_idx(idx)

    def heapify_up(self):
        print("Heapifying up")
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent < child:
                print(f"Swapping {parent} with {child}")
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)


def heapsort(lst):
    sort = []
    max_heap = MaxHeap()
    for idx in lst:
        max_heap.add(idx)
    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.insert(0, max_value)
    return sort


my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
print(sorted_list)
# [10, 13, 21, 22, 23, 61, 99]
