# 01
# Medium

# Is BST: Given a Binary Tree, determine if it is a Binary Search Tree (BST).


# -----------------------------------------------------

# Time Complexity:​ O(n)
# Space Complexity:​ O(h) on recursion stack

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

    def is_bst(self) -> bool:
        if is_bst_dfs(self.root, 0, 1000):
            return True
        return False

def is_bst_dfs(node: Node, low: int, high: int) -> bool:
    if not node:
        return True
    if node.data < low or node.data > high:
        return False
    if is_bst_dfs(node.left, low, node.data) and is_bst_dfs(node.right, node.data, high):
        return True
    return False

# a previous answer with some upside
# def is_bst_dfs_alt(node, low, high):
#     if node.data < low or node.data > high:
#         return False
#     if node.left:
#         if not is_bst_dfs_alt(node.left, low, node.data):
#             return False
#     if node.right:
#         if not is_bst_dfs_alt(node.right, node.data, high):
#             return False
#     return True


# -----------------------------------------------------

"""
              5
           /     \
        3           8
      /   \       /    \
    2       4   6        10
   /             \      /  \
  1               7    9    11
"""

import pytest

def test_is_bst():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    n11 = Node(11)
    n5.left = n3
    n5.right = n8
    n3.left = n2
    n3.right = n4
    n2.left = n1
    n8.left = n6
    n8.right = n10
    n6.right = n7
    n8.right = n10
    n10.left = n9
    n10.right = n11
    bt = BinaryTree(n5)
    assert(bt.is_bst())

    n6.right = False
    n6.left = n7
    assert(not bt.is_bst())

pytest.main()
