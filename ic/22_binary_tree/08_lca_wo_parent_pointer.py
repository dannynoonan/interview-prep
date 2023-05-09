# 08
# Medium

# LCA without Parent Pointer: 
# How will you find the LCA if you don't have a parent pointer?


# -----------------------------------------------------

# Time Complexity:​ O(n), where n is the number of nodes
# Space Complexity:​ O(height), used on the recursion stack

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

    def lca(self, n1: Node, n2: Node) -> Node:
        return find_lca(self.root, n1, n2)

def find_lca(node: Node, n1: Node, n2: Node) -> Node|None:
    if not node:
        return None
    if node == n1 or node == n2:
        return node
    left = find_lca(node.left, n1, n2)
    right = find_lca(node.right, n1, n2)
    if left and right:
        return node
    if left:
        return left
    if right:
        return right
    return None

# -----------------------------------------------------

"""
            1
         /     \
       2         3
     /   \ 
    4     5
   /    / 
  8   6
 /   /
9   7
"""

import pytest

def test_find_lca():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n5.left = n6
    n6.left = n7
    n4.left = n8
    n8.left = n9
    bt = BinaryTree(n1)
    assert(bt.lca(n9, n6) == n2)
    assert(bt.lca(n3, n4) == n1)
    assert(bt.lca(n8, n9) == n8)
    assert(bt.lca(n7, n2) == n2)

pytest.main()
