from copy import deepcopy
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
            alt = dist[u] + G[u][v]
            if alt < dist[v]:
                dist[v] = alt
    return dist

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
    #Run dijkstra on g
    dist = dijkstra(g_no_r, s)
    # dist_s_to_t = dist[s][t]

    print("dist to t", dist[t])
    return dist[t]



    