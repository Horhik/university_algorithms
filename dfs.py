from random import  randint

def gen_graph(node_count, max_connections):
    graph = {}
    for i in range(node_count):
        graph[i] = []
    for i in range(node_count):
        connections = randint(1, max_connections)
        #print("creating ", connections, " connections on ", i, " vertex")
        for k in range(connections):
            vertex = randint(0, node_count - 1)
            #print(vertex)
            graph[i].append(vertex)
        graph[i] = list(set(graph[i]))

    return graph

'''
def is_there_vertex_deeper(graph, el, marklist):

    for vertex in graph[el]:
        mark = vertex in marklist
        if not mark:
            return (True, vertex)
    return (False, el)

def dfs(graph, el):
    child_exsits = True
    stack = [el]
    marklist = []

    # извращение
    push = stack.append
    pop = stack.pop
    # конец извращений

    while len(stack) > 0:
        print("STACK IS: ", stack)
        (child_exsits, current_el) = is_there_vertex_deeper(graph, el, marklist)
        marklist.append(el)
        if child_exsits:
            push(el)
            el = current_el
        else:
            el = pop()
        #print("GRAPH IS: ", graph)
    
    return(graph)
'''

visited = []
def dfsearch(G, v, search_value):
    visited.append(v)
    for el in G[v]:
        #print(visited)
        #if el == search_value:
        #    print("Found")
        #    return
        if not el in visited:
            dfsearch(G, el, search_value)
        

#g = gen_graph(20, 4)
#print(g)
#for el in g[0]:
#    dfsearch(g, el)



    
    
