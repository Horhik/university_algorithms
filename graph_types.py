inf = 5e+1000
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
        G = nx.DiGraph(directed=True)
        G.add_edges_from(self.visual) 
        nx.draw_networkx(G,arrows=True, with_labels=True) 
        plt.show() 
  
    
class Vertex():
    def __init__(self, connections, distances):
        self.connections = connections
        self.distances = distances
        self.visited = False
        self.parent = None

    def visit(self):
        self.visited = True


            
class Graph():


    def __init__(self, node_count, max_connections=3, max_distance=100):
        self.size = node_count
        self.nodes = {}
        self.G = GraphVisualization() 
        self.max_connections = max_connections
        self.all_visited = False
        self.visited = set()
        self.start_node = None
        

        for v in range(node_count):
            self.nodes[v] = Vertex(set(), {})
        for v in range(node_count):
            # making random number of connections for each vertex
            connections = randint(1, max_connections)
            for i in range(connections):
                vertex = randint(0, node_count - 1)
                if vertex != v:

                    dist = randint(1, max_distance)

                    self.nodes[v].distances[vertex] = dist
                    self.nodes[vertex].distances[v] = dist

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

    # method of visiting specific node and tracking if all nodes are visited 
    def set_parent(self, node, parent):
        print("set parent of ", node, ' to be ', parent)
        self.nodes[node].parent = parent

    def visit_node(self, node):
        vert = self.nodes[node]
        vert.visit()
        self.visited.add(node)
        self.all_visited = len(self.visited) == self.size

     # Convert functions
    def gen_from_dict_with_distances(self, dict):
        self.nodes = {}
        self.size = len(dict)
        self.G = GraphVisualization() 

        for v in dict:
            dists = dict[v]
            conns = [l for l in dists]

            self.nodes[v] = Vertex(set(conns), dists)

            # Add edges to G for visualisation
            for el in dict[v]:
                print('connecting ', el, ' with ', v)
                self.G.addEdge(v, el)

   

    # Convert functions
    def gen_from_dict(self, dict):
        self.nodes = {}
        self.size = len(dict)
        self.G = GraphVisualization() 

        for v in dict:
            self.nodes[v] = Vertex(set(dict[v]), {})

            # Add edges to G for visualisation
            for el in dict[v]:
                self.G.addEdge(v, el)
    def turn_into_matrix(self):
        n = self.size
        m = [[0 if i == j else inf for j in range(n)] for i in range(n)]
        for v in self.nodes:
            dists = self.nodes[v].distances
            for d in dists:
                m[v][d] = dists[d]

        return m
            

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
