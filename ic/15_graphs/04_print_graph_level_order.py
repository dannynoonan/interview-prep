# 04
# Easy

# Print Graph in Level Order: Given a graph and a node N, print the Graph in order of distance
# from N. Each level should be in a new line.

# For example,
# All nodes of distance 1 from N
# All nodes of distance 2 from N, etc.

# Similar Problem: Print a tree in level order


# -----------------------------------------------------

# Time Complexity:​ O(V+E)
# Space Complexity:​ O(V)

from collections import deque

class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.relations = []
        self.visited = False
        self.level = None

    def __repr__(self) -> str:
        return str(self.data)

class Graph(object):
    def __init__(self):
        self.nodes = []

    def reset(self) -> None:
        for n in self.nodes:
            n.visited = False

    def print_level_order(self, node: Node) -> None:
        q = deque()
        last_level = 0
        print(f'-------- LEVEL 0 -----------------')
        node.level = last_level
        q.appendleft(node)
        while q:
            n = q.pop()
            if n.visited:
                continue
            if n.level > last_level:
                print(f'-------- LEVEL {n.level} -----------------')
                last_level = n.level
            print(n.data)
            n.visited = True
            for r in n.relations:
                r.level = n.level + 1
                q.appendleft(r)

# -----------------------------------------------------

n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n4 = Node(20)
n5 = Node(25)
n6 = Node(30)

n1.relations = [n2,n3]
n2.relations = [n4]
n3.relations = [n4,n5]
n4.relations = [n6]
n5.relations = [n6]
        
g = Graph()
g.nodes = [n1,n2,n3,n4,n5,n6]

g.print_level_order(n1)
        