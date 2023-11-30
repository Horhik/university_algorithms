from graph_types import Graph
graph = {
    0: {1: 8, 6: 9},
    1: {3: 5},
    2: {1: -9},
    3: {4: -1, 2: 5},
    4: {2: 6, 5: 3},
    5: {3: 2, 6: 10, 0: -10},
    6: {4: -5, 1: -1}
}


g = Graph(7, max_connections=4)
g.gen_from_dict_with_distances(graph)

m = g.turn_into_matrix()
mm = m.copy()
n = len(m)


for i in m:
    print(i)

for k in range(n):
    for j in range(n):
        for i in range(n):
            if m[i][j] > m[i][k] + m[k][ j]:
                m[i][j] = m[i][k] + m[k][ j]

for i in m:
    print(i)
          

