from NoneXD import shortest_path

# parse graphs
def parse_word_graph():
    with open("data/wall-z-10000.txt") as f:
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
       
def parse_number_graph():
    with open ("data/grid-5-0.txt") as f:
        g = {}
        lines = f.readlines()
        num_nodes, num_edges, num_red_nodes = lines[0].split()
        start_node, end_node = lines[1].split()
    

g, num_nodes, num_edges, rednodes, start_node, end_node = parse_word_graph()

# print shortest path
sp = shortest_path(g, start_node, end_node, rednodes, int(num_edges))
print("sp return ", sp)
# print("length of shortest path with no red node ", sp)

# run None, Some, Many, Few & Alternate on the graph 
# it is allowed to run on some well defined class of graph only (e.g. all bipartite, acyclic, directed, or simply all graphs)

# repeat for all graph types


