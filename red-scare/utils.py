from copy import deepcopy
import networkx as nx
import time

class NegativeWeightCycleException(Exception):
    pass

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

def bfs(G,s,t,parent):
    visited = deepcopy(G)
    for node in visited:
        visited[node] = False
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.pop(0)
        for ind in G[u]:
            if ind != "isRed":
                if visited[ind] == False and G[u][ind] > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
    return True if visited[t] else False

def ford_fulkerson_max_flow(G, source, sink):
    # Create a residual graph and fill the residual graph with given capacities in the original graph as residual capacities in residual graph  
    # Residual graph where rGraph[i][j] indicates residual capacity of edge from i to j (if there is an edge. If rGraph[i][j] is 0, then there is not)
    rGraph = deepcopy(G)
    for u in rGraph:
        for v in rGraph[u]:
            if v != "isRed":
                rGraph[u][v] = G[u][v]
    # This array is filled by BFS and to store path
    parent = {}
    max_flow = 0 # There is no flow initially
    # Augment the flow while there is path from source to sink
    while bfs(rGraph, source, sink, parent):
        # Find minimum residual capacity of the edges along the path filled by BFS. Or we can say find the maximum flow through the path found.
        path_flow = float("Inf")
        s = sink
        while(s !=  source):
            path_flow = min(path_flow, rGraph[parent[s]][s])
            s = parent[s]
        # Add path flow to overall flow
        max_flow +=  path_flow
        # update residual capacities of the edges and reverse edges along the path
        v = sink
        while(v !=  source):
            u = parent[v]
            rGraph[u][v] -= path_flow
            rGraph[v][u] += path_flow
            v = parent[v]
    # Return the overall flow
    return max_flow

def remove_reverse_edges(G): # undirected --> directed
    for u in G:
        for v in G[u]:
            if v != "isRed":
                if u in G[v]:
                    G[v].pop(u) # remove reverse edge

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

def bellman_ford(G,s):
    dist = {}
    for node in G:
        dist[node] = float('inf')
    dist[s] = 0
    # Only find simple paths, meaning that we don't allow cycles
    for i in range(len(G)-1):
        for u in G:
            for v in G[u]:
                if v != "isRed":
                    if dist[u] != float('inf') and dist[u] + G[u][v] < dist[v]:
                        dist[v] = dist[u] + G[u][v]
    for u in G:
        for v in G[u]:
            if v != "isRed":
                if dist[u] != float('inf') and dist[u] + G[u][v] < dist[v]:
                    raise NegativeWeightCycleException
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

def is_DAG(G):
    if is_undirected(G):
        return False
    if does_graph_contain_cycle(G):
        return False
    return True
            
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