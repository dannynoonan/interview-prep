# 03
# Easy

# Find the height of a binary tree.


# -----------------------------------------------------

# Time Complexity:​ O(n) where n is the number of nodes
# Space Complexity:​ O(h) where h is the height of the tree. Space is used on the recursion stack.

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

    def height(self, type: str) -> int:
        if type == 'top_down':
            return tree_height_top_down(self.root, 0)
        if type == 'bottom_up':
            return tree_height_bottom_up(self.root)

def tree_height_top_down(node: Node, depth: int) -> int:
    if not node:
        return depth
    left_depth = tree_height_top_down(node.left, depth+1)
    right_depth = tree_height_top_down(node.right, depth+1)
    return max(left_depth, right_depth)

def tree_height_bottom_up(node: Node) -> int:
    if not node:
        return 0
    left_depth = tree_height_bottom_up(node.left)
    right_depth = tree_height_bottom_up(node.right)
    return max(left_depth, right_depth) + 1

# -----------------------------------------------------

import pytest

def test_height():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    bt = BinaryTree(n1)
    assert(bt.height("top_down") == 3)
    assert(bt.height("bottom_up") == 3)

    n8 = Node(8)
    n7.left = n8
    n9 = Node(9)
    n8.left = n9
    assert(bt.height("top_down") == 5)
    assert(bt.height("bottom_up") == 5)

    n8.left = None
    n7.right = n9
    assert(bt.height("top_down") == 4)
    assert(bt.height("bottom_up") == 4)

pytest.main()
