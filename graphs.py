import time

import sys
sys.setrecursionlimit(30_000)

from graph_types import Graph, gen_graph
from bfs import BFS
from dfs import dfsearch as dfs

import queue

# Testing BFS

start = time.time()
print("begin BFS search")

g = Graph(20_000)
g_ = g.copy()
q = queue.Queue()
q.put(0)
BFS(g, q, 433)
#g.G.visualize()



end = time.time()
print(" Time taken for BFS: ", end - start, "\n")


# TESTING DFS

start = time.time()
print("begin DFS search")

g = g.make_dict()



for el in g[0]:
    dfs(g, el, 433)

#g.G.visualize()


end = time.time()
print(" Time taken for DFS: ", end - start)


#g_.G.visualize()
