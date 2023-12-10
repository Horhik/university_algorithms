from graph_types import Graph

def fleury(graph):

    odd_degree_count = 0
    start_vertex = list(graph.nodes.keys())[0]

    # Count vertices with odd degree
    for node in graph.nodes:
        if len(graph.nodes[node].connections) % 2 != 0:
            odd_degree_count += 1
            start_vertex = node

    if odd_degree_count > 2:
        print("More than 2 odd vertices, no euler path!")
        return -1 

    if odd_degree_count == 2:
        start_vertex = [node for node in graph.nodes if len(graph.nodes[node].connections) % 2 != 0][0]

    eulerian_path = []
    current_vertex = start_vertex

    while graph.nodes[current_vertex].connections:
        # removing next_vertex from list of connections of current_vertex and saving it
        next_vertex = graph.nodes[current_vertex].pop()
        # removing connection of next_vertex to current_vertex from next_vertex
        graph.nodes[next_vertex].remove(current_vertex)
        # appending connection to euler path
        eulerian_path.append((current_vertex, next_vertex))
        # starting from next vertex
        current_vertex = next_vertex

    return eulerian_path

eulerian_path_graph = {
    1: [2, 3, 4, 5],
    2: [1, 3, 4, 6],
    3: [1, 2, 4, 6],
    4: [1, 2, 3, 5],
    5: [1, 4, 6, 7],
    6: [2, 3, 5, 7],
    7: [5, 6]
}

graph = Graph(7)
graph.gen_from_dict(eulerian_path_graph)
print(fleury(graph))
#graph.G.visualize()


