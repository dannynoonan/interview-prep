# 07
# Easy

# LCA: Given two nodes A and B in a Binary Search Tree, find the lowest common ancestor.


# -----------------------------------------------------

# Time Complexity: O(h)
# Space Complexity: O(1)

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

def lca(node: Node, n1: Node, n2: Node) -> Node:
    if not node:
        raise Exception("node was None")
    if node.data < n1.data and node.data < n2.data:
        return lca(node.right, n1, n2)
    if node.data > n1.data and node.data > n2.data:
        return lca(node.left, n1, n2)
    return node

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

    assert(lca(bt.root, n15, n7) == n9)
    assert(lca(bt.root, n5, n1) == n3)
    assert(lca(bt.root, n19, n11) == n13)
    assert(lca(bt.root, n5, n7) == n7)
    assert(lca(bt.root, n19, n9) == n9)

pytest.main()
