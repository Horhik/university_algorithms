def split(array):
    n = len(array)
    m = n//2
    return (array[:m], array[m:])

def sort(a,b):
    if a < b:
        return [a,b]
    else:
        return [b,a]

def merge_(left, right):
    res = []
    n = len(left)
    for i in range(n):
        (l,r) = sort(left[i], right[r])
        res += [l,r]
    return res


def merge(left, right):
    ll = len(left)
    lr = len(right)
    res = [None]*(ll+lr)
    current_left_index = 0
    current_right_index = 0
    for i in range(ll+lr):
        if (current_left_index < ll and current_right_index < lr):
            if(left[current_left_index] < right[current_right_index]):
                res[i] = left[current_left_index]
                current_left_index += 1
            else:
                res[i] = right[current_right_index]
                current_right_index += 1
        elif (current_left_index < ll):
            res[i] = left[current_left_index]
            current_left_index += 1
        else:

            res[i] = right[current_right_index]
            current_right_index += 1
    return res
        
def merge_sort(array):
    if len(array) < 2:
        return array

    (left,right) = split(array)
    return merge(merge_sort(left), merge_sort(right))

