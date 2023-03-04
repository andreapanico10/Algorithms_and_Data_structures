def merge_sort(list):
    '''
    Sort a list in ascending order
    Returns a new sorted list

    Divide: find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in the previous step

    Takes overall O(n log n ) time
    '''

    if len(list) <= 1:
        return list
    
    left_half, right_half = split_list(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge_lists(left, right)

def split_list(list):
    '''
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes O(log n) time
    '''

    mid = len(list) // 2 
    left = list[:mid] # slicing is slow, better with index
    right = list[mid:]

    return left, right


def merge_lists(left, right):

    '''
    Merges 2 lists sorting them in the process
    Returns a new merged list

    Takes overall O(n) runtime
    '''

    united_list = []
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            united_list.append(left[l])
            l += 1
        else:
            united_list.append(right[r])
            r += 1
    
    while l < len(left):
        united_list.append(left[l])
        l += 1 

    while r < len(right):
        united_list.append(right[r])
        r += 1 

    return united_list

def recursive_verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and recursive_verify_sorted(list[1:])


array = [10,6,43,2,3,1,5435,32,4]
array = merge_sort(array)
print(array)
print(recursive_verify_sorted(array))