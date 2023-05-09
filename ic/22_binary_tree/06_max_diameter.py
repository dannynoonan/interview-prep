# 06
# Medium

# Find the Diameter of a Binary Tree. 
# The Diameter is the longest path from any 2 nodes in the tree. 


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

    def diameter(self) -> int:
        max_depth, max_diameter = max_diameter_dfs(self.root)
        return max_diameter

def max_diameter_dfs(node: Node) -> tuple:
    if not node:
        return 0, 0
    left_depth, left_max_diameter = max_diameter_dfs(node.left)
    right_depth, right_max_diameter = max_diameter_dfs(node.right)
    diameter = left_depth + right_depth
    max_diameter = max(left_max_diameter, right_max_diameter, diameter)
    return max(left_depth, right_depth) + 1, max_diameter
    
# -----------------------------------------------------

"""
            1
           / \
          2   3
         / \
        4   5
       /   /
      8   6
     /   /
    9   7
"""

import pytest

def test_tree_diameter():
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
    assert(bt.diameter() == 6)

    n6.left = None
    assert(bt.diameter() == 5)

    n6.left = n7
    n10 = Node(10)
    n7.right = n10
    assert(bt.diameter() == 7)

    n2.right = None
    assert(bt.diameter() == 5)

    n2.left = None
    assert(bt.diameter() == 2)

pytest.main()
