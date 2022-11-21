from copy import deepcopy
from Few import count_reds_in_path,does_graph_contain_cycle
import sys
from utils import is_undirected, dijkstra, graph_to_nx
import networkx as nx

sys.setrecursionlimit(10000)
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
        #print("found path")
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
    visited = deepcopy(G)
    path = []
    for node in visited:
        visited[node] = False
    if is_undirected(G) == True:
        if count_reds_in_graph(G) > 0:
            return float("inf")
        else:
            res = dijkstra(G)
            if res[s][t] != float("inf"): # if infinite, no path was found
                return 0 # path exists with no reds
            else:
                return -1
    else:
        if not does_graph_contain_cycle(G):
            # DAG
            # find all paths from s to t
            global max_red_path
            max_red_path = 0
            max_count = count_reds_in_graph(G)
            try:
                find_all_paths_dfs(G, s, t, visited, path, max_count)
                return max_red_path
            except ManyRedException:
                return max_count
            # find the max number of reds in any path
        else:
            # Directed Cyclic world
            # remove cycles
            # find all cycles
            list_of_cycles = nx.simple_cycles(graph_to_nx(G))
            for cycle in list_of_cycles:
                #remove edge from last element to first element
                G[cycle[-1]].remove(cycle[0])
            # find all paths from s to t
            # find the max number of reds in any path
    pass