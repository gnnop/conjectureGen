import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

# A function to check if two graphs are isomorphic
def isomorphic(G1, G2):
    return GraphMatcher(G1, G2).is_isomorphic()

# A function to enumerate non-isomorphic graphs
def enumerate_graphs(n):
    # Create a list of all possible edges in a complete graph of size n
    edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    graphs = []
    for i in range(2**(len(edges))):
        # Convert the binary representation of i to a set of edges
        graph_edges = set([edges[j] for j in range(len(edges)) if (i & (2**j))])
        # Create a graph from the set of edges
        G = nx.Graph()
        G.add_nodes_from(range(n))
        G.add_edges_from(graph_edges)
        # Check if the graph is isomorphic to any previously generated graphs
        is_isomorphic = False
        for H in graphs:
            if isomorphic(G, H):
                is_isomorphic = True
                break
        # If the graph is not isomorphic to any previously generated graphs, add it to the list
        if not is_isomorphic:
            graphs.append(G)
    return graphs

# Test the function with n=3
graphs = enumerate_graphs(3)
for G in graphs:
    print(nx.adjacency_matrix(G).todense())






"""
The top most important numerical properties of a mathematical graph made up of edges and vertices are:
the chromstic number,
the degree of each vertex,
the order of the graph,
the number of edges,
the number of vertices,
the shortest path between two vertices,
the eccentricity of a vertex,
the radius,
the diameter of the graph,
the girth of the graph,
the connectivity of the graph,
the cuts of the graph,
the independence number of the graph,
the clique number of the graph,
the graph's planarity,
the degree sequence of the graph,
the traversal cost of the graph,
the average degree of the graph,
the average clustering coefficient,
the average path length
"""


