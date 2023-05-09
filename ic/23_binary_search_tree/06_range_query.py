# 06
# Medium

# Range Querying: Given a Binary Search Tree, find all the elements in the range [A..B], both A and
# B inclusive.


# -----------------------------------------------------

# Time Complexity: O(h)
# Space Complexity: O(r) list of nodes in range

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

    def find_element(self, data: int) -> Node:
        node = self.root
        while node:
            if data == node.data:
                return node
            if data < node.data:
                node = node.left
            else:
                node = node.right
        return None

    def find_successor(self, data: int) -> Node:
        node = self.root
        last_with_left = None
        while node:
            if data < node.data:
                if node.left:
                    last_with_left = node
                    node = node.left
                else:
                    return node
            else:
                if node.right:
                    node = node.right
                else:
                    if last_with_left:
                        return last_with_left
                    else:
                        # raise Exception(f"No successor to node={node}")
                        return None
        raise Exception(f"Problems finding successor for node={node}")
    

def find_elements_in_range(btree: BinaryTree, low: int, high: int) -> list:
    nodes_in_range = []
    low_node = btree.find_element(low)
    if low_node:
        nodes_in_range.append(low_node)
    while low < high:
        low_node = btree.find_successor(low)
        if low_node and low_node.data <= high:
            nodes_in_range.append(low_node)
            low = low_node.data
        else:
            break
    return nodes_in_range


# -----------------------------------------------------

"""
                         10
           5                            15
     3           7               12            20
   2           6                    13       17
                                           16
"""

import pytest

def test_find_elements_in_range():
    n2 = Node(2)
    n3 = Node(3)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n10 = Node(10)
    n12 = Node(12)
    n13 = Node(13)
    n15 = Node(15)
    n16 = Node(16)
    n17 = Node(17)
    n20 = Node(20)

    n10.left = n5
    n10.right = n15
    n5.left = n3
    n5.right = n7
    n3.left = n2
    n7.left = n6
    n15.left = n12
    n15.right = n20
    n12.right = n13
    n20.left = n17
    n17.left = n16
    bt = BinaryTree(n10)
    assert(find_elements_in_range(bt, 5, 13) == [n5, n6, n7, n10, n12, n13])
    assert(find_elements_in_range(bt, 0, 8) == [n2, n3, n5, n6, n7])
    assert(find_elements_in_range(bt, 15, 22) == [n15, n16, n17, n20])
    assert(find_elements_in_range(bt, 8, 9) == [])

pytest.main()