# 03
# Medium

# Given a graph, mark each connected component with a different color.
# Note 3/24: Every edge in the graph is bi-directional.


# -----------------------------------------------------

# Time Complexity: O(V + E)
# Space Complexity: O(V)

class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.relations = []
        self.color = None
    
    def __repr__(self) -> str:
        return f"{self.data}:{self.color}"

class Graph(object):
    def __init__(self):
        self.nodes = []

    def reset(self) -> None:
        for n in self.nodes:
            n.color = None

colors = ['red','orange','yellow','green','blue','purple']

def mark_connected_components(g: Graph) -> None:
    color_i = 0
    for node in g.nodes:
        if not node.color:
            mark_component(node, colors[color_i])
            color_i += 1

def mark_component(node: Node, color: str) -> None:
    node.color = color
    for r in node.relations:
        if not r.color:
            mark_component(r, color)
        elif r.color and r.color != color:
            raise Exception(f"Foreign node color={r.color} found while marking component with {color}!")

# -----------------------------------------------------

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n1.relations = [n2]
n2.relations = [n1,n3]
n3.relations = [n2,n4]
n4.relations = [n3]
n5.relations = [n6]
n6.relations = [n5]
n7.relations = [n8]
n8.relations = [n7,n9]
n9.relations = [n8]
g = Graph()
g.nodes = [n4,n5,n6,n7,n8,n9,n1,n2,n3]

"""
>>> mark_connected_components(g)

>>> g.nodes
[4:red, 5:orange, 6:orange, 7:yellow, 8:yellow, 9:yellow, 1:red, 2:red, 3:red]
"""
