'''
CSC263 Winter 2025
Problem Set 4 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements
# Do NOT use Python dictionaries


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
        return hash(k) % capacity

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

def can_visit_all_cities(numCities, dependencies):
    '''
      Pre:  numCities is the number of cities to be visited
            dependencies is a list of 2-tuples representing (city1,city2) with city1 can only be visited after city2
      Post: return whether visiting all cities is possible or not
    '''
    # convert dependencies into adjacency list
    dp = HashTable(2 * numCities)
    dep = HashTable(2 * numCities) # number of depend
    for d in dependencies:
        val = dp.search(d[0])
        if val is None:
            dp.insert(d[0], [d[1]])
        else:
            val.append(d[1])
    

    pass  # TODO: implement this function

if __name__ == '__main__':
    # some small test cases
    # Case 1
    numCities1: int = 25
    dependencies1 = [('reykjavik', 'stjohns'), ('limerick', 'dublin'), ('london', 'dublin'), ('brighton', 'london'),
                    ('heidelberg', 'frankfurt'),('frankfurt', 'london'), ('frankfurt', 'dublin'),
                    ('batam', 'singapore'), ('newcastle', 'sydney'),('sandiego', 'honolulu')]

    # Case 2
    numCities2: int = 10
    dependencies2 = [('paris','madrid'),('madrid','lisbon'),('lisbon','paris')]

    assert 1 == can_visit_all_cities(numCities1, dependencies1)
    assert 0 == can_visit_all_cities(numCities2, dependencies2)
