# graph is the hash table for the graph

graph = {}

# start -> 6 -> A 
#       -> 2 -> B  

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# costs is the hash table for the costs

infinity = float("inf")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# parents is the hash table for the parents

parents = {} 
parents["a"] = "start" 
parents["b"] = "start" 
parents["fin"] = None

# keep track of processed:
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def print_solution(graph, parents):
    start = "start"
    finish = "fin"
    node = finish
    
    solution_route = []
    solution_cost = 0

    solution_route.append(node)

    while node is not start:
        solution_route.append(parents[node])
        solution_cost += graph[parents[node]][node]

        node = parents[node]

    print("Shortest Path: ", end= "")
    print( *reversed(solution_route), sep=' -> ')
    print("Total cost: {}".format(solution_cost))

    

#       Dijkstra's Algorithm
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#          PSEUDO - CODE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# while we have node to process:
#   1 - Grab the node that is closest to the start
#   2 - Update costs for its neighbors
#   3 - If any of the neighbors' costs were updated, update the parents too
#   4 - Mark this node processed

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def dijkstra_algorithm(graph, costs, parents):
    # 1 - Grab the node that is closest to the start
    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for neighbor in neighbors.keys():
            new_cost = cost + neighbors[neighbor]
            if costs[neighbor] > new_cost:
                # 2 - Update costs for its neighbors
                costs[neighbor] = new_cost
                # 3 - If any of the neighbors' costs were updated, update the parents too
                parents[neighbor] = node
        # 4 - Mark this node processed
        processed.append(node)
        # 1 - Grab the node that is closest to the start
        node = find_lowest_cost_node(costs)

    print_solution(graph, parents)

dijkstra_algorithm(graph, costs, parents)
