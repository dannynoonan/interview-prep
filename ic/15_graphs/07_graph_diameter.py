# 07
# Medium

# Diameter of a Graph: Given a directed graph, find the length of the longest path in the graph.


# -----------------------------------------------------

# Time Complexity: O(V+E)
# Space Complexity: O(V)

# TODO I think this is right, but it doesn't use topo_sort directly the way previous solutions did, so might need to be verified

class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.relations = []
        self.max_depth = None

    def __repr__(self) -> str:
        return str(self.data)

    def get_depth(self) -> int:
        if self.max_depth:
            return self.max_depth
        max_depth = 0
        for r in self.relations:
            depth = r.get_depth() + 1
            max_depth = max(max_depth, depth)
        self.max_depth = max_depth
        return max_depth

class Graph(object):
    def __init__(self):
        self.nodes = []

    def reset(self) -> None:
        for n in self.nodes:
            n.max_depth = None

    def diameter(self) -> int:
        max_depth = 0
        for n in self.nodes:
            max_depth = max(max_depth, n.get_depth())
        return max_depth

# -----------------------------------------------------

import pytest

def test_topo_sort():
    n1 = Node(5)
    n2 = Node(10)
    n3 = Node(15)
    n4 = Node(20)
    n5 = Node(25)
    n6 = Node(30)
    n7 = Node(35)
    n8 = Node(40)

    n1.relations = [n2,n3]
    n2.relations = [n4]
    n3.relations = [n4,n5]
    n4.relations = [n6]
    n5.relations = [n6]

    g = Graph()
    g.nodes = [n1,n2,n3,n4,n5,n6,n7,n8]
    assert(g.diameter() == 3)

    g.reset()
    n6.relations = [n7]
    assert(g.diameter() == 4)

    g.reset()
    n7.relations = [n8]
    assert(g.diameter() == 5)

pytest.main()
    