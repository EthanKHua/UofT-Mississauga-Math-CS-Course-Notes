'''
CSC263 Winter 2025
Problem Set 2 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements

###############################################
# BST Nodes.
###############################################

class Node(object):
    """
    A binary tree node object. Each node will have three fields:
        key:   the key stored in the node (a number)
        left:  the left subtree (a Node or None)
        right: the right subtree (a Node or None)

    Do not change this class
    """
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

example_bst = Node(5)
example_bst.left = Node(2)
example_bst.left.left = Node(1)
example_bst.left.right = Node(3)
example_bst.right = Node(9)


def range_sum_bst(root, low, high):
    """
    Return the sum of the node values within the specified range.
    
    """
    if root is None:
        return 0
    if root.key < low:
        return range_sum_bst(root.right, low, high)
    if root.key > high:
        return range_sum_bst(root.left, low, high)
    return root.key + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)


if __name__ == "__main__":
    # Simple test case for range_sum_bst

    # Using the "Node" to represent the binary tree:
    #          5
    #         ---
    #       2   9
    #   1   3

    # Calling range_sum_bst(root, 3, 9) should return the sum of the values 3, 5, and 9
    print(range_sum_bst(example_bst, 3, 9))
    pass

   
