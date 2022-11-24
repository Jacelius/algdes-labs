from NoneXD import shortest_path
from Some import path_exists_including_red
from Alternate import path_exists_alternating_red
from Few import min_red_on_any_path, min_red_on_any_path_dijkstra
from Many import max_red_on_any_path_brute, max_red_on_any_path
import time
import os
from utils import NegativeWeightCycleException

import sys
sys.setrecursionlimit(100000)

def remove_increase(files):
    for file in files:
        if "increase" in file:
            files.remove(file)
    return files

# parse graphs
def parse_graph(filename):
    with open("data/" + filename) as f:
        g = {} 
        lines = f.readlines()
        num_nodes, num_edges, num_red_nodes = lines[0].split()
        start_node, end_node = lines[1].split() # common: s, t == "start", "ender"
        for i in range(2, int(num_nodes)+2):
            line = lines[i].split()
            if ("*" in line): # red node found
                # add node to graph
                g[line[0]] = {}
                g[line[0]]["isRed"] = True
            else: 
                # add node to graph
                g[line[0]] = {}
                g[line[0]]["isRed"] = False
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
        return g, num_nodes, num_edges, start_node, end_node
       
#Create a list of all filesnames in data folder 
def get_files():
    files = []
    for file in os.listdir("data"):
        if file.endswith(".txt"):
            files.append(file)
    return files

files = get_files()
# files.remove("bht.txt")
# files = remove_increase(files)
# files = ["miniDAG.txt"]
# files = ["gnm-1000-2000-1.txt"]
files = ["G-ex.txt"]
# files = ["bht.txt"]
# files = ["rusty-1-17.txt"]
Few_results = []
NoneXD_results = []

should_write = input("Press 1 to write to file or enter to print to terminal: ")
if should_write != '1':
    print("Not writing to file")  
else:
    file_to_delete = open("results.txt",'w')
    file_to_delete.close()  

for file in files: # run None, Some, Many, Few & Alternate on the graph 
    G, num_nodes, num_edges, start_node, end_node = parse_graph(file)

    print('starting on ', file)

    start_time = time.time()

    #None:
    none = shortest_path(G, start_node, end_node, int(num_edges))
    none_res = f"None res for {file}: {none} in {time.time() - start_time} seconds"
    print(none_res)

    # #Alternate:
    alternates = path_exists_alternating_red(G, start_node, end_node)
    alternates_res = f"Alternate res for {file}: {alternates} in {time.time() - start_time} seconds"
    print(alternates_res)

    #Few:
    few = min_red_on_any_path_dijkstra(G, start_node, end_node)
    few_res = f"Few res for {file}: {few} in {time.time() - start_time} seconds"
    print(few_res)
    
    #Many:
    if int(num_nodes) < 14:
        many = max_red_on_any_path_brute(G, start_node, end_node)
        many_res = f"Many res for {file}: {many} in {time.time() - start_time} seconds"
        print(many_res)
    else:
        try:
            many = max_red_on_any_path(G, start_node, end_node)
            many_res = f"Many res for {file}: {many} in {time.time() - start_time} seconds"
            print(many_res)
        except NegativeWeightCycleException:
            many = "???"
            many_res = f"Many res for {file}: {many} in {time.time() - start_time} seconds"
            print(many_res)

    # #Some: true if many > 0)
    if many == "???" or many == 0:
        some = path_exists_including_red(G, start_node, end_node)
        some_res = f"Some res for {file}: {some} in {time.time() - start_time} seconds"
        print(some_res)
    else:
        some_res = f"Some res for {file}: True in {time.time() - start_time} seconds"
        print(some_res)
    
    if should_write == '1':
        with open("results.txt", "a") as f:
            f.write(none_res + "\n")
            f.write(some_res + "\n")
            f.write(alternates_res + "\n")
            f.write(few_res + "\n")
            f.write(many_res + "\n\n")
            
    print("\n")
    
    time.sleep(0.01)