from copy import deepcopy
import networkx as nx

def graph_to_nx(graph):
    G = nx.DiGraph()
    #Array containing all outlevel keys
    for node in graph:
        G.add_node(node)
        for edge_target in graph[node]:
            if edge_target != "isRed":
                G.add_edge(node, edge_target, weight=graph[node][edge_target])
    # print("nx Graph", G)
    return G

def dijkstra(G, s):
    dist = {}
    for node in G:
        dist[node] = float('inf')
    dist[s] = 0
    Q = set(G)
    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)
        for v in G[u]:
            if v != "isRed":
                alt = dist[u] + G[u][v]
                if alt < dist[v]:
                    dist[v] = alt
    return dist

def count_reds_in_path(G, path):
    count = 0
    for node in path:
        if G[node]["isRed"] == True:
            count += 1
    return count

def is_undirected(G):
    for node in G:
        for neighbor in G[node]:
            if neighbor != "isRed": # ignore isRed
                if node not in G[neighbor]:
                    return False
                return True
            
def is_cyclic_util(G, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
 
        for neighbour in G[v]:
            if neighbour != "isRed": # ignore isRed 
                if visited[neighbour] == False:
                    if is_cyclic_util(G,neighbour, visited, recStack) == True:
                        return True
                elif recStack[neighbour] == True:
                    return True
 
        recStack[v] = False
        return False
            
def does_graph_contain_cycle(G):
    visited = deepcopy(G)
    recstack = deepcopy(G)
    for node in visited:
        visited[node] = False
        recstack[node] = False
    for node in G:
        if visited[node] == False:
            if is_cyclic_util(G, node, visited, recstack) == True:
                return True
    return False