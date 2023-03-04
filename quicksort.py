import random 

def quicksort(array):
    
    if len(array) < 2:
        return array
    else:
        #introducing randomization to obtain average case O(n log n)
        random_position = random.randint(0,len(array)-1)
        
        pivot = array[random_position]
        less = [i for i in array[:random_position] if i <= pivot] + [i for i in array[random_position+1:] if i <= pivot]
        greater = [i for i in array[:random_position] if i > pivot] + [i for i in array[random_position+1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

array = [2, 10, 5, 15, 1, 0, 12]
print(quicksort(array))