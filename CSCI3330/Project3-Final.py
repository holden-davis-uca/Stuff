# CSCI 3330 - CRN 22104 - Fall 2021 - Dr. Hu
# Holden Davis, Jordan Maxwell, Tyler Walters
# Project 3 - Graph Algorithms

import networkx as nx
import matplotlib.pyplot as plt

def maketask1graph():
    task1graph = nx.Graph()
       
    task1graphedges = [("a", "b"),
                       ("a", "f"),
                       ("a", "e"),
                        ("b", "f"),
                        ("b", "c"),
                        ("c", "d"),
                        ("c", "g"),
                        ("d", "g"),
                        ("g", "j"),
                        ("e", "f"),
                        ("e", "i"),
                        ("f", "i"),
                        ("i", "j"),
                        ("i", "m"),
                        ("m", "n"),
                        ("h", "k"),
                        ("k", "o"),
                        ("k", "l"),
                        ("l", "h"),
                        ("l", "p")]
    
    task1graph.add_edges_from(task1graphedges)
    
    return task1graph

def maketask2graph():
    task2graph = nx.DiGraph()
    
    task2graphedges = [(1,3),
                       (3,2),
                       (3,5),
                       (2,1),
                       (4,1),
                       (4,12),
                       (5,6),
                       (5,8),
                       (6,8),
                       (6,7),
                       (8,9),
                       (9,5),
                       (9,11),
                       (8,10),
                       (10,9),
                       (6,10),
                       (7,10),
                       (10,11),
                       (11,12)]
    
    task2graph.add_edges_from(task2graphedges)
    
    return task2graph
    
def maketask3graph():
    task3graph = nx.Graph()

    task3graph.add_edge("a", "b",weight=22)
    task3graph.add_edge("a","c",weight=9)
    task3graph.add_edge("a","d",weight=12)
    task3graph.add_edge("b","f",weight=36)
    task3graph.add_edge("c","b",weight=35)
    task3graph.add_edge("c","d",weight=4)
    task3graph.add_edge("c","e",weight=65)
    task3graph.add_edge("c","f",weight=42)
    task3graph.add_edge("d","e",weight=33)
    task3graph.add_edge("e","g",weight=23)
    task3graph.add_edge("e","f",weight=18)
    task3graph.add_edge("f","g",weight=39)
    task3graph.add_edge("b","h",weight=34)
    task3graph.add_edge("d","i",weight=30)
    task3graph.add_edge("h","i",weight=19)
    task3graph.add_edge("f","h",weight=24)
    task3graph.add_edge("g","i",weight=21)
    task3graph.add_edge("g","h",weight=25)
        
    return task3graph

def makeNegDijkGraph():
    task3graph = nx.Graph()

    task3graph.add_edge("a", "b",weight=22)
    task3graph.add_edge("a","c",weight=9)
    task3graph.add_edge("a","d",weight=12)
    task3graph.add_edge("b","f",weight=36)
    task3graph.add_edge("c","b",weight=35)
    task3graph.add_edge("c","d",weight=4)
    task3graph.add_edge("c","e",weight=65)
    task3graph.add_edge("c","f",weight=42)
    task3graph.add_edge("d","e",weight=33)
    task3graph.add_edge("e","g",weight=23)
    task3graph.add_edge("e","f",weight=18)
    task3graph.add_edge("f","g",weight=39)
    task3graph.add_edge("b","h",weight=34)
    task3graph.add_edge("d","i",weight=30)
    task3graph.add_edge("h","i",weight=19)
    task3graph.add_edge("f","h",weight=24)
    task3graph.add_edge("g","i",weight=21)
    task3graph.add_edge("g","h",weight=-25)
        
    return task3graph

