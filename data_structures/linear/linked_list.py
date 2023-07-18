'''
Linked Lists

Linked lists are a construct of nodes, each containing a value and reference to the next node in the list. Nodes can be scattered throughout memory. This makes insertion/removal operations very efficient, as new items can be saved anywhere and only require the preceding node to update its pointers.

Note that python lists are NOT linked lists. The elements (or rather references to those elements) are stored in a contiguous block of memory, occupying a fixed amount of space. This makes retrieval/indexing very fast. On the other hand, inserting or removing an element at the beginning or middle of the list requires shifting all of the subsequent elements over by one position, which can be a relatively laborious and slow operation if the list is large.

Usage:
- Linked lists are often utilised for queues and stacks, which typically only require operations at the start / end of the list, rather than in the middle.
'''


from node import Node


class LinkedList:

    # at the initialising of the LL, the first node will always be the head_node.
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_end(self, value):
        current_node = self.head_node
        # iterate through to reach the end node and append on end.
        while (current_node.get_next_node()):
            current_node = current_node.get_next_node()
        current_node.set_next_node(Node(value))

    # the method here is to simply orphan the node so it is garbage collected, rather than actively delete it.
    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + " "
            current_node = current_node.get_next_node()
        return string_list

    def __iter__(self):
        current_node = self.head_node
        while (current_node):
            yield current_node
            current_node = current_node.get_next_node()


if __name__ == "__main__":
    ll = LinkedList(15)
    ll.insert_beginning(10)
    ll.insert_beginning(5)
    ll.insert_end(20)
    ll.insert_end(25)
    print(ll.stringify_list())

    ll.remove_node(10)
    ll.remove_node(15)
    ll.remove_node(20)
    print(ll.stringify_list())

    for i in ll:
        print(i.value)
