class Queue:
    
    
    def __init__(self):
        self.items = []

    def enqueue(self, element):
        self.items.append(element)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.items)
    

class Point:

    value = None
    visited : bool
    valid : bool
    parent = None

    def __init__(self, value):
        self.value = value
        self.visited = False
        self.valid = True

    def __str__(self):
        x,y = self.value
        return f"({x},{y})"
    

class Maze:
    rows : int
    columns : int
    points = []
    unavailable_points : list
    starting_point : Point
    goal : Point

    def __init__(self, rows, columns, starting_point, unavailable_points, goal):
        
        self.rows = rows
        self.columns = columns
        self.starting_point = starting_point
        self.unavailable_points = unavailable_points
        self.goal = goal

        for i in range(self.rows):
            for j in range(self.columns):
                point = Point((i,j))
                if point in self.unavailable_points:
                    point.valid = False
                self.points.append(point)

    def __str__(self):
        maze = ""
        for i in range(self.rows):
            for j in range(self.columns):
                if (i,j) == self.goal:
                    maze += "G"
                elif (i,j) == self.starting_point:
                    maze += "U"
                elif (i,j) in self.unavailable_points:
                    maze += "x"
                else:
                    maze += "o"
            maze += "\n"
        return maze

MAZE_ROWS = 5
MAZE_COLUMNS = 5
UNAVAILABLE_POINTS = [(1,1), (1,2), (1,3), (2,1), (2,3), (3,1)]

STARTING_POINT = Point((2,2))
GOAL = Point((0,0))


def BFS(maze : Maze, current_point : Point):
    q = Queue()
    q.enqueue(current_point)
    for point in maze.points:
        if point.value == current_point.value:
            current_point.visited= True

    while not q.isEmpty():
        current_point = q.dequeue()

        neighbors = []
        current_point_x, current_point_y = current_point.value
        if current_point_y + 1 < maze.rows and not (current_point_x, current_point_y + 1) in maze.unavailable_points:
            neighbors.append(Point((current_point_x, current_point_y + 1)))
        if current_point_y - 1 >= 0 and not (current_point_x, current_point_y - 1) in maze.unavailable_points:
            neighbors.append(Point((current_point_x, current_point_y - 1)))
        if current_point_x - 1 >= 0 and not (current_point_x-1, current_point_y) in maze.unavailable_points:
            neighbors.append(Point((current_point_x-1, current_point_y)))
        if current_point_x + 1 < maze.columns and not (current_point_x+1, current_point_y) in maze.unavailable_points:
            neighbors.append(Point((current_point_x+1, current_point_y)))

        for neighbor in neighbors:
            for point in maze.points:
                if point.value == neighbor.value:
                    if not point.visited:
                        point.parent = current_point
                        point.visited = True
                        q.enqueue(neighbor)
                        if neighbor.value == GOAL.value:
                            print(f"GOAL FIND {GOAL}")
                            #return neighbor #Return Path using neighbor
    return "NO path to goal"



if __name__ == "__main__":
    maze = Maze(MAZE_ROWS, MAZE_COLUMNS, STARTING_POINT, UNAVAILABLE_POINTS, GOAL)
    BFS(maze, STARTING_POINT)