from copy import deepcopy
from Few import count_reds_in_path,does_graph_contain_cycle
import sys
from utils import is_undirected, dijkstra, graph_to_nx
import networkx as nx

global max_red_path

class ManyRedException(Exception):
    pass

def find_all_paths_dfs(G, s, t, visited, path, max_count):
    global max_red_path
    visited[s]= True
    path.append(s)

    # If current vertex is same as destination, then print
    # current path[]
    # print("s, t: ", s, t)
    if s == t:
        # print("found path")
        red_count = count_reds_in_path(G, path)
        #print("current red count: ", red_count)
        if red_count == max_count:
            raise ManyRedException("We did it bois - We found the path")
        if red_count > max_red_path:
            max_red_path = red_count
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for v in G[s]:
            if v != "isRed": # ignore isRed
                if visited[v]== False:
                    find_all_paths_dfs(G, v, t, visited, path, max_count)
                    
    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[s]= False

def count_reds_in_graph(G):
    count = 0
    for v in G:
        if G[v]['isRed'] == True:
            count += 1
    return count

# Return the maximum number of red vertices on any path from s to t
def max_red_on_any_path(G, s, t):
    global max_red_path
    max_red_path = 0
    path = []
    g_nx = graph_to_nx(G)
    all_simple_paths = nx.all_simple_paths(g_nx, s, t, cutoff=30)
    for path in all_simple_paths:
        red_count = count_reds_in_path(G, path)
        if red_count > max_red_path:
            print("new max red path: ", max_red_path)
            max_red_path = red_count
