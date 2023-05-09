# 01 
# Medium

# Given a graph, find if there is a cycle.


# -----------------------------------------------------

# Time Complexity: O(V + E)
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

def detect_cycle(g: Graph) -> bool:
    for n in g.nodes:
        if detect_cycle_dfs(n):
            return True
    return False

def detect_cycle_dfs(n: Node) -> bool:
    if n.visited:
        print(f"n={n} already visited")
        return True
    n.visited =  True
    for r in n.relations:
        if detect_cycle_dfs(r):
            return True
    n.visited = False
    return False

# -----------------------------------------------------

import pytest

def test_detect_cycle():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    n11 = Node(11)

    n1.relations = [n2,n4]
    n2.relations = [n3]
    n3.relations = [n5,n6]
    n4.relations = [n2,n5,n7]
    n5.relations = [n7,n8,n11]
    n6.relations = [n8]
    n7.relations = [n9,n10]
    n8.relations = [n7,n10]
    n9.relations = [n10,n11]
    n10.relations = [n11]
        
    g = Graph()
    g.nodes = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11]
    assert(not detect_cycle(g))

    g.reset()
    n11.relations = [n2]
    assert(detect_cycle(g))

    g.reset()
    n11.relations = []
    assert(not detect_cycle(g))
    
pytest.main()
