from copy import deepcopy
from utils import is_undirected, does_graph_contain_cycle, count_reds_in_path, dijkstra
import sys

class MinPathFound(Exception):
    pass


global least_red_path


def find_all_paths_dfs(G, s, t, visited, path, mincount):
    global least_red_path
    visited[s] = True
    path.append(s)

    # If current vertex is same as destination, then print
    # current path[]
    # print("s, t: ", s, t)
    if s == t:
        #print("found path")
        red_count = count_reds_in_path(G, path)
        #print("current red count: ", red_count)
        if red_count == mincount:
            # 0, 1, or 2 reds dependent on s and t
            raise MinPathFound("We found a MIN path")
        if red_count < least_red_path:
            least_red_path = red_count
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for v in G[s]:
            if v != "isRed":  # ignore isRed
                if visited[v] == False:
                    find_all_paths_dfs(G, v, t, visited, path, mincount)

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[s] = False


def min_red_on_any_path(G, s, t, num_nodes):
    mincount = 0
    if G[s]["isRed"] == True:
        mincount += 1
    if G[t]["isRed"] == True:
        mincount += 1
    if t in G[s]:  # s has a direct edge to t
        return mincount
    if not is_undirected(G) and not does_graph_contain_cycle(G):
        # print("Graph is DAG")
        global least_red_path
        least_red_path = sys.maxsize
        visited = deepcopy(G)
        paths = []
        for node in visited:
            visited[node] = False
        try:
            find_all_paths_dfs(G, s, t, visited, paths, mincount)
        except MinPathFound:
            return 0
        # print("all paths: ", all_paths)

        if least_red_path == sys.maxsize:  # no path found
            return -1
        else:
            # instead of counting reds in each path now, we could not store the paths and just store the amount of reds
            return least_red_path
    else:
        # print("graph is not DAG")
        return "???"


def min_red_on_any_path_dijkstra(G, s, t):
    # change graph edges to non-red nodes to be 0
    new_g = deepcopy(G)
    for node in new_g:
        for edge_target in new_g[node]:
            if edge_target != 'isRed':
                if new_g[edge_target]['isRed'] == True:
                    new_g[node][edge_target] = 1
                else:
                    new_g[node][edge_target] = 0
    dist = dijkstra(new_g, s)
    if dist[t] == float('inf'):  # no path
        return -1
    return dist[t]
