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
        self.node_map_list = []
        for i in range(num_nodes):
            self.node_map_list.append({}) # create a dictionary {node: Edges[]} for each node

class FordFulkerson:
    def augment(self, graph, current, sink, flow, visited, threshold):
        if current == sink:
            print("augmenting flow by " + str(flow))
            return flow
        elif (current not in visited):
            visited.add(current)
            edges = graph.node_map_list[current].values()
            for edge in edges:
                if edge.c >= threshold:
                    residual = self.augment(graph, edge.v, sink, min(flow, edge.c), visited, threshold)
                    if residual > 0:
                        edge.c -= residual
                        graph.node_map_list[edge.v][edge.u].c += residual
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
                """                 if flow == 118:
                    print("118 now")
                    print("flow = " + str(flow))
                # print("flow = " + str(flow)) """
            threshold /= 2
        self.max_flow = flow

    def __init__(self, graph, source, sink):
        self.graph = graph
        self.max_flow(graph, source, sink)
        # self.min_cut = min_cut(graph, source, sink)
    

# parsing
with open('C:/Users/silas/git-projects/algdes-labs/flow/data/rail.txt') as f:
        lines = f.readlines()

num_nodes = int(lines[0]) # n
nodes = []
for i in range(1, num_nodes+1):
    node = lines[i].split()
    nodes.append(lines[i].strip()) # removes newlines
# print("nodes", nodes)
num_arcs = int(lines[num_nodes+1]) # m

g = Graph(num_arcs*2)

for i in range(num_nodes+2, num_nodes+2+num_arcs):
    u, v, c = lines[i].split() # [u, v, c]
    if c == "-1":
        c = float('inf')
        g.node_map_list[int(u)][int(v)] = Edge(int(u), int(v), c) # add edge to graph
        g.node_map_list[int(v)][int(u)] = Edge(int(u), int(v), c) # add reverse edge to graph
    else:
        g.node_map_list[int(u)][int(v)] = Edge(int(u), int(v), int(c)) # add edge to graph
        g.node_map_list[int(v)][int(u)] = Edge(int(u), int(v), int(c)) # add reverse edge to graph

# print(g.node_map_list)

print("Ford-Fulkerson running on graph with", num_nodes, "nodes and", num_arcs, "arcs")
FordFulkerson = FordFulkerson(g, 0, 54)
print("max flow: ", FordFulkerson.max_flow)

