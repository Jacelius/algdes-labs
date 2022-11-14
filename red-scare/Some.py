from copy import deepcopy
import sys
sys.setrecursionlimit(10000)

class redPathFound(Exception):
    pass

def does_path_contain_red(path, R):
    for node in path:
        if node in R:
            return True
    return False

def does_vertex_have_red_neighbor(G, v, R):
    for neighbor in G[v]:
        if neighbor in R:
            return True, neighbor
    return False, None

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

def depth_first_search(G, s, t, visited, path, R):
    # Find all possible paths from 's' to 't'.

    visited[s] = True
    path.append(s)
    if (s == t): # path found
        # print("path found: ", path)
        if does_path_contain_red(path, R):
            raise redPathFound("path found with red")
            
    s_has_red_neighbor, neighbor = does_vertex_have_red_neighbor(G, s, R)
    if s_has_red_neighbor:
        if dfs(G, neighbor, t):
            raise redPathFound
        
    else: 
        for v in G[s]:
            if (visited[v] == False):
                depth_first_search(G, v, t, visited, path, R)

    path.pop()
    visited[s] = False
    #Rerun finding other paths

# return True if there is a path from s to t that includes at least one red node
# otherwise return False
def path_exists_including_red(G, s, t, R):
    # if we find a path, that doesn't include a red node, try again with a different path 
    visited = deepcopy(G)
    for node in visited:
        visited[node] = False
    path = []
    try:
        depth_first_search(G, s, t, visited, path, R)
        return False
    except redPathFound:
        return True