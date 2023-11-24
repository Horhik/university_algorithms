# Dictionary based graph
def gen_graph(node_count, max_connections):
    graph = {}
    for i in range(node_count):
        graph[i] = set()
    for i in range(node_count):
        connections = randint(1, max_connections)
        #print("creating ", connections, " connections on ", i, " vertex")
        for k in range(connections):
            vertex = randint(0, node_count - 1)
            #print(vertex)
            graph[i].add(vertex)
            graph[vertex].add(i)
    return graph

# Class based graph

from random import  randint


import networkx as nx 
import matplotlib.pyplot as plt 

import queue

   
  
# Visualisation
class GraphVisualization: 
   
    def __init__(self): 
          
        # visual is a list which stores all  
        # the set of edges that constitutes a 
        # graph 
        self.visual = [] 
          
    # addEdge function inputs the vertices of an 
    # edge and appends it to the visual list 
    def addEdge(self, a, b): 
        temp = [a, b] 
        self.visual.append(temp) 
          
    # In visualize function G is an object of 
    # class Graph given by networkx G.add_edges_from(visual) 
    # creates a graph with a given list 
    # nx.draw_networkx(G) - plots the graph 
    # plt.show() - displays the graph 
    def visualize(self): 
        G = nx.Graph() 
        G.add_edges_from(self.visual) 
        nx.draw_networkx(G) 
        plt.show() 
  
    
class Vertex():
    def __init__(self, connections):
        self.connections = connections
        self.visited = False

    def visit(self):
        self.visited = True

            
class Graph():


    def __init__(self, node_count, max_connections=3):
        self.size = node_count
        self.nodes = {}
        self.G = GraphVisualization() 
        self.max_connections = max_connections

        for v in range(node_count):
            self.nodes[v] = Vertex(set())

            # making random number of connections for each vertex
            connections = randint(1, max_connections)
            for i in range(connections):
                vertex = randint(0, node_count - 1)
                if vertex != v:
                    self.nodes[v].connections.add(vertex)
                    self.G.addEdge(v, vertex) 
                    '''
        l = range(0, node_count-2, 2)
        r = range(1, node_count-2, 2)

        # make two connected graphs
        for i in l:
            self.nodes[i].connections.add(i+2)
            self.G.addEdge(i, i+2) 
        for i in r:
            self.nodes[i].connections.add(i+2)
            self.G.addEdge(i, i+2) 

        # connecting two random vertices of this graph
        bind = randint(0, node_count - 1)
        self.nodes[bind].connections.add(bind+1)
        self.G.addEdge(bind, bind+1) 
                    '''

    def copy(self):
        new_G = Graph(self.size, self.max_connections)
        for i in self.nodes:
            new_G.nodes[i] = self.nodes[i].connections.copy()
        new_G.G = self.G
        return new_G

    # Convert functions
    def gen_from_dict(self, dict):
        self.nodes = {}
        self.size = len(dict)
        self.G = GraphVisualization() 

        for v in dict:
            self.nodes[v] = Vertex(set(dict[v]))

            # Add edges to G for visualisation
            for el in dict[v]:
                self.G.addEdge(v, el)

    def make_dict(self):
        dict = {}
        for i in self.nodes:
            dict[i] = self.nodes[i].connections
        return dict


'''
# Test part

# Is class_graph stay the same
class_graph = Graph(20, max_connections=3)

class_graph_ = class_graph.copy()

dict_graph = class_graph.make_dict()

class_graph.gen_from_dict(dict_graph)
dict_graph_ = class_graph.make_dict()

print(dict_graph == dict_graph_)

# Is dict_graph stay the same
dict_graph = gen_graph(20, 3)

class_graph_ = Graph(20,3)
class_graph_.gen_from_dict(dict_graph)

dict_graph_ = class_graph_.make_dict()


print(dict_graph == dict_graph_)
'''
