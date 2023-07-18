'''
Hashmaps

Hashmaps, also known as a hash tables, are data structures that allows efficient storage, retrieval, and modification of key-value pairs. Key-value pairs are stored in an array-based data structure like a python list. The index to which they are placed (and retrieved) is calculated by hashing the key. Where keys return the same index (collisions), an algorithm is used to determine an available spot.

Usage:
- Caching systems
- Symbol tables in compilers and interpreters
- Databases and indexing structures
- Implementations of sets and dictionaries in programming languages
'''


import random


class HashMap:

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(array_size)]

    def hash(self, key, count_collisions=0):
        # hashes the key name to a value.
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        # reduces the hashed value to a viable index in the array.
        return hash_code % self.array_size

    def assign(self, key, value):
        # assigns key and value to the hashmap array.
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        # if there is nothing there, save new key/value in.
        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        # if key matches, change value associated with it (intention was obviously to update the value associated with the key).
        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # if neither of the above, collision encountered!
        number_collisions = 1

        # find a slot that is free by adding a salt to the hashing algorithm.
        while (current_array_value[0] != key):
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            # repeat above checks on the new index position.
            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1

        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieval_collisions = 1

        while (possible_return_value != key):
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1

        return


if __name__ == "__main__":
    hm = HashMap(16)
    for i in range(16):
        hm.assign(f'key{i}', random.randint(0, 100))
    hm.assign('key7', 100)
    hm.assign('key5', 110)

    print("key2: ", hm.retrieve('key2'))
    print("key7: ", hm.retrieve('key7'))

    print("\nHashmap array:")
    for i, val in enumerate(hm.array):
        print(f"Index {i}:\t{val}")
