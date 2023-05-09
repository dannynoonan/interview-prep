# 02
# Hard

# Clone a Graph: Given an directed graph, make a copy.

# Hint: The trick here is to maintain a map of old nodes to their corresponding new nodes. 
# This will ensure that any cycles are handled.

# Note: This can be solved with either DFS or BFS.


# -----------------------------------------------------

# Time Complexity:​ O(V+E)
# Space Complexity:​ O(V+E)

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

# -----------------------------------------------------

def clone_graph(g: Graph) -> Graph:
    g_clone = Graph()
    nodes_to_clones = {}
    for n in g.nodes:
        n_clone = Node(n.data)
        g_clone.nodes.append(n)
        nodes_to_clones[n] = n_clone
    # for n_clone in g_clone.nodes:
    for n in g.nodes:
        for r in n.relations:
            nodes_to_clones[n].relations.append(nodes_to_clones[r])
    return g_clone

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

def test_clone_graph():
    g_clone = clone_graph(g)
    assert(g_clone.nodes == g.nodes)
    # TODO I'm not sure the sequence is deterministic...
    assert(g_clone.nodes[0].relations == g.nodes[0].relations)
    assert(g_clone.nodes[3].relations == g.nodes[3].relations)

pytest.main()
