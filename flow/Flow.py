class Edge:
    def __init__(self, u, v, c):
        self.u = u
        self.v = v
        self.c = c

    def __str__(self):
        return str(self.u) + "->" + str(self.v) + " c = " + str(self.c)

    def __repr__(self):
        return str(self)

class Graph:
    def __init__(self, num_nodes):
        self.node_to_edge_list_dict = {} # node index key -> list of edges
        for i in range(num_nodes):
            self.node_to_edge_list_dict[i] = {}

class FordFulkerson:
    def augment(self, graph, current, sink, flow, visited, threshold):
        if current == sink:
            return flow
        elif (current not in visited):
            visited.add(current)
            edges = graph.node_to_edge_list_dict[current].values()
            for edge in edges:
                if edge.c >= threshold:
                    residual = self.augment(graph, edge.v, sink, min(flow, edge.c), visited, threshold)
                    if residual > 0:
                        edge.c -= residual
                        graph.node_to_edge_list_dict[edge.v][edge.u].c += residual
                        return residual
        return 0

    def max_flow(self, graph, source, sink):
        self.max_flow = 0
        threshold = 1
        flow = 0
        inc = 0

        while threshold > 0:
            inc = -1
            while inc != 0:
                inc = self.augment(graph, source, sink, float('inf'), set(), threshold)
                flow += inc
            threshold /= 2
        self.max_flow = flow
        
    def min_cut(self, graph, source, sink):
        return 0

    def __init__(self, graph, source, sink):
        self.graph = graph
        self.max_flow(graph, source, sink)
        self.min_cut(graph, source, sink)
    

# parsing
with open('data/rail.txt') as f:
        lines = f.readlines()

num_nodes = int(lines[0]) # n
nodes = []
for i in range(1, num_nodes+1):
    nodes.append(lines[i].strip()) # removes newlines
# print("nodes", nodes)
num_arcs = int(lines[num_nodes+1]) # m

g = Graph(num_nodes)

for i in range(num_nodes+2, num_nodes+2+num_arcs):
    u, v, c = lines[i].split() # [u, v, c]
    if c == "-1":
        c = float('inf')
        g.node_to_edge_list_dict[int(u)][int(v)] = (Edge(int(u), int(v), c))
        g.node_to_edge_list_dict[int(v)][int(u)] = (Edge(int(v), int(u), c))
    else:
        g.node_to_edge_list_dict[int(u)][int(v)] = (Edge(int(u), int(v), int(c)))
        g.node_to_edge_list_dict[int(v)][int(u)] = (Edge(int(v), int(u), int(c)))


print("Ford-Fulkerson running on graph with", num_nodes, "nodes and", num_arcs, "arcs")
FordFulkerson = FordFulkerson(g, 0, 54)
print("max flow: ", FordFulkerson.max_flow)

