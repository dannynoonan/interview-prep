# 05
# Medium
    
# Find Successor: Given a Node N in a BST, find the node with the next largest value, also
# known as the successor of the node.


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

    def find_successor(self, target: int) -> int:
        last_with_left = None
        node = self.root
        while node:
            if target < node.data:
                if node.left:
                    last_with_left = node
                    node = node.left
                else:
                    return node.data
            else:
                if node.right:
                    node = node.right
                else:
                    if last_with_left:
                        return last_with_left.data
                    else:
                        raise Exception(f"No successor found for node={target}")


"""
              9
           /     \
        3           13
      /   \       /    \
    1       7   11      17
           /           /  \
          5          15    19
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
    assert(bt.find_successor(7) == 9)
    assert(bt.find_successor(11) == 13)
    assert(bt.find_successor(13) == 15)
    assert(bt.find_successor(2) == 3)  # unclear if this should work or raise exception
    with pytest.raises(Exception):
        bt.find_successor(19)

pytest.main()
