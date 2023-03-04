array = [2, 4, 6]

def array_sum(array):

    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    
    return array[0] + array_sum(array[1:])

print(array_sum(array))
     