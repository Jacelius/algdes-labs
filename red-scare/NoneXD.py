from copy import deepcopy
from utils import dijkstra

# return the length of the shortest s, t path
# If no such path exists, return ‘-1’.
# has to avoid red nodes (nodes in R)e
def shortest_path(G, s, t, R, num_edges):
    if s == t:
        return 0
    if num_edges == 0: 
        return -1
    if t in R or s in R:
        return -1
    # Find shortest path from s to t, that avoids nodes in R
    # idea: remove nodes in R from G
    g_no_r = deepcopy(G)
    for node in R:
        g_no_r.pop(node)
    for node in g_no_r:
        for rnode in R:
            if rnode in g_no_r[node]:
                g_no_r[node].pop(rnode)
    # print("G, without red nodes: ", g_no_r)

    #check if s has an edge to t in order to skip dijkstra 
    if t in g_no_r[s]:
        return 1

    #Run dijkstra on g_no_r
    dist = dijkstra(g_no_r, s)
    if dist[t] == float('inf'):
        return -1
    return dist[t]



    