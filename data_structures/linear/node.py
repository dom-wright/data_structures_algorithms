'''
Nodes

Nodes are fundamental components of various data structures, including linked lists, trees, graphs, and more. They represents a single element within the data structure and typically contains two main parts, data (a value), and references (or pointers) to other nodes within the data structure.

The two nodes classes below define node objects that you would find in linked lists / linear data structures.
'''


class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class NodeDouble:

    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value
