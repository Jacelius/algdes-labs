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


def depth_first_search(G, s, t, visited, path,R):
    global all_paths
    # Find all possible paths from 's' to 't'.

    visited[s] = True
    path.append(s)

    if (s == t): # path found
        # print("path found: ", path)
        if does_path_contain_red(path, R):
            raise redPathFound("path found with red")
            
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
    global all_paths
    # if we find a path, that doesn't include a red node, try again with a different path 
    # geeks for geeks idea
    """
    1. The idea is to do Depth First Traversal of a given directed graph.
    2. Start the DFS traversal from the source.
    3. Keep storing the visited vertices in an array or HashMap say ‘path[]’.
    4. If the destination vertex is reached, print the contents of path[].
    5. The important thing is to mark current vertices in the path[] as visited also so that the traversal doesn’t go in a cycle.
    """
    visited = deepcopy(G)
    for node in visited:
        visited[node] = False
    path = []
    try:
        depth_first_search(G, s, t, visited, path, R)
        return False
    except redPathFound:
        return True