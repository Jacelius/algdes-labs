from NoneXD import shortest_path
from Some import path_exists_including_red, path_exists_including_red_flow
from Alternate import path_exists_alternating_red
from Few import min_red_on_any_path, min_red_on_any_path_dijkstra
from Many import max_red_on_any_path_brute, max_red_on_any_path
import time
import os
from utils import NegativeWeightCycleException, does_graph_contain_cycle, is_undirected , is_DAG

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
# files = ["G-ex.txt"]
# files = ["bht.txt"]
# files = ["rusty-1-17.txt"]
# files = ["common-1-20.txt"]
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

    print('starting on ', file + '... isDAG = ' + str(is_DAG(G)))

    start_time = time.time()

    #None:
    none = shortest_path(G, start_node, end_node, int(num_edges))
    none_time = round(time.time() - start_time, 2)
    none_res = f"None res for {file}: {none} in {none_time} seconds"
    print(none_res)

    start_time = time.time()
    # #Alternate:
    alternates = path_exists_alternating_red(G, start_node, end_node)
    Alternate_time = round(time.time() - start_time, 2)
    alternates_res = f"Alternate res for {file}: {alternates} in {Alternate_time} seconds"
    print(alternates_res)

    start_time = time.time()
    #Few:
    few = min_red_on_any_path_dijkstra(G, start_node, end_node)
    few_time = round(time.time() - start_time, 2)
    few_res = f"Few res for {file}: {few} in {few_time} seconds"
    print(few_res)

    #Many:
    start_time = time.time()
    if int(num_nodes) < 14: # "brute force" many
        many = max_red_on_any_path_brute(G, start_node, end_node)
        many_time = round(time.time() - start_time, 2)
        many_res = f"Many res for {file}: {many} in {many_time} seconds"
        print(many_res)
    else:
        if (is_DAG(G)):
            try:
                many = max_red_on_any_path(G, start_node, end_node)
                many_time = round(time.time() - start_time, 2)
                many_res = f"Many res for {file}: {many} in {many_time} seconds"
                print(many_res) 
            except NegativeWeightCycleException: # should never happen, because we should only try on DAGs
                many_time = round(time.time() - start_time, 2)
                many_res = f"Many res for {file}: ??? in {many_time} seconds"
                print(many_res)
        else:
            many_time = round(time.time() - start_time, 2)
            many_res = f"Many res for {file}: ??? in {many_time} seconds"
            print(many_res)

    if is_undirected(G):
        some = path_exists_including_red_flow(G, start_node, end_node)
        some_time = round(time.time() - start_time, 2)
        some_res = f"Some res for {file}: {some} in {some_time} seconds"
        print(some_res)
    elif many > 0:
        some = path_exists_including_red_flow(G, start_node, end_node)
        some_time = round(time.time() - start_time, 2)
        some = f"Some res for {file}: True in {some_time} seconds"
        print(some)
    else:
        some_time = round(time.time() - start_time, 2)
        some = f"Some res for {file}: ??? in {some_time} seconds"   
        print(some)
    


    if should_write == '1':
        with open("results_format.txt", "a") as f:
            f.write(file + " " + str(none_time) + " " + str(Alternate_time) + " " + str(few_time) + " " + str(many_time) + " " 
            + str(some_time)+ "\n")
            #f.write(none_res + "\n")
            #f.write(some_res + "\n")
            #f.write(alternates_res + "\n")
            #f.write(few_res + "\n")
            #f.write(many_res + "\n\n")
            
    print("\n")
    
    time.sleep(0.01)