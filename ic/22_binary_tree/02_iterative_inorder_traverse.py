# 02
# Easy

# Implement inorder traversal iteratively instead of using recursion.


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(n)

# 9:21

class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None
        self.visited = False

    def __repr__(self) -> str:
        return str(self.data)

class BinaryTree(object):
    def __init__(self, root: Node = None):
        self.root = root

def inorder_traverse(btree: BinaryTree) -> None:
    s = []
    s.append(btree.root)
    while s:
        node = s.pop()
        if node.visited:
            print(node)
        else:
            node.visited = True
            if node.right:
                s.append(node.right)
            s.append(node)
            if node.left:
                s.append(node.left)

# -----------------------------------------------------

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

"""
        1
    2       3
  4   5   6   7

>>> inorder_traverse(bt)
4
2
5
1
6
3
7
"""