def task1():
    plt.figure(0)
    task1file = open("task1.txt", 'w')
    task1graph = maketask1graph()
    task1file.write("\nTASK1GRAPH NODES:")
    for node in task1graph.nodes():
        task1file.write(str(node))
    task1file.write("\nTASK1GRAPH EDGES:")
    for edge in task1graph.edges():
        task1file.write(str(edge))
    nx.draw_networkx(task1graph)
    plt.savefig("task1graph.png")
    
    #a. Starting from any vertex, can DFS and BFS find all connected components of an undirected graph?
    #Yes
    task1file.write("\n\nTask 1, Part a.\n\n")
    #For each node in the graph, if a dfs search with said node as the source has the same result as a bfs search with said node as the source, the answer is yes.
    for node in task1graph.nodes:
        dfsresult = []
        bfsresult = []
        for i in nx.dfs_tree(task1graph, node):
            dfsresult.append(i)
        for i in nx.bfs_tree(task1graph, node):
            bfsresult.append(i)
        task1file.write("\nBeginning at node " + str(node) + ", are the resulting trees created by DFS and BFS the same? --> " + str(set(dfsresult) == set(bfsresult)))
    
    #b. Can both BFS and DFS determine if there is a path between two given nodes?
    #Yes
    task1file.write("\n\nTask 1, Part b.\n\n")
    #For each node in the graph, if a dfs search with said node as the source contains a node in the result, then such a path does exist. The same goes for bfs.
    for node in task1graph.nodes:
        for i in nx.dfs_tree(task1graph, node):
            if i != node:
                task1file.write("\nWith DFS, a path exists between the source node " + str(node) + " and the end node " + str(i))
        for i in nx.bfs_tree(task1graph, node):
            if i != node:
                task1file.write("\nWith BFS, a path exists between the source node " + str(node) + " and the end node " + str(i))
    
    #c. There is a path between two vertices A and B. If started from A, do DFS and BFS always find exactly the same path?
    #No
    task1file.write("\n\nTask 1, Part c.\n\n")
    #For some two nodes A and B in the graph, if the order of the contents between the tree of the dfs result differs from that of the bfs result, the found path is not the same
    for nodeA in task1graph.nodes:
        for nodeB in task1graph.nodes:
            if nodeA != nodeB:
                task1file.write("\nChecking path from " + str(nodeA) + " to " + str(nodeB))
                dfsresult = []
                bfsresult = []
                for i in nx.dfs_tree(task1graph, nodeA):
                    dfsresult.append(i)
                for i in nx.bfs_tree(task1graph, nodeA):
                    bfsresult.append(i)
                if nodeB in dfsresult and nodeB in bfsresult:
                    dfsendnodeindex = dfsresult.index(nodeB)
                    bfsendnodeindex = bfsresult.index(nodeB)
                    dfspath = dfsresult[:dfsendnodeindex]
                    bfspath = bfsresult[:bfsendnodeindex]
                    if dfspath == bfspath:
                        task1file.write("\nDFS and BFS paths are identical")
                    else: task1file.write("\nDFS and BFS paths are different")
                else: task1file.write("\nNo path exists between " + str(nodeA) + " and " + str(i))
                
    print("Completed task 1 - check task1.txt for computational results and task1.png for the graph!")
    task1file.close()

def task2():
    plt.figure(1)
    task2file = open("task2.txt", 'w')
    task2graph = maketask2graph()
    task2file.write("\nTASK2GRAPH NODES:")
    for node in task2graph.nodes():
        task2file.write(str(node))
    task2file.write("\nTASK2GRAPH EDGES:")
    for edge in task2graph.edges():
        task2file.write(str(edge))
    nx.draw_networkx(task2graph)
    plt.savefig("task2graph.png")
    
    #a. Use an application to find the strongly connected components of the digraph
    task2file.write("\n\nTask 2, Part a.\n")
    scc = nx.strongly_connected_components(task2graph)
    
    for s in scc:
        task2file.write("\nStrongly Connected Components: ")
        task2file.write(", ".join(str(e) for e in s))
    task2file.write("\n")
    
    #b. Draw the digraph as a ‘meta graph’ of its strongly connected components in your project report
    task2file.write("\n\nTask 2, Part b.\n\n")
    task2file.write("For this task, we hand-drew a diagraph of the strongly connected components.")
    task2file.write("\nIn order to run the hand-drawn graph through an alogorithm that linearizes it, we will use the following letters to denote strongly connected components.")
    task2file.write("\n\n1, 2, 3 ---------------> A")
    task2file.write("\n4 ---------------------> B")
    task2file.write("\n5, 6, 7, 8, 9, 10 -----> C")
    task2file.write("\n11 --------------------> D")
    task2file.write("\n12 --------------------> E")

    plt.figure(3)
    task2diagraph = nx.DiGraph()
    task2diagraph_edges = [("B", "A"),
                           ("B", "E"),
                           ("D", "E"),
                           ("C", "D")]
    task2diagraph.add_edges_from(task2diagraph_edges)
    nx.draw_networkx(task2diagraph)
    plt.savefig("task2diagraph.png")

    #c. Represent the ‘meta graph’ as a DAG and linearize it in its topological order
    # chapter 3 sample code scc code!!!
    task2file.write("\n\n\nTask 2, Part c.\n\n")
    topological = nx.all_topological_sorts(task2diagraph)
    topological_list = list(topological)
    task2file.write("Different Topological Order Combinations of the Strongly Connected Components: ")
    for l in topological_list:
        task2file.write("\nCombo: ")
        for n in l:
            task2file.write(n + " ")

    print("Completed task 2 - check task2.txt for computational results and task2.png for the graph!")
    task2file.close()
    
