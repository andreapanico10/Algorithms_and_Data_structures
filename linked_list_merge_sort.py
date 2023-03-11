from single_linked_list import Linked_list

linked_list = Linked_list()
linked_list.add(1)
print(linked_list)

def merge_sort(linked_list):
    '''
    Sort a linked list in ascending order
    - Recursively divide the linked list into sublists containing a dingle node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list
    Runs in O(kn log n)
    
    '''
#Takes overall O(n log n ) time
    if linked_list.size() == 1:
        return linked_list
    
    elif linked_list is None:
        return linked_list
    
    left_half, right_half = split_linked_list(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split_linked_list(linked_list):
    '''
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    
    Takes O(k logn) time 

    '''

    if linked_list == None or linked_list.head == None:

        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid - 1)
        left_half = linked_list
        right_half = Linked_list()

        #Hook the mid_node.next_node(and its consequents) to the right half
        right_half.head = mid_node.next_node
        #Break the connection for the left half
        mid_node.next_node = None



def merge(left, right):

    '''
    Merges 2 linked lists sorting by data in nodes
    Returns a new, merged list

    '''

    # Create a new linked list that contains nodes from merging
    # left and right

    merged = Linked_list()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of linked list
    current = merged.head

    # Obtain head nodes for the left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either
    while left_head or right_head:

        # if the head node of left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Set the stopping condition for the while loop
            right_head = right_head.next_node
        # if the head node of right is None, we're pass the tail
        # add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node

        else:
            # Not a neither tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to left node

            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # if data on left is greater than right, set current to right node
            else: 
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node
        
        # Move current to next_node
        current = current.next_node

        # Discard fake head and set first merged node as head
        head = merged.head.next_node
        merged.head = head

        return merged    

def recursive_verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and recursive_verify_sorted(list[1:])


linked_list = Linked_list()
linked_list.add(10)
linked_list.add(2)
linked_list.add(43)
linked_list.add(15)
linked_list.add(210)

print(linked_list)
sorted_linked_list = merge_sort(linked_list)
print(sorted_linked_list)

#print(recursive_verify_sorted(array))