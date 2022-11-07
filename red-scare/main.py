from NoneXD import shortest_path

# parse graphs
def parse_word_graph():
    with open("red-scare/data/rusty-1-17.txt") as f:
        g = {} 
        if "-1-" in f.name:
            k = 1
        else:
            k = 2
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
            # build edges
            u, v = lines[i].split(" -- ")
            u = u.strip()
            v = v.strip()
            g[u][v] = 1
            g[v][u] = 1 # reverse edge
        return g, num_nodes, num_edges, rednodes, start_node, end_node
       

g, num_nodes, num_edges, rednodes, start_node, end_node = parse_word_graph()

# print shortest path
sp = shortest_path(g, start_node, end_node, rednodes, int(num_edges))
# print("length of shortest path with no red node ", sp)

# run None, Some, Many, Few & Alternate on the graph 
# it is allowed to run on some well defined class of graph only (e.g. all bipartite, acyclic, directed, or simply all graphs)

# repeat for all graph types


