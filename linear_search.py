def linear_search(list, target_value):
    ''' 
    Returns the position of the target value if found, else returns None
    '''

    for index in range(0,len(list)):
        if list[index] == target_value:
            return index
    return None

def search_print_output(target_value, index):
    if index is not None:
        print("Target {} found at index: ".format(target_value), index)   
    else:
        print("Target {} not found in list".format(target_value))

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
search_print_output(12, result)

result = linear_search(numbers, 5)
search_print_output(5, result)


