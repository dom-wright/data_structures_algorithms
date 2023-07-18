'''
Double Linked Lists

Very similar to Linked Lists, but allow operations at both ends of the list.
'''


from node import NodeDouble


class LinkedListDouble:

    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_value):
        new_head = NodeDouble(new_value)
        current_head = self.head_node

        if current_head != None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head

        if self.tail_node == None:
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        new_tail = NodeDouble(new_value)
        current_tail = self.tail_node

        if current_tail != None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        if self.head_node == None:
            self.head_node = new_tail

    def remove_head(self):
        removed_head = self.head_node

        if removed_head == None:
            return None

        self.head_node = removed_head.get_next_node()

        if self.head_node != None:
            self.head_node.set_prev_node(None)

        if removed_head == self.tail_node:
            self.remove_tail()

        return removed_head.get_value()

    def remove_tail(self):
        removed_tail = self.tail_node

        if removed_tail == None:
            return None

        self.tail_node = removed_tail.get_prev_node()

        if self.tail_node != None:
            self.tail_node.set_next_node(None)

        if removed_tail == self.head_node:
            self.remove_head()

        return removed_tail.get_value()

    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node

        while current_node != None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break

            current_node = current_node.get_next_node()

        if node_to_remove == None:
            return None

        if node_to_remove == self.head_node:
            self.remove_head()

        elif node_to_remove == self.tail_node:
            self.remove_tail()

        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)

            return node_to_remove

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
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
    ll = LinkedListDouble()

    ll.add_to_head(10)
    ll.add_to_head(5)
    ll.add_to_tail(15)
    ll.add_to_tail(20)
    ll.add_to_tail(25)
    print(ll.stringify_list())

    ll.remove_head()
    ll.remove_tail()
    ll.remove_by_value(15)
    print(ll.stringify_list())
