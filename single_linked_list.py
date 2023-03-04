class Node:
    ''' Object for storing a single node of a linked list
        Models 2 attributes - data and the link to the next node in the list
    '''
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" %self.data

class Linked_list:

    ''' 
    Singly linked list
    '''
    
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        '''
        Returns the number of nodes in the list
        Takes O(n) time
        '''
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node
        
        return count
    
    def add(self, data):
        ''' Insert operation (Add new node at the begin of the linked list) 
            Takes O(1) time
        '''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert(self, data, index):

        '''
        Insert a new Node containing data at index position
        Insertion takes O(1) time, but finding the node at the insertion point takes O(n) time 
        '''
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:

                current = node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node


    def remove(self, key):
 
        '''
        Removes Node containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes O(n) time
        '''       

        current = self.head
        previous : Node = None
        found = False

        while current and not found:

            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node

            elif current.data == key:
                found = True
                previous.next_node = current.next_node

            else:
                previous = current
                current = current.next_node
        
        return current

    def __repr__(self):

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        
        return '-> '.join(nodes)
    
    def search(self, key):
        
        '''
        Search for the first node that matches the key
        Returns the node or 'None' if not found
        '''
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        
        return None    
    
N1 = Node(10)
N2 = Node(20)

N1.next_node = N2
linked_list = Linked_list()
linked_list.head = N1
linked_list.add(1)
linked_list.insert(4, 1)
print(linked_list.size())
print(linked_list)
print(linked_list.search(10))