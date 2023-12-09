from graph_types import Graph
from tarjan import tarjan
from fleury import fleury

def gen_cycle_list(graph):
    g = Graph(0, initial_dict=graph)
    cycles = tarjan(g)
    graphs = []
    for cycle in cycles:
        new_graph = {}
        for node in cycle:
            new_graph[node] = [el for el in graph[node] if el in cycle]
        graphs.append(Graph(0, initial_dict=new_graph))
    return(graphs)

def get_euler_cycles(cycles):
    euler_cycles = []
    for cycle in cycles:
        res = fleury(cycle)
        if res and len(cycle.nodes)>2 and res != -1:
            euler_cycles.append(res)
    return euler_cycles

graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [0, 4],
    4: [8, 3],
    5: [7],
    6: [5],
    7: [6, 8],
    8: [9],
    9: [8, 10],
    10: [11, 12, 13],
    11: [],
    12: [],
    13: [14],
    14: [15],
    15: [16],
    16: [13]
}

g = Graph(0, initial_dict=graph)
#g.G.visualize()
cl = gen_cycle_list(graph)
print(list(map(lambda x: x.make_dict(), cl)))
cycles = get_euler_cycles(cl)
print(list(map(lambda x: x.nodes, cycles)))
