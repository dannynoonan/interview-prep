# 08
# Easy

# Given a sorted array, build a balanced Binary Search Tree with the elements of the array.


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(n) space used by the new tree

class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.data)

    def __eq__(self, other):
        if self.data == other.data:
            return True
        return False

class BinaryTree(object):
    def __init__(self, root: Node = None, s_arr: list = None):
        if root:
            self.root = root
        elif s_arr:
            self.root = build_bst_node(s_arr, 0, len(s_arr)-1)
        else:
            self.root = None

def build_bst_node(s_arr: list, low: int, high: int) -> BinaryTree:
    if low > high:
        return None
    mid = round((low + high) / 2)
    node = Node(s_arr[mid])
    node.left = build_bst_node(s_arr, low, mid-1)
    node.right = build_bst_node(s_arr, mid+1, high)
    return node

# -----------------------------------------------------

import pytest

def test_init_bst_from_sorted_arr():
    sorted_array = [2,5,8,9,12,16,21,22,23,35,47,90,117,267]
    bt = BinaryTree(s_arr=sorted_array)
    assert(bt.root == Node(21))
    assert(bt.root.left.right.left == Node(9))
    assert(bt.root.right.right.left == Node(90))
    assert(bt.root.right.right == Node(117))

pytest.main()
