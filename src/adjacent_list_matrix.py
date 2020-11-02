"""
Below is a representation of the graph above in Python:
Notice that this adjacency list doesn't use any lists. 
The vertices collection is a dictionary which lets us access each collection of edges in O(1) constant time. 
Because a set contains the edges, we can check for edges in O(1) constant time.
"""

# class Graph:
#     def __init__(self):
#         self.vertices = {
#                             "A": {"B"},
#                             "B": {"C", "D"},
#                             "C": {"E"},
#                             "D": {"F", "G"},
#                             "E": {"C"},
#                             "F": {"C"},
#                             "G": {"A", "F"}
#                         }

"""
Here is the representation of the graph above in an adjacency matrix:
We represent this matrix as a two-dimensional array–a list of lists. 
With this implementation, we get the benefit of built-in edge weights. 
0 denotes no relationship, but any other value represents an edge label or edge weight. 
The drawback is that we do not have a built-in association between the vertex values and their index.

In practice, implementing both the adjacency list and adjacency matrix would contain more information by including Vertex and Edge classes
"""

# class Graph:
#     def __init__(self):
#         self.edges = [[0,1,0,0,0,0,0],
#                       [0,0,1,1,0,0,0],
#                       [0,0,0,0,1,0,0],
#                       [0,0,0,0,0,1,1],
#                       [0,0,1,0,0,0,0],
#                       [0,0,1,0,0,0,0],
#                       [1,0,0,0,0,1,0]]

#----------------------------Adjacency Lists and Matrix's----------------------

# """
# Add Vertex:
# """
# # Adjacency Matrix - O(V)
# for v in self.edges:
#   self.edges[v].append(0)
# v.append([0] * len(self.edges + 1))

# # Adjacency List - O(1)
# self.vertices["H"] = set()


# """
# Add Edge:
# """
# # Adjacency Matrix - O(1)
# self.edges[v1][v2] = 1

# # Adjacency List - O(1)
# self.vertices[v1].add(v2)


# """
# Remove Edge:
# """

# # Adjacency Matrix - O(1)
# self.edges[v1][v2] = 0

# # Adjancecy List - O(1)
# self.vertices[v1].remove(v2)


# """
# Find Edge:
# """

# # Adjacency Matrix - O(1)
# return self.edges[v1][v2] > 0

# # Adjacency List - O(1)
# return v2 in self.vertices[v1]


# """
# Get All Edges from Vertex:
# """

# # Adjacency Matrix - O(V)
# v_edges = []
# for v2 in self.edges[v]:
#     if self.edges[v][v2] > 0:
#         v_edges.append(v2)
# return v_edges

# # Adjacency List - O(1)
# return self.vertex[v]








