array = [2, 4, 6]

def array_maximum(array):

    if len(array) == 0:
        return None
    if len(array) == 1:
        return array[0]
    
    return max(array[0], array_maximum(array[1:]))

print(array_maximum(array))
     