class Edge:
    def __init__(self, u, v, c):
        self.u = u
        self.v = v
        self.c = c

    def __str__(self):
        return str(self.u) + " -> " + str(self.v) + " : " + str(self.c)

    def __repr__(self):
        return str(self)

class Graph:
    def __init__(self, num_nodes):
        self.node_map_list = []
        for i in range(num_nodes):
            self.node_map_list.append({}) # create a dictionary for each node

class FordFulkerson:
    def augment(self, graph, current, sink, flow, visited, threshold):
        if current == sink:
            return flow
        elif (current not in visited):
            visited.add(current)
            for next in graph.node_map_list[current]:
                if next.c >= threshold:
                    augmented_flow = self.augment(graph, next, sink, min(flow, next.c), visited, threshold)
                    if augmented_flow > 0:
                        next.c -= augmented_flow
                        next.u.c += augmented_flow
                        return augmented_flow
        return 0

    def max_flow(self, graph, source, sink):
        self.max_flow = 0
        threshold = 1
        flow = 0
        while threshold > 0:
            threshold /= 2
            while True:
                flow += self.augment(graph, source, sink, float('inf'), set(), threshold)
                if flow == 0:
                    break
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
    g.node_map_list[int(u)][int(v)] = Edge(u, v, c) # add edge to graph
    g.node_map_list[int(v)][int(u)] = Edge(u, v, c) # add reverse edge to graph

print(g.node_map_list)

FordFulkerson = FordFulkerson(g, 0, 54)
print("max flow: ", FordFulkerson.max_flow)

