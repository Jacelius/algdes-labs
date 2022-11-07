# parse graphs
def parse_word_graph():
    with open("data/common-1-3000.txt") as f:
        g = {} 
        print("f", f.name)
        if "-1-" in f.name:
            k = 1
        else:
            k = 2
        print("k", k)
        
        lines = f.readlines()
        num_nodes, num_edges, num_red_nodes = lines[0].split()
        start_node, end_node = lines[1].split() # common s, t: "start", "ender"
        for i in range(2, int(num_nodes)+2):
            line = lines[i].split()
            if (len(line) == 2): # red node found
                # add node to graph
                g[line[0]] = {}
                pass
        # print("g", g)
        # for each node, build edge to all nodes that are k-anagrams 
       

parse_word_graph()

def is_k_anagram(word1, word2, k): #Maybe fucky woky at some point because of sets idk tho lets hope not
    if (len(set(word1) ^ set(word2)) <= k):
        return True 
    else:
        return False

print("k anagram test: ", is_k_anagram("runty", "enter", 1))

# run None, Some, Many, Few & Alternate on the graph 
# it is allowed to run on some well defined class of graph only (e.g. all bipartite, acyclic, directed, or simply all graphs)

# repeat for all graph types


