from copy import deepcopy
import sys

class MinPathFound(Exception):
    pass
sys.setrecursionlimit(10000)
# Return the minimum number of red vertices on any path from s to t
def dfs(G, s, t): # Depth first search that returns true if a path exists from s to t
    visited = set()
    stack = [s]
    while stack:
        node = stack.pop()
        if node == t:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in G[node]:
                stack.append(neighbor)
    return False

global all_paths
all_paths = []

def find_all_paths_dfs(G, s, t, visited, path, R):
    global all_paths
    visited[s]= True
    path.append(s)

    # If current vertex is same as destination, then print
    # current path[]
    if s == t:
        if count_reds_in_path(path,R) == 0:
            raise MinPathFound("We found a 0 path")
        all_paths.append(deepcopy(path))
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for v in G[s]:
            if visited[v]== False:
                find_all_paths_dfs(G, v, t, visited, path, R)
                    
    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[s]= False

def count_reds_in_path(path, R):
    count = 0
    for node in path:
        if node in R:
            count += 1
    return count

def is_undirected(G):
    for node in G:
        for neighbor in G[node]:
            if node not in G[neighbor]:
                return False
            return True

def isCyclicUtil(G, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
 
        for neighbour in G[v]: 
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

def min_red_on_any_path(G, s, t, num_nodes, R):
    if not is_undirected(G) and not does_graph_contain_cycle(G):
        # print("Graph is DAG")
        global all_paths
        visited = deepcopy(G)
        paths = []
        for node in visited:
            visited[node] = False
        try:
            find_all_paths_dfs(G, s, t, visited, paths, R)
        except MinPathFound:
            return 0
        # print("all paths: ", all_paths)
        
        if all_paths == []:
            return -1
        else:
            min_reds = sys.maxsize
            for path in all_paths:
                # Return the minimum number of red vertices on any path from s to t
                reds = count_reds_in_path(path, R)
                if reds == 0: # won't get any better than this
                    return reds
                elif reds < min_reds:
                    min_reds = reds
            return min_reds
    else: 
        # print("graph is not DAG")
        return -1 
    