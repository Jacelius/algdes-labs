from copy import deepcopy

class redPathFound(Exception):
    pass

def does_path_contain_red(G, path):
    for node in path:
        if G[node]["isRed"]:
            return True
    return False

def does_vertex_have_red_neighbor(G, v):
    for neighbor in G[v]:
        if neighbor != "isRed":
            if G[neighbor]["isRed"]:
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
                if neighbor != "isRed": # ignore isRed
                    stack.append(neighbor)
    return False

def depth_first_search_check_red(G, s, t, visited, path):
    # Find all possible paths from 's' to 't'.

    visited[s] = True
    path.append(s)
    if (s == t): # path found
        # print("path found: ", path)
        if does_path_contain_red(G, path):
            raise redPathFound("path found with red")
            
    s_has_red_neighbor, neighbor = does_vertex_have_red_neighbor(G, s)
    if s_has_red_neighbor:
        if dfs(G, neighbor, t):
            raise redPathFound
        
    else: 
        for v in G[s]:
            if v != "isRed": # ignore isRed
                if (visited[v] == False):
                    depth_first_search_check_red(G, v, t, visited, path)

    path.pop()
    visited[s] = False
    #Rerun finding other paths

# return True if there is a path from s to t that includes at least one red node
# otherwise return False
def path_exists_including_red(G, s, t):
    # if we find a path, that doesn't include a red node, try again with a different path 
    visited = deepcopy(G)
    for node in visited:
        visited[node] = False
    path = []
    try:
        depth_first_search_check_red(G, s, t, visited, path)
        return False
    except redPathFound:
        return True

def path_exists_including_red_flow(G, s, t):
    red_nodes = []
    for node in G:
        if G[node]["isRed"]:
            red_nodes.append(node)
    
    for red_node in red_nodes:
        # construct flow graph where red_node is the source and s & t are sinks
        # if max_flow = 2, then there is a path from red_node to s and t
        # -> so there is a path from s to t that includes red_node
        pass
    pass

