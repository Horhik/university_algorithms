from graph_types import Graph, gen_graph

inf = 5e+1000

# Finding an element of an avaliable elements of parent with minimum distance to it 
def find_a_good_child(childs, parent, graph ):
    child_goodness_measure = inf
    good_child = None
    goodness = graph.nodes[parent].distances

    for child in childs:
        print(goodness)
        if goodness[child] < child_goodness_measure:
            child_goodness_measure = goodness[child]
            good_child = child

    return good_child



# Search for next node and it's parents until find an unvisited node or returning an empty array
def search_for_next_node(vertex, graph):
    print("searching next for", vertex)
    if vertex == None:
        return None

    avaliable = []
    nodes = graph.nodes

    for v in nodes[vertex].connections:
        if not nodes[v].visited :
            print('unvisited nodes of' , vertex, ' is ', v)
            avaliable.append(v)

    if not avaliable:
        print("fail... searching in parents", vertex)
        print("parent of ", vertex, ' is ', nodes[vertex].parent)
        search_for_next_node(nodes[vertex].parent, graph)

    return find_a_good_child(avaliable, vertex, graph)
    
        
def dijkstra(graph, s):

    # Generating distances array
    D = [inf for i in range(0, graph.size)]
    D[s] = 0

    graph.start_node = s
    graph.visit_node(s)

    node = graph.nodes

    # Visit queue
    next_node = s

    # Filling up an array of distances with very big values
    while next_node != None:
        # Selecting a vertex to visit
        v = next_node 

        # Getting the distances of nodes connected to `v`
        dists = node[v].distances
        # Getting nodes connected to `v`
        conns = node[v].connections


        #check all new verticies and measure distances from current vertex to connected vertecies
        next_node_dist = inf
        for child in dists:

            d = dists[child] + D[v]
            # Modifying distances array if there's more short path from `s` to node `child`
            if d < D[child]:
                print(' distance to ', child, ' changing from ', D[child], ' to ', d)
                D[child] = d
                graph.set_parent(child, v)

        next_node = search_for_next_node(v, graph)
        if next_node != None:
            #graph.set_parent(next_node, v)
            graph.visit_node(v)

        
    return D

def print_way(graph, vertex):
    start = vertex
    parent = start
    way = []
    print(start, end = '')
    while graph.nodes[start].parent != None:
        parent = g.nodes[start].parent 
        print(  ' -> ', parent, end='')
        way.append(parent)
        start = parent
    print()
    return way

def print_distances(d):
    for i in (range(len(d))):
        print(' Shortest path to ', i, ' is ', d[i])
          


graph = {
    0: {6: 20, 4: 10, 1: 22, 2:4},
    1: {3: 1, 5: 5},
    2: {1: 3},
    3: {2: 3, 6: 2},
    4: {3: 4, 5: 6},
    5: {6: 11},
    6: {4: 1}
}


g = Graph(6)

g.gen_from_dict_with_distances(graph)

m = g.turn_into_matrix()
for i in m:
    print(i)
exit(0)
#g.G.visualize()
D = dijkstra(g, 0)
print_distances(D)

print("Ways is")
for i in graph:
    print_way(g, i)
