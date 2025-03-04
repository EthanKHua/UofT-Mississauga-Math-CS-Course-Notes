'''
CSC263 Winter 2025
Problem Set 3 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any additional "import" statements
from math import floor

#############################################
# Hash table
###############################################

# Placeholder for a deleted element
DELETED = "DELETED"

# Element in the HashTable
class Node(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v

class HashTable(object):
    """
    A hash table object. Each hash table will have the
    following fields:
        array:    The address table, represented as a list in Python.
                  The values of this address table is either None,
                  DELETED, or a Node object
        capacity: The current size of the address table
        size:     The number of elements in the table.
    """
    def __init__(self, initial_capacity=10):
        # Hash table capacity
        self.capacity = initial_capacity
        self.initial_capacity = initial_capacity

        # Initialize the address table to have all "None"
        # This table should have elements None, "DELTED", or a Node object
        self.array = [None] * initial_capacity

        # Track the number of elements in the hash table
        self.size = 0

    def hash(self, k, capacity=None):
        """
        Hash function that returns a bucket {0, 1, 2, ..., capacity-1} given
        a key `k`. The argument `capacity` is initialized to `self.capacity`,
        but an alternative capacity can be provided.

        This function is provided to you.
        """
        A = 0.6387390215
        if capacity is None:
            capacity = self.capacity
        return floor(capacity * (hash(k) * A % 1))

    def find(self, arr, cap, k):
        """
        Find the index of the node with key k within arr with capacity cap. If key is not present, returns the index of
        an empty spot where a new node with key k should be inserted.
        """
        i = 0
        first_delete_index = -1
        hashed = self.hash(k, cap)
        while arr[(hashed + i * i) % cap]:
            if arr[(hashed + i * i) % cap] == DELETED:
                if first_delete_index == -1:
                    first_delete_index = (hashed + i * i) % cap
            elif arr[(hashed + i * i) % cap].key == k:
                return (hashed + i * i) % cap
            i += 1
        
        return (hashed + i * i) % cap if first_delete_index == -1 else first_delete_index

    def rehash(self, new_capacity):
        """
        Reinsert the existing elements in the current array into a new array with
        the given new capacity
        """
        new_arr = [None] * new_capacity
        for node in self.array:
            if node is None or node == DELETED:
                continue
            new_arr[self.find(new_arr, new_capacity, node.key)] = node
        self.array = new_arr
        self.capacity = new_capacity

    def insert(self, k, v):
        """
        Insert Node(k, v) into the hash table. Use the hash function self.hash(),
        and quadratic probing if the slot is already occupied.

        If the key `k` already exists in the Hash Table, replace the coresponding
        value `v`.

        If the hash table capacity is >= 50%, double the hash table capacity.
        """
        # insert new element
        insert_index = self.find(self.array, self.capacity, k)
        if self.array[insert_index] is None or self.array[insert_index] == DELETED:
            self.size += 1
        self.array[insert_index] = Node(k, v)

        # if hash table capacity is above half, double array capacity and rehash all the elements
        if self.size >= self.capacity / 2:
            self.rehash(self.capacity * 2)

    def search(self, k):
        """
        Return the value of the node with key k in the hash table,
        or None if no such node exists.
        """
        index = self.find(self.array, self.capacity, k) # possible index of node
        if not self.array[index] or self.array[index] == DELETED:
            return None
        return self.array[index].val

    def delete(self, k):
        """
        Delete the node with key `k` from the hash table, if it exists.

        If the hash table capacity is <= 25%, halve the hash table capacity,
        but do not go below self.initial_capacity
        """
        index = self.find(self.array, self.capacity, k) # index candidate for node
        if self.array[index] is None or self.array[index] == DELETED:
            return
        self.array[index] = DELETED
        self.size -= 1
        if self.size <= self.capacity / 4 and self.initial_capacity < self.capacity:
            self.rehash(self.capacity // 2)

    # You may write helper functions freely


# You may add additional test case below. HOWEVER, your code must
# compile and be runnable in order to earn any credit for correctness.

if __name__ == "__main__":
    T = HashTable(5)
    T.insert(1, "c")
    T.delete(1)
    # check that the DELTETED token is used
    assert T.array[T.hash(1)] == DELETED 

    T.insert(1, "c")
    T.insert(2, "s")

    # check that size and capacity are tracked correctly
    assert(T.size == 2)
    assert(T.capacity == 5)

    T.insert(3, "c")

    # check that size and capacity are tracked correctly
    assert(T.size == 3)
    assert(T.capacity == 10)

    # check that search gives us the appropriate result
    n = T.search(1)
    assert(n == "c")

    for i in range(100):
        T.insert(i, i)
        assert(T.search(i) == i)
    assert(T.size == 100)
    assert(T.capacity == 320)
    for i in range(100):
        assert(T.search(i) == i)
    for i in range(100):
        T.delete(i)
        assert(not T.search(i))
        for j in range(i+1, 100):
            assert(T.search(j) == j)
    