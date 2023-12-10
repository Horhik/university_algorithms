from random import randint
from graph_types import Graph

def find_closest(way, graph):
    closest = None
    dist = 100000000000
    parent = None
    for vertex in way:
        distances = graph.nodes[vertex].distances
        print(distances)
        for nextv in distances:
            print(" next is " , nextv, distances, " of vertex ", vertex)
            visited = graph.nodes[nextv].visited
            print(nextv, " " , visited, " is visited ")
            distance = distances[nextv]
            if not visited and distance < dist:
                closest = nextv
                dist = distances[nextv]
                parent = vertex
    return((parent, closest))


        

def prim(graph):
    current = randint(0, graph.size-1)
    graph.visit_node(current)
    way = [current]
    connections = []
    
    while not graph.all_visited:
        parent, closest = find_closest(way, graph)
        print("closest to ", current, " is ", closest)
        graph.visit_node(closest)
        way.append(closest)
        connections.append((parent, closest))
    return (way, connections)


g = {
    0: {1: 7, 2: 5},
    1: {0: 7, 4:8, 5:7, 2:9},
    2: {0: 5, 1: 9, 5:15, 3:6},
    3: {2: 6, 5: 8, 6: 11},
    4: {1:8, 5: 5},
    5: {4: 5, 1: 7, 2: 15, 3:8 , 6: 9},
    6: {5: 9, 3: 11},
    }
graph = Graph(0, initial_dict=g, dict_with_distances=True)
print(prim(graph))
