from NoneXD import shortest_path
from Some import path_exists_including_red
import time

# parse graphs
def parse_graph(filename):
    with open("data/" + filename) as f:
        g = {} 
        lines = f.readlines()
        num_nodes, num_edges, num_red_nodes = lines[0].split()
        start_node, end_node = lines[1].split() # common: s, t == "start", "ender"
        rednodes = []
        for i in range(2, int(num_nodes)+2):
            line = lines[i].split()
            if ("*" in line): # red node found
                rednodes.append(line[0])
                # add node to graph
                g[line[0]] = {}
            else: 
                # add node to graph
                g[line[0]] = {}
        for i in range(int(num_nodes)+2, int(num_nodes)+2+int(num_edges)):
            if(' -- ' in lines[i]):
                # build edges
                u, v = lines[i].split(" -- ")
                u = u.strip()
                v = v.strip()
                g[u][v] = 1
                g[v][u] = 1 # reverse edge
            elif('->' in lines[i]):
                u, v = lines[i].split(" -> ")
                u = u.strip()
                v = v.strip()
                g[u][v] = 1 # no reverse edge
        return g, num_nodes, num_edges, rednodes, start_node, end_node
       
#Create a list of all filesnames in data folder 
def get_files():
    import os
    files = []
    for file in os.listdir("data"):
        if file.endswith(".txt"):
            files.append(file)
    return files

files = get_files()
for file in files:
    if(file != "bht.txt"):
        G, num_nodes, num_edges, rednodes, start_node, end_node = parse_graph(file)
        start_time = time.time()
        #print("Graph: ", G)
        # sp = shortest_path(g, start_node, end_node, rednodes, int(num_edges))
        # print(f"None res for {file}: {sp} in {time.time() - start_time}")
        some = path_exists_including_red(G, start_node, end_node, rednodes)
        print(f"Some res for {file}: {some} in {time.time() - start_time}")

# print shortest path

# run None, Some, Many, Few & Alternate on the graph 
# it is allowed to run on some well defined class of graph only (e.g. all bipartite, acyclic, directed, or simply all graphs)

# repeat for all graph types



