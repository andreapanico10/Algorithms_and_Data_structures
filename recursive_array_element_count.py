array = [2, 4, 6]

def array_element_count(array):

    if len(array) == 0:
        return 0
    if len(array) == 1:
        return 1
    
    return 1 + array_element_count(array[1:])

print(array_element_count(array))
     