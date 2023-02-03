from math import floor
from pprint import pformat


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        asString = f"\n"
        nodes = self
        while nodes:
            key = f"\'{ nodes.key }\'\t\t\t"
            value = f"{ nodes.value }\t\t\t"
            nextNode = f"Node({ nodes.next.value if nodes.next else None })"

            asString += f"{ key }{ value }{ nextNode }\n"

            nodes = nodes.next

        return asString


# * This number is random from the example used online
# * See: https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd
# * Ideally this should be some prime number.
# * Refer to algo text book on how to best pick this number
INITIAL_CAPACITY = 50


class HashTable:
    def __init__(self):
        # self.nodes = node
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def __str__(self):
        dashCount = 20

        tableRepr = f"\nTable Capacity:\t{ self.capacity}"
        tableRepr += f"\nTable Size:\t{ self.size }"
        tableRepr += f"\n"
        tableRepr += "-"*dashCount
        tableRepr += f"\nKEY\t\t\tVALUE\t\t\tNEXT"

        for node in self.buckets:
            if node:
                tableRepr += str(node)

        return tableRepr

    def hash(self, key):
        return self._hash(key)
        # return self._hashByMultiplication(key)
        # return self._hashByDivision(key)
        # return self._universalHash

    def _hash(self, key):  # * This example is using hash by division
        hashSum = 0   # * Place holder for making a
        # For each character in the key

        for idx, c in enumerate(key):
            # * Add (index + length of key) ^ (current char code)
            hashSum += (idx + len(key)) ** ord(c)
            # Perform modulus to keep hashSum in range [0, self.capacity - 1]
            hashSum = hashSum % self.capacity

        return hashSum

    def _hashByMultiplication(self, key):
        # * Some number to the power of 2. Not too important
        m = 2
        # * some constant but this example should generally work
        a = (5 ** .5)/2
        return floor((m*(key*a) % 1))

    def _hashByDivision(self, key):
        # * Mod depends on the size of the table.
        # * It should be a prime number not too close to a power of 2
        mod = 1
        return key % mod

    def _universalHash(self, key):
        # * Randomly select between multiplication and division
        pass

    def insert(self, key, value):
        # 1. Increment size

        self.size += 1
        # 2. Compute index of key

        index = self.hash(key)
        # Go to the node corresponding to the hash

        node = self.buckets[index]
        # 3. If bucket is empty:

        if node is None:
            # Create node, add it, return

            self.buckets[index] = Node(key, value)
            return

        # 4. Collision! Iterate to the end of the linked list at provided index
        # * This allows for duplicate keys which is a no go in hash tables
        prev = node
        while node is not None:
            prev = node
            node = node.next
        # Add a new node at the end of the list with provided key/value

        prev.next = Node(key, value)

    def search(self, key):
        # 1. Compute hash

        index = self.hash(key)
        # 2. Go to first node in list at bucket

        node = self.buckets[index]
        # 3. Traverse the linked list at this node

        while node is not None and node.key != key:
            node = node.next
        # 4. Now, node is the requested key/value pair or None

        if node is None:
            # Not found

            return None
        else:
            # Found - return the data value

            return node.value

    def delete(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            return

        if node.key == key:
            node = node.next
            self.buckets[index] = node
            return

        prev = node
        while node and node.key != key:
            prev = node
            node = node.next

        prev.next = node.next if node else None
        self.buckets[index] = prev


print()
hashTable = HashTable()
print(f"The empty hash table is:\n{ hashTable }\n")

hashTable.insert('one', 1)
print(f"One entry table is:\n{ hashTable }\n")

# hashTable.insert('one', 2)
# print(f"Two entry table is { hashTable }")
# # ! This won't work the key would have to be an iterable (str/list)
# # ! hashTable.insert(2, 'two')
# one = hashTable.search('one')
# print(f"searching for one: { one }")

hashTable.delete('one')
print(f"The table should be empty now:\n{ hashTable }")
