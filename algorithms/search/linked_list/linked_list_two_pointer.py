'''
Algorithms to find the nth last or middle value of a linked list.
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


def nth_last_node(linked_list, n):
    first_trav = linked_list.get_head_node()
    counter = 0
    while counter < n:
        first_trav = first_trav.get_next_node()
        if first_trav == None:
            return None
        counter += 1
    second_trav = linked_list.get_head_node()
    while first_trav != None:
        first_trav = first_trav.get_next_node()
        second_trav = second_trav.get_next_node()
    return second_trav


def find_middle(linked_list):
    fast = linked_list.head_node
    slow = linked_list.head_node
    while fast:
        fast = fast.get_next_node()
        if fast:
            fast = fast.get_next_node()
            slow = slow.get_next_node()
    return slow


def generate_test_linked_list():
    linked_list = LinkedList()
    for i in range(1, 31):
        linked_list.insert_end(i)
    return linked_list


test_list = generate_test_linked_list()
nth_last = nth_last_node(test_list, 10)
print(nth_last.value)

middle = find_middle(test_list)
print(middle.value)
