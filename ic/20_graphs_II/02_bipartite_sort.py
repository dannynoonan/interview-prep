# 02
# Hard

# Given a graph, separate nodes into 2 groups, such that no 2 nodes in the same group have an edge.

# Note 4/29/23: OK here's the deal: these graphs are bidirectional, hence anything connected to anything
# will be revealed in a single pass using any starting node.  To make things clearer, we can start with a 
# "source" or "root" node, but theoretically this can be any node.

# Note 3/9/21: Separate them into 2 groups *if possible*, i.e. validate whether graph is bipartite or not.
# Note 3/9/21: And I'm pretty sure we can assume we start with a "main node" rather re-processing every node in graph 
# Note 6/3/21: If we do re-process every node in graph, as with my 4/24 solution, you can 100% solve for bipartite, though you can't 
# easily sort by color (unless you employ some "temp" color I haven't tried) and/or you increase the time complexity to O(V+E)^2 
# I believe. Maybe relations are supposed to be bidirectional?)

# Alternative Phrasing 1: 
# 2 Color Problem: Given a graph, color its nodes with 2 colors - red and blue - such that
# no 2 neighbors have the same color.

# Alternative Phrasing 2:
# Let's say you have invited a group of people to your house for a party. You make a graph where
# a node is a person and an edge between 2 people means that they know each other.
# You want to separate them into 2 groups such that in each group, no one knows each other.
# Determine if such a grouping is possible, and if so, make the 2 groups.


# -----------------------------------------------------

# Time Complexity: O(V+E)
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

from collections import deque

def toggle(group: int) -> int:
    if group == 1:
        return 2
    return 1

def is_bipartite(g: Graph, start: Node) -> bool:
    node_group_map = {n: None for n in g.nodes}
    node_group_map[start] = 1
    q = deque()
    q.appendleft(start)
    while q:
        n = q.pop()
        n_group = node_group_map[n]
        for r in n.relations:
            r_group = toggle(n_group)
            if not node_group_map[r]:
                node_group_map[r] = r_group
                q.appendleft(r)
            if node_group_map[r] and node_group_map[r] == n_group:
                return False
    return True
            
# -----------------------------------------------------

import pytest

def test_is_bipartite():
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n0.relations = [n1,n3]
    n1.relations = [n0,n4,n5]
    n2.relations = [n5]
    n3.relations = [n0]
    n4.relations = [n1,n6]
    n5.relations = [n1,n2,n6]
    n6.relations = [n4,n5]
        
    g = Graph()
    g.nodes = [n0,n1,n2,n3,n4,n5,n6]
    assert(is_bipartite(g, n0))

    n1.relations.append(n2)
    n2.relations.append(n1)
    assert(not is_bipartite(g, n0))

pytest.main()
