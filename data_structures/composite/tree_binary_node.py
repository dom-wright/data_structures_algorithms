'''
Binary search tree:

a binary search tree node contains a value and at maximum a left and right leave node of the same type. it may also contain a depth attribute to show its position within the larger tree structure.

when a node is added, the root node will check if the value is lower or higher than its own value. if lower, it will attempt to place the node as its left leave. if it already has a left leave, it will pass the value to that node and recursively call its insert method until a free leave is available. note the class must decide which way to send matching values and stick with it.

searching involves a very similar pattern, eventually returning self once the matching value has been found.
'''


class BinaryTreeNode:

    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTreeNode(value, self.depth + 1)
                print(
                    f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(value, self.depth + 1)
                print(
                    f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)

    def retrieve(self, value):
        if value == self.value:
            return self
        if value < self.value:
            if self.left is None:
                print(f'No node with that value found')
                return
            else:
                return self.left.retrieve(value)
        else:
            if self.right is None:
                print(f'No node with that value found')
                return
            else:
                return self.right.retrieve(value)

    def depth_first_traversal(self):
        if self.left:
            self.left.depth_first_traversal()
        print(f'Depth={self.depth}, Value={self.value}')
        if self.right:
            self.right.depth_first_traversal()

    def delete(self, value):
        '''
        where does all this get completed?

        1 - traverse down to the given node. identify it by its value. if not found, print that warning and return.
        2 - if it is found, check for a left and right node. if none, just delete the node (del self). if there is only a left or right node, reallocate to the parent node.
        3 - if both nodes are present, you will need to take the right node and traverse down its left side to the bottom i.e. if self.left == none, return self. this will be the new node.

        don't reallocate node, just change the value.

        remember to change the depths.

        '''


if __name__ == "__main__":
    root = BinaryTreeNode(100)

    root.insert(50)
    root.insert(125)
    root.insert(75)
    root.insert(25)
    root.insert(20)
    root.insert(160)
    root.insert(150)
    root.insert(30)

    root.depth_first_traversal()