def task3():
    plt.figure(2)
    task3file = open("task3.txt", 'w')
    task3graph = maketask3graph()
    task3file.write("\nTASK3GRAPH NODES:")
    for node in task3graph.nodes():
        task3file.write(str(node))
    task3file.write("\nTASK3GRAPH EDGES:")
    for edge in task3graph.edges():
        task3file.write(str(edge))
    pos = nx.spring_layout(task3graph)
    nx.draw_networkx(task3graph, pos)
    nx.draw_networkx_edge_labels(task3graph, pos, edge_labels=nx.get_edge_attributes(task3graph, 'weight'))
    plt.savefig("task3graph.png")
    
    #a. Write an application that applies Dijkstra’s algorithm to produce the shortest path tree for a weighted graph with a given starting node. Test and verify your program with the given graph starting with node A
    task3file.write("\n\nTask 3, Part a.\n\n")
    
    #Finds the shortest path using Dijkstra's algorithm
    dijkPath = nx.single_source_dijkstra_path(task3graph, 'a')
    task3file.write(str(dijkPath))
    #print(dijkPath)

    #b. Write a program that produces a minimum spanning tree for a connected weighted graph. Test your program with the given graph above
    task3file.write("\n\nTask 3, Part b.\n\n")

    #Finds the minimum spanning tree
    mstTree = nx.minimum_spanning_tree(task3graph)

    #Finds the edges of the minimum spanning tree 
    mstPath = nx.minimum_spanning_edges(task3graph, algorithm="kruskal", data=False)
    edgelist = list(mstPath)

    #print(edgelist)
    task3file.write(str(edgelist))
    plt.figure(4)
    nx.draw_networkx(mstTree)
    plt.savefig("task3_mst.png")

    #c. Are a shortest path tree and a minimum spanning tree usually the same?
    task3file.write("\n\nTask 3, Part c.\n\n")

    #Finds shortest path from 'i', the central node of the minimum spanning tree,
    #To each of the other nodes in the weighted graph
    shortPath = nx.shortest_path(task3graph, source='i')
    task3file.write(str(shortPath))
    #print(shortPath)

    #d. If the graph has an edge with a negative weight, can you apply Dijkstra’s algorithm to find a shortest path tree?
    task3file.write("\n\nTask 3, Part d.\n\n")
    
    #This is Dijkstra's algorithm but uses a negative value in the weighted graph
    #To illustrate that the algorithm will not operate properly with a negative weighted value

    #negDijkGraph = makeNegDijkGraph()
    #negDijkPath = nx.single_source_dijkstra_path(negDijkGraph, 'a')
    #task3file.write(str(negDijkPath))
    #print(negDijkPath)
    
    print("Completed task 3 - check task3.txt for computational results and task3.png for the graph!")
    task3file.close()
    

print("\n\n!<---STARTING--->!\n\n")

task1()
task2()
task3()

print("\n\n!<---STOPPING--->!\n\n")

