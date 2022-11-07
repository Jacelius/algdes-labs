# parse graphs
def parse_common_graph():
    with ("red-scare/data/common-1-3000.txt") as f:
        g = {} 
        print("f", f)
        lines = f.readlines()
        num_nodes, num_edges, idk = lines[0].split()
        start_node, end_node = lines[1].split() # "start", "ender"
        for i in range(2, num_nodes+2):
            node_id, node_type = lines[i].split()
            # add node to graph
            g[node_id] = node_type
        print("g", g)
        # what do the stars mean for the words?

parse_common_graph()

    
# run None, Some, Many, Few & Alternate on the graph 
# it is allowed to run on some well defined class of graph only (e.g. all bipartite, acyclic, directed, or simply all graphs)

# repeat for all graph types


