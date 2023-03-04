def binary_search(list, target):
    
    ''' Returns the position of the target value if found, else returns None'''

    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2  # // is the FLOOR division (example: 5//2) = 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            last = midpoint - 1
        elif list[midpoint] > target:
            first = midpoint + 1
    return None

def search_print_output(target_value, index):
    if index is not None:
        print("Target {} found at index: ".format(target_value), index)   
    else:
        print("Target {} not found in list".format(target_value))

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
search_print_output(12, result)

result = binary_search(numbers, 5)
search_print_output(5, result)