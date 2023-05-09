# 04
# Easy

# Given a Binary Tree, print all paths from root to leaf. For example, in the below tree:

#     A
#    / \
#   B   C
#  /   / \
# D   E   F

# Output:
# A -> B -> D
# A -> C -> E
# A -> C -> F


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree

class Node(object):
    def __init__(self, data: str):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return self.data

class BinaryTree(object):
    def __init__(self, root: Node = None):
        self.root = root

def print_all_paths(btree: BinaryTree) -> None:
    path = []
    print_path(btree.root, path)

def print_path(node: Node, path: list) -> None:
    path.append(node)
    if not node.left and not node.right:
        print(path)
    if node.left:
        print_path(node.left, path)
    if node.right:
        print_path(node.right, path)
    path.pop()

# -----------------------------------------------------

nA = Node('A')
nB = Node('B')
nC = Node('C')
nD = Node('D')
nE = Node('E')
nF = Node('F')

btree = BinaryTree(nA)
nA.left = nB
nA.right = nC
nB.left = nD
nC.left = nE
nC.right = nF

print_all_paths(btree)
