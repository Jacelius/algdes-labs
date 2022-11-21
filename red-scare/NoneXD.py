from copy import deepcopy
from utils import dijkstra

# return the length of the shortest s, t path
# If no such path exists, return ‘-1’.
# has to avoid red nodes (nodes in R)e
def shortest_path(G, s, t, num_edges):
    if s == t:
        return 0
    if num_edges == 0: 
        return -1
    # check if t or r are red
    if G[t]["isRed"] or G[s]["isRed"]:
        return -1

    # Find shortest path from s to t, that avoids nodes in R
    # idea: remove nodes in R from G
    g_no_r = deepcopy(G)
    for node in G:
        if G[node]["isRed"]:
            g_no_r.pop(node)
    for node in g_no_r:
        for edge_target in G[node]:
            # remove all edges to red nodes
            if edge_target != "isRed" and G[edge_target]["isRed"]:
                g_no_r[node].pop(edge_target)
    
    # print("G, without red nodes: ", g_no_r)

    #check if s has an edge to t in order to skip dijkstra 
    if t in g_no_r[s]:
        return 1

    #Run dijkstra on g_no_r
    dist = dijkstra(g_no_r, s)
    if dist[t] == float('inf'):
        return -1
    return dist[t]



    