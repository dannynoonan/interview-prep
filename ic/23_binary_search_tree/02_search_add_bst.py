# 02 
# Easy

# Implement operations to Search for a node and Add a node into a Binary Search Tree.


# -----------------------------------------------------

# Time Complexity: O(h) for Search, Add, Delete
# Space Complexity:: O(1) space for Add and Delete, O(h) space on the recursion stack for Search

class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.data)

class BinaryTree(object):
    def __init__(self, root: Node = None):
        self.root = root

    def contains(self, data: int) -> bool:
        node = self.root
        while node:
            if data == node.data:
                return True
            if data < node.data:
                node = node.left
            else:
                node = node.right
        return False

    def add(self, data: int) -> None:
        node = self.root
        while node:
            if data == node.data:
                raise Exception(f"Unable to add, tree already contains data={data}")
            if data < node.data:
                if not node.left:
                    node.left = Node(data)
                    return
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = Node(data)
                    return
                else:
                    node = node.right
        
# -----------------------------------------------------
    
"""
              9
           /     \
        3           13
      /   \       /    \
    1       7   11       17
           /            /  \
          5           15    19
"""

import pytest

def test_search_add_bst():
    n1 = Node(1)
    n3 = Node(3)
    n5 = Node(5)
    n7 = Node(7)
    n9 = Node(9)
    n11 = Node(11)
    n13 = Node(13)
    n15 = Node(15)
    n17 = Node(17)
    n19 = Node(19)
    n9.left = n3
    n9.right = n13
    n3.left = n1
    n3.right = n7
    n7.left = n5
    n13.left = n11
    n13.right = n17
    n17.left = n15
    n17.right = n19
    bt = BinaryTree(n9)
    assert(not bt.contains(4))
    assert(bt.contains(5))
    assert(not bt.contains(6))
    assert(bt.contains(7))

    bt.add(8)
    assert(bt.contains(8))
    assert(n7.right.data == 8)

    bt.add(10)
    assert(n11.left.data == 10)

    bt.add(25)
    bt.add(24)
    assert(n19.right.data == 25)
    assert(n19.right.left.data == 24)

pytest.main()
