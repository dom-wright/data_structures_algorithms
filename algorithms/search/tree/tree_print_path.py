from collections import deque


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return self.value


def print_tree(root):

    stack = deque()
    stack.append([root, 0])
    level_str = "\n"

    while len(stack) > 0:
        node, level = stack.pop()
        if level > 0 and len(stack) > 0 and level <= stack[-1][1]:
            level_str += "   "*(level-1) + "├─"
        elif level > 0:
            level_str += "   "*(level-1) + "└─"
        level_str += str(node.value)
        level_str += "\n"
        level += 1
        for child in node.children:
            stack.append([child, level])

    print(level_str)


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


print_tree(sample_root_node)
