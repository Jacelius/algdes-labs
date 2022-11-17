from copy import deepcopy
import sys

class MinPathFound(Exception):
    pass
sys.setrecursionlimit(10000)
global least_red_path


def find_all_paths_dfs(G, s, t, visited, path, mincount):
    global least_red_path
    visited[s]= True
    path.append(s)

    # If current vertex is same as destination, then print
    # current path[]
    # print("s, t: ", s, t)
    if s == t:
        #print("found path")
        red_count = count_reds_in_path(G, path)
        #print("current red count: ", red_count)
        if red_count == mincount:
            raise MinPathFound("We found a MIN path") # 0, 1, or 2 reds dependent on s and t
        if red_count < least_red_path:
            least_red_path = red_count
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for v in G[s]:
            if v != "isRed": # ignore isRed
                if visited[v]== False:
                    find_all_paths_dfs(G, v, t, visited, path,mincount)
                    
    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[s]= False

def count_reds_in_path(G, path):
    count = 0
    for node in path:
        # print("node: ", node)
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

def isCyclicUtil(G, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
 
        for neighbour in G[v]:
            if neighbour != "isRed": # ignore isRed 
                if visited[neighbour] == False:
                    if isCyclicUtil(G,neighbour, visited, recStack) == True:
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
            if isCyclicUtil(G, node, visited, recstack) == True:
                return True
    return False

def min_red_on_any_path(G, s, t, num_nodes):
    mincount = 0
    if G[s]["isRed"] == True:
        mincount =+ 1
    if G[t]["isRed"] == True:
        mincount =+ 1
    if t in G[s]: # s has a direct edge to t
        return mincount
    if not is_undirected(G) and not does_graph_contain_cycle(G):
        #Run dijksta to make sure a path exists
        #print("distance to t", dist[t])
        # print("Graph is DAG")
        global least_red_path
        least_red_path = sys.maxsize
        visited = deepcopy(G)
        paths = []
        for node in visited:
            visited[node] = False
        try:
            find_all_paths_dfs(G, s, t, visited, paths,mincount)
        except MinPathFound:
            return 0
        # print("all paths: ", all_paths)
        
        if least_red_path == sys.maxsize: # no path found
            return -1
        else:
            # instead of counting reds in each path now, we could not store the paths and just store the amount of reds 
            return least_red_path
    else: 
        # print("graph is not DAG")
        return -1 
    