def look_right(parent):
    return(2*parent + 1)

def look_left(parent):
    return(2*parent + 2)

def heapify(tree, parent, N):
    l = 2*parent + 1
    r = 2*parent + 2
    largest = parent;
    if  l < N and tree[largest] < tree[l]:
        largest = l
    if  r < N and tree[largest] < tree[r]:
        largest = r
    if largest != parent:
        tree[largest], tree[parent] = tree[parent], tree[largest]

        heapify(tree, largest, N)
    return tree

def heapsort(array):
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, i, len(array))

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i)
    return(array)

    
