from graph_types import Graph
def get_distances_dict(graph):
    dict = {}
    nodes = graph.nodes
    for node in nodes:
        for vertex in nodes[node].distances:
            distance = nodes[node].distances[vertex]
            if distance in dict:
                to_add = (min(node, vertex), max(node,vertex))
                dict[distance].add(to_add)
                print(" TO ADD: ", to_add, " RESULTED: ", dict[distance])
            else:
                to_add = (min(node, vertex), max(node,vertex))
                dict[distance] = {(to_add)}
                #dict[distance].add(to_add)
                print(" TO ADD: ", to_add, " RESULTED: ", dict[distance])
    return (dict, sorted(dict.keys()))


            
def add_edge(edge, dist , tree):
    a,b, = edge

    if not a in tree:
        tree[a] = {b: dist}
    else:
        tree[a][b] = dist

    if not b in tree:
        tree[b] = {a: dist}
    else:
        tree[b][a] = dist
    

def they_are_in_different_sets(edge, graph, disjoineds):
    for st in disjoineds:
        if edge[0] in st and edge[1] in st:
            return False
    return True


def process_disjoineds(edge, visit_state, disjoineds):
    va, vb = visit_state
    a,b, = edge
    a_set = [a, b]
    b_set = [a, b] 
    for st in disjoineds:
        if a in st:
            a_set = st
            
        if b in st:
            b_set = st
    # if there's two disconnected trees, we're connecting them 
    if a_set != b_set and va and vb:
        disjoineds = [arr for arr in disjoineds if not (arr == a_set) and not (arr == b_set)]
        disjoineds.append(a_set+b_set)
    # if a, b is new edge disconnected from others
    elif not va and not vb:
        disjoineds.append([a,b])
    elif va and not vb:
        a_set.append(b)
    elif vb and not va:
        b_set.append(a)
    print('final set is: ', disjoineds)
    return disjoineds

  
        


def kurskall(graph):


    g = graph.nodes
    resulted_tree = {}
    disjoineds = []

    distances_dict, dist_sorted = get_distances_dict(graph)
    for dist in dist_sorted:
        for edge in distances_dict[dist]:
            A, B = edge[0], edge[1]
            a = g[A]
            b = g[B]
            # if at least one not visited
            if not (a.visited and b.visited) or (a.visited and b.visited and they_are_in_different_sets(edge, graph, disjoineds)):
                if (a.visited and b.visited and they_are_in_different_sets(edge, graph, disjoineds)):
                    print("Evaluated", edge, " is in different sets ", disjoineds  )


                disjoineds = process_disjoineds(edge, (a.visited, b.visited), disjoineds)
                graph.visit_node(A)
                graph.visit_node(B)

                add_edge(edge, dist, resulted_tree)
    return resulted_tree
                

#    while not graph.all_visited:
        
graph = {
    0: {3: 5, 1: 7},
    1: {0: 7, 3: 9, 4: 7, 2: 8},
    2: {1: 8, 4: 5},
    3: {0: 5, 1: 9, 4: 15, 5: 6 },
    4: {2: 5, 1: 7, 3: 15, 5: 8, 6: 9},
    5: {3: 6, 4: 8, 6: 11},
    6: {5: 11, 4: 9},
}

g = Graph(0, initial_dict=graph, dict_with_distances=True)
ng = Graph(0, initial_dict=kurskall(g), dict_with_distances=True)
g.G.visualize()
ng.G.visualize()
