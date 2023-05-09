# 05 
# Easy

# Given a binary tree, determine if it is balanced


# -----------------------------------------------------

# Time Complexity:​ O(n)
# Space Complexity:​ O(height) on recursion stack

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

    def is_balanced(self) -> bool:
        if is_balanced_dfs(self.root) > 0:
            return True
        return False

def is_balanced_dfs(node: Node) -> int:
    if not node:
        return 1
    left_depth = is_balanced_dfs(node.left)
    right_depth = is_balanced_dfs(node.right)
    if left_depth == -1 or right_depth == -1:
        return -1
    if abs(left_depth - right_depth) > 1:
        return -1
    return max(left_depth, right_depth) + 1

# -----------------------------------------------------

import pytest

def test_is_balanced():
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
    n3.left = n6
    n3.right = n7
    n4.left = n8
    bt = BinaryTree(n1)
    assert(bt.is_balanced())

    n8.left = n9
    assert(not bt.is_balanced())

pytest.main()
