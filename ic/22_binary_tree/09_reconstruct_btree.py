# 09
# Hard

# Given inorder and preorder traversals of a binary tree, reconstruct the binary tree.


# -----------------------------------------------------

# Time Complexity: O(n) worse case, if the tree was like a chain
# Space Complexity: O(n) worse case, if the tree was like a chain

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
    def __init__(self, root: Node = None):
        self.root = root

def build_preorders_to_inorders(preorder: list, inorder: list) -> dict:
    preorders_to_inorders = {k:None for k in preorder}
    for i in range(len(inorder)):
        preorders_to_inorders[inorder[i]] = i
    return preorders_to_inorders

def reconstruct_btree(preorder: list, inorder: list) -> BinaryTree:
    btree = BinaryTree()
    preorders_to_inorders = build_preorders_to_inorders(preorder, inorder)
    btree.root = build_tree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, preorders_to_inorders)
    return btree

def build_tree(preorder: list, preorder_low: int, preorder_high: int, inorder: list, inorder_low: int, inorder_high: int, preorders_to_inorders: dict) -> Node:
    if preorder_low > preorder_high:
        return None

    node_val = preorder[preorder_low]
    node = Node(node_val)
    inorder_mid = preorders_to_inorders[node_val]

    left_span = inorder_mid - inorder_low

    inorder_left_high = inorder_low + left_span - 1
    inorder_right_low = inorder_low + left_span + 1

    left_preorder_low = preorder_low + 1
    left_preorder_high = preorder_low + left_span
    right_preorder_low = preorder_low + left_span + 1
    right_preorder_high = preorder_high

    node.left = build_tree(preorder, left_preorder_low, left_preorder_high, inorder, inorder_low, inorder_left_high, preorders_to_inorders)
    node.right = build_tree(preorder, right_preorder_low, right_preorder_high, inorder, inorder_right_low, inorder_high, preorders_to_inorders)
    
    return node

# -----------------------------------------------------

"""
             1
      2            3
   4     5      6      7
 8   9    10  11    

"""

import pytest

def test_reconstruct_btree():
    preorder = [1,2,4,8,9,5,10,3,6,11,7]
    inorder = [8,4,9,2,5,10,1,11,6,3,7]
    btree = reconstruct_btree(preorder, inorder)
    assert(btree.root == Node(1))
    assert(btree.root.left.left == Node(4))
    assert(btree.root.left.left.right == Node(9))
    assert(btree.root.left.left.right.left is None)
    assert(btree.root.left.right.right == Node(10))
    assert(btree.root.right.left.left == Node(11))
    assert(btree.root.right.right == Node(7))
    assert(btree.root.right.right.right is None)

pytest.main()
