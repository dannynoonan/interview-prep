# 01 
# Medium

# Given a graph, find if there is a cycle.


# -----------------------------------------------------

# 02
# Hard

# Given a graph, separate nodes into 2 groups, such that no 2 nodes in the same group have an edge.

# Note 3/9: Separate them into 2 groups *if possible*, i.e. validate whether graph is bipartite or not.
# Note 3/9: And I'm pretty sure we can assume we start with a "main node" rather re-processing every node in graph 
# Note 6/3: If we do re-process every node in graph, as with my 4/24 solution, you can 100% solve for bipartite, though you can't 
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

# 03
# Medium

# Given a graph, mark each connected component with a different color.
# Note 3/24: Every edge in the graph is bi-directional.


# -----------------------------------------------------
