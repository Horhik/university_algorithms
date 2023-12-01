from random import randint
from graph_types import Graph

stack = []
SCC_list = []
SCC = []
           
            
            


def dfs(graph, vertex):
    nodes = graph.nodes

    nodes[vertex].travel_time = graph.timer
    nodes[vertex].earliest_link = graph.timer
    nodes[vertex].visit()

    graph.timer +=1

    stack.append(vertex)
    graph.on_stack[vertex] = True

    for v in nodes[vertex].connections:
        print('  '*graph.timer + ' looking at ',  v)
        if graph.on_stack[v]:
            nodes[vertex].earliest_link = min(nodes[v].earliest_link, nodes[vertex].travel_time)

        elif nodes[v].travel_time == -1:
            # go deep into graph 
            dfs(graph, v)
            nodes[vertex].earliest_link = min(nodes[v].earliest_link, nodes[vertex].earliest_link)

    # if current vertex is start vertex
    # that means dfs came to the beginning again and there's a cycle
    print(" STACK IS ", stack)
    if nodes[vertex].earliest_link == nodes[vertex].travel_time:
        SCC = []
        popped = stack.pop()
        stack.append(popped)
        while popped != vertex:
            popped = stack.pop()
            SCC.append(popped)
            graph.on_stack[popped] = False
        if stack:
            stack.pop()
        if vertex not in SCC:
            SCC.append(vertex)
        SCC_list.append(SCC)
    return
 
def tarjan(graph):
    graph.timer = 0
    stack = []
    graph.on_stack = [False]*graph.size
    SCC_list = []

    for v in graph.nodes:
        if graph.nodes[v].travel_time == -1:
            SCC = []
            stack = []
            graph.timer = 0
            dfs(graph, v)
    return SCC_list
      

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
    13: []
}

g = Graph(8)
g.gen_from_dict(graph)
#g.G.visualize()
slist = tarjan(g)
