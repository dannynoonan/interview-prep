# 06
# Hard

# Sort a graph in topological order.


# -----------------------------------------------------

# Time Complexity: O(V + E), where V is vertices (nodes) and E is edges.
# Space Complexity: O(V)

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

def topo_sort(g: Graph) -> list:
    g.reset()
    s = []
    for node in g.nodes:
        topo_sort_dfs(node, s)
    return s

def topo_sort_dfs(node: Node, s: list) -> None:
    if not node.visited:
        for r in node.relations:
            topo_sort_dfs(r, s)
        node.visited = True
        s.append(node)

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

def test_topo_sort():
    assert(topo_sort(g) == [n6, n4, n2, n5, n3, n1]) # [30, 20, 10, 25, 15, 5]

pytest.main()
