def find_minimum(array):
    
    minimum = array[0]
    minimum_idx = 0

    for i in range(0, len(array)):
        if array[i] < minimum:
            minimum = array[i]
            minimum_idx = i
    return minimum_idx

def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        minimum = find_minimum(array)
        new_array.append(array.pop(minimum))
    return new_array
