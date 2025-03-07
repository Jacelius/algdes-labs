from copy import deepcopy
from Few import count_reds_in_path,does_graph_contain_cycle
import sys
from utils import is_undirected, dijkstra, graph_to_nx, bellman_ford, remove_reverse_edges, bellman_ford
import networkx as nx

# Problem for many: 
# Return the maximum number of red vertices on any path from s to t
# Return the max number
# If no path exists from s-t return -1
# G_ex = 2

class ManyRedException(Exception):
    pass

def count_reds_in_graph(G):
    count = 0
    for v in G:
        if G[v]['isRed'] == True:
            count += 1
    return count

# Return the maximum number of red vertices on any path from s to t
def max_red_on_any_path_brute(G, s, t):
    max_red_path = 0
    g_nx = graph_to_nx(G)
    # print("g_nx", g_nx)
    all_simple_paths = nx.all_simple_paths(g_nx, s, t)
    # print("all simple paths", list(all_simple_paths))
    for path in all_simple_paths:
        red_count = count_reds_in_path(G, path)
        if red_count > max_red_path:
            max_red_path = red_count
            # print("new max red path: ", max_red_path)
    return max_red_path

def max_red_on_any_path(G, s, t):
    # edges to red nodes = -1 
    # edges to non-red nodes = 0
    # bellman ford to find shortest path
    new_G = deepcopy(G)
    for node in new_G:
        for edge_target in new_G[node]:
            if edge_target != 'isRed':
                if new_G[edge_target]['isRed'] == True:
                    new_G[node][edge_target] = -1
                else:
                    new_G[node][edge_target] = 0
    dist = bellman_ford(new_G, s)
    if dist[t] == float('inf'): # no path
        return -1
    return -dist[t] # negative distance is the number of red nodes in path

