'''
Tree search

depth-first vs breadth-first search
- The function can be modified to be either depth-first or breadth-first simply by changing how the paths to check are either appended to the deque, or popped from the deque for checking.
- Note the TreeNode class used for this is highly simplified for the purposes of the exercise, missing many of its common methods.
'''


from collections import deque


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return self.value


def search(root_node, goal_value):

    my_queue = deque()
    current_path = [root_node]
    my_queue.append(current_path)

    while my_queue:
        '''
        breadth first = pop from end of queue, i.e. use pop()
        depth first = pop from front of queue i.e. use popleft()
        alternatively you can alternate appendleft() and append() when adding to the queue to change the method.
        '''

        current_path = my_queue.popleft()
        print(f"Checking {current_path}")
        node_to_check = current_path[-1]
        if node_to_check.value == goal_value:
            return current_path

        for child in node_to_check.children:
            new_path = current_path[:]
            new_path.append(child)
            # you can also control search method by how you append the paths to check to the queue.
            my_queue.appendleft(new_path)
            print(my_queue)

    return None


sample_root_node = TreeNode("A")
two = TreeNode("B")
three = TreeNode("C")
sample_root_node.children = [three, two]
four = TreeNode("D")
five = TreeNode("E")
six = TreeNode("F")
seven = TreeNode("G")
two.children = [five, four]
three.children = [seven, six]

search_val = "D"

goal_path = search(sample_root_node, search_val)
if goal_path is None:
    print("No path found")
else:
    print("Path found!")
    for node in goal_path:
        print(node)
