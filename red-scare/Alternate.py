# return True if there is a path from s to t that alternates between red and non-red nodes
# otherwise return False
# G is a graph
# s is a node in G
# t is a node in G
# R is a set of nodes in G
from copy import deepcopy

def dfs(G, s, t): # Depth first search that returns true if a path exists from s to t
    visited = set()
    stack = [s]
    while stack:
        node = stack.pop()
        if node == t:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in G[node]:
                if neighbor != "isRed":
                    stack.append(neighbor)
    return False

def build_graph(G):
    # make set of red nodes
    R_set = set()
    for node in G:
        if G[node]["isRed"]:
            R_set.add(node)
    not_red = set(G) - R_set # Build not_red set
    #build a graph with red and non-red nodes alternating
    G2 = deepcopy(G)
    for node in G:
        if G[node]["isRed"]:
            for neighbor in G[node]:
                if neighbor != "isRed":
                    if G[neighbor]["isRed"]:
                        G2[node].pop(neighbor)
    #Remove all edges from non-red nodes to non-red nodes
    for node in G:
        if node in not_red:
            for neighbor in G[node]:
                if neighbor in not_red:
                    G2[node].pop(neighbor)
    return G2

def path_exists_alternating_red(G, s, t):
    Graph = build_graph(G)
    return dfs(Graph, s, t)
    
