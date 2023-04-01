import random
import numpy as np

array = np.random.randint(0, 10, size=10)

def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            return False
    return True

def bogo_sort(array):
    attempts = 0
    while not is_sorted(array):
        random.shuffle(array)
        attempts += 1
        print(attempts)
    print("Sorted in {} attempts".format(attempts))
    return array

print (bogo_sort(array))