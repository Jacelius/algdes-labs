from copy import deepcopy
from Few import count_reds_in_path,does_graph_contain_cycle
import sys
from utils import is_undirected, dijkstra, graph_to_nx
import networkx as nx

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