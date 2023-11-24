from random import randint


array = []

def quicksort(array, pivot = lambda arr: arr[0]):
    if len(array) < 2:
        return array
    middle = pivot(array)
    left = list(filter(lambda x: x < middle, array))
    right = list(filter(lambda x: x > middle, array))
    return quicksort(left) + [middle] + quicksort(right)

array = [0,2,4,6,8,1,3,7,-2,-45,34,123,-64,-6]#gen_array(20, 50)

