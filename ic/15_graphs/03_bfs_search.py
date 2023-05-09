# 03
# Medium

# BFS: Given a graph and a target number T, find if T exists in the graph.


# -----------------------------------------------------

# Time Complexity: O(V + E)
# Space Complexity: O(V)
# We can store at most V nodes on the Queue, and we also use V space to store the state
# of each node.

# 3:43

from collections import deque

class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.relations = []
        self.visited = False

    def __repr__(self) -> str:
        return str(self.data)

class Graph(object):
    def __init__(self):
        self.nodes = []

    def reset(self) -> None:
        for n in self.nodes:
            n.visited = False

    def contains(self, v: int) -> bool:
        for node in self.nodes:
            if node.visited:
                continue
            q = deque()
            q.appendleft(node)
            while q:
                n = q.pop()
                if n.data == v:
                    return True
                n.visited = True
                for r in node.relations:
                    if not r.visited:
                        q.appendleft(r)
        return False

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

import pytest

def test_graph_contains():
    assert(g.contains(25))
    g.reset()
    assert(not g.contains(31))
    g.reset()
    assert(not g.contains(1))
    g.reset()
    assert(g.contains(5))

pytest.main()
