# 07
# Medium

# LCA with Parent Pointer: Given a Binary Tree and two Nodes A and B, find their lowest 
# common ancestor. Assume that each node has a pointer to its parent node.


# -----------------------------------------------------

# Time Complexity: O(h)
# Space Complexity: O(1)

class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.data)

class BinaryTree(object):
    def __init__(self, root: Node = None):
        self.root = root

def find_lca(n1: Node, n2: Node) -> Node:
    n1_tree = [n1]
    node = n1.parent
    while node:
        n1_tree.append(node)
        node = node.parent
    n2_tree = [n2]
    node = n2.parent
    while node:
        n2_tree.append(node)
        node = node.parent
    if len(n1_tree) > len(n2_tree):
        deeper = n1_tree
        shallower = n2_tree
    else:
        deeper = n2_tree
        shallower = n1_tree
    depth_diff = len(deeper) - len(shallower)

    deep_node = deeper[depth_diff]
    shallow_node = shallower[0]
    while deep_node:
        if deep_node == shallow_node:
            return deep_node
        deep_node = deep_node.parent
        shallow_node = shallow_node.parent
    raise Exception(f"No common ancestor found for n1={n1} n2={n2}")
        
     
# -----------------------------------------------------

"""
            1
         /     \
       2         3
     /   \      /
    4     5    7
   / \  
  8   6
 /
9
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
    n2.parent = n1
    n1.right = n3
    n3.parent = n1
    n2.left = n4
    n4.parent = n2
    n2.right = n5
    n5.parent = n2
    n4.right = n6
    n6.parent = n4
    n3.left = n7
    n7.parent = n3
    n4.left = n8
    n8.parent = n4
    n8.left = n9
    n9.parent = n8
    # bt = BinaryTree(n1)
    assert(find_lca(n8, n6) == n4)
    assert(find_lca(n9, n4) == n4)
    assert(find_lca(n5, n6) == n2)
    assert(find_lca(n8, n9) == n8)
    assert(find_lca(n7, n4) == n1)
    assert(find_lca(n6, n2) == n2)

pytest.main()
