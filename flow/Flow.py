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
# print("num_arcs", num_arcs)
arcs = []
for i in range(num_nodes+2, num_nodes+2+num_arcs):
    arc = lines[i].split() # [u, v, c] 
    arcs.append(arc)
# print("arcs", arcs)