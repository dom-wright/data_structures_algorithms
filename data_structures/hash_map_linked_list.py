'''
Hashmaps

Hashmaps, also known as a hash tables, are data structures that allows efficient storage, retrieval, and modification of key-value pairs. Key-value pairs are stored in an array-based data structure like a python list. The index to which they are placed (and retrieved) is calculated by hashing the key. In some cases, hash collisions are dealt with by using an algorithm to calculate an alternative spot, but in this case linked lists are established at each index and key-values simply appended to the end.

Usage:
- Caching systems
- Symbol tables in compilers and interpreters
- Databases and indexing structures
- Implementations of sets and dictionaries in programming languages
'''


import random


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
        pass

    def insert_end(self, value):
        current_node = self.head_node
        # iterate through to reach the end node and append on end.
        while (current_node.get_next_node()):
            current_node = current_node.get_next_node()
        current_node.set_next_node(Node(value))

    def remove_node(self, value_to_remove):
        pass

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


class HashMap:

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        # if there is nothing there, create a linked list with a key, value list being the head node's value.
        if current_array_value is None:
            self.array[array_index] = LinkedList([key, value])
            return

        # iterate through linked list until the key value is encounted or add it to the end.
        for node in self.array[array_index]:
            if node.get_value()[0] == key:
                node.set_value([key, value])
                return

        # if key, value doesn't already exist, insert key, value at end.
        self.array[array_index].insert_end([key, value])
        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        # iterate through linked list until the key value is encounted or add it to the end.
        for node in self.array[array_index]:
            if node.get_value()[0] == key:
                return node.get_value()[1]

        print("Key not found!")
        return


if __name__ == "__main__":
    hm = HashMap(16)
    for i in range(40):
        hm.assign(f'key{i}', random.randint(0, 100))
    hm.assign('key7', 100)
    hm.assign('key5', 110)

    print("key2: ", hm.retrieve('key2'))
    print("key7: ", hm.retrieve('key7'))

    print("\nHashmap array:")
    for i, val in enumerate(hm.array):
        print(f"Index {i}:\t{val.stringify_list() if val else 'Empty'}")
