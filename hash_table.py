from collections import deque

# HASH TABLE #
# Implementation from Grokking Algorithm 

# Graph is a dictionary
graph = {}
graph["you"] = ["bob", "claire", "alice"] 
graph["bob"] = ["anuj", "peggy"] 
graph["alice"] = ["peggy"] 
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def breadth_first_search(name):      
    # queue
    search_queue = deque()
    search_queue += graph["you"]
    #to check the duplicates
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person +  " is a mango seller!")
            return True 
        else:
            print(person +  " NOT")
            search_queue += graph[person]
            searched.append(person)

def person_is_seller(name):
    return name[-1] == "m"

breadth_first_search("you")