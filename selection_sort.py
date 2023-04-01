import random
import numpy as np

array = list(np.random.randint(0, 100, size=10000))

def find_minimum(array):
    
    minimum = array[0]
    minimum_idx = 0

    for i in range(0, len(array)):
        if array[i] < minimum:
            minimum = array[i]
            minimum_idx = i
    return minimum_idx

def selection_sort(array):
    sorted_array = []
    #print("%-35s %-35s" % (array, sorted_array))
    for i in range(len(array)):
        minimum = find_minimum(array)
        sorted_array.append(array.pop(minimum))
        #print("%-35s %-35s" % (array, sorted_array))
    return sorted_array


print (selection_sort(array))