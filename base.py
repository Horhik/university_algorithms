from random import randint 
import time

def gen_array(N, max_val):
    array = []
    for i in range(0, N):
        val = randint(-max_val, max_val)
        if not val in array:
            array.append(val)
    return array

def measure_time(func, args, function_name):
    start = time.time()
    print(f'begin {function_name} time_measuring....')

    func(args)

    end = time.time()
    print(f" Time taken for {function_name}: ", end - start, '\n')



        
    
def test_sorting(function, function_name):
    print("generating array")
    array = gen_array(200, 50)
    print(f'Testing {function_name}...')
    python_sort = sorted(array.copy())
    quick_sort = function(array.copy())
    #print(python_sort)
    #print(quick_sort)
    print("Match with python `sorted` function: ", python_sort == quick_sort)

    measure_time(function, array.copy(), function_name)



from merge_sort import merge_sort
import quick_sort
from heap_sort import heapsort

test_sorting(merge_sort, "Merge Sort")
test_sorting(quick_sort.quicksort, "Quick Sort")
test_sorting(heapsort, "Heap Sort")

import graphs
