import queue
from graph_types import Graph

def BFS(G, queue, search_value):
    while not queue.empty():
        e = queue.get()
        #if e == search_value:
        #    print("FOUND")
        #   return
        #print("checking: ", e)
        v = G.nodes[e]
        v.visit()
        for el in v.connections:
           #print(list(queue))
            if not G.nodes[el].visited:
                queue.put(el)


