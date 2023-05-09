# 01 
# Easy

# Traverse the binary Tree inorder, postorder and preorder.


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree

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

def traverse(btree: BinaryTree, type: str) -> None:
    if type == "inorder":
        in_order_traverse(btree.root)
    if type == "postorder":
        post_order_traverse(btree.root)
    if type == "preorder":
        pre_order_traverse(btree.root)

def in_order_traverse(node: Node) -> None:
    if node.left:
        in_order_traverse(node.left)
    print(node)
    if node.right:
        in_order_traverse(node.right)

def pre_order_traverse(node: Node) -> None:
    print(node)
    if node.left:
        pre_order_traverse(node.left)
    if node.right:
        pre_order_traverse(node.right)

def post_order_traverse(node: Node) -> None:
    if node.left:
        post_order_traverse(node.left)
    if node.right:
        post_order_traverse(node.right)
    print(node)

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

>>> traverse(bt, 'inorder')
4
2
5
1
6
3
7

>>> traverse(bt, 'preorder')
1
2
4
5
3
6
7

>>> traverse(bt, 'postorder')
4
5
2
6
7
3
1
"""
    