def binary_search_recursive(list, target):
    ''' Returns only a boolean condition'''
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return binary_search_recursive(list[midpoint + 1:], target)
            if list[midpoint] >= target:
                return binary_search_recursive(list[:midpoint], target) 

def search_print_output(result):
    print("Target found: ", result)   


numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search_recursive(numbers, 12)
search_print_output(result)

result = binary_search_recursive(numbers, 5)
search_print_output(result)