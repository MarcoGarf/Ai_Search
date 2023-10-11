from collections import deque
import sys, heapq, time

class Node:
    def __init__(self, x, y, parent, cost):
        self.x = x
        self.y = y
        self.parent = parent
        self.cost = cost
    
    def getPos(self):
        return (self.x, self.y)

def read_map(file_name):
    with open(file_name, 'r') as file:
        # Read the first three lines for size, start, and goal information
        size_line = file.readline().strip().split()
        start_line = file.readline().strip().split()
        goal_line = file.readline().strip().split()

        # Extract the size, start, and goal values
        size = (int(size_line[0]), int(size_line[1]))
        start = (int(start_line[0]), int(start_line[1]))
        goal = (int(goal_line[0]), int(goal_line[1]))

        # Read the rest of the lines to build the grid
        lines = file.readlines()
        grid = []
        for line in lines:
            row = [int(cell) for cell in line.strip().split()]
            grid.append(row)

        return size, start, goal, grid

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python Breath_First_Search.py <map_file> <algorithm>")
    sys.exit(1)

# Get the map file name and algorithm from command-line arguments
map_file = sys.argv[1]
algorithm = sys.argv[2]

# Read the map and extract size, start, goal, and grid
size, start, goal, grid = read_map(map_file)
# Print the extracted information
print("Size:", size)
print("Start:", start)
print("Goal:", goal)
print("Grid:", grid)
# Define possible moves (up, down, left, right)
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Function to check if a coordinate (x, y) is valid and not a barrier
def is_valid(x, y):
    # Check if the coordinates (x, y) are within the grid's bounds
    is_inside_grid = 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    if not is_inside_grid:
        return False  # Coordinates are outside the grid

    # Check if the cell at (x, y) is not equal to 0 (it's not a barrier)
    is_not_barrier = grid[x][y] != 0

    # Return True if both conditions are met, indicating it's a valid move
    return is_not_barrier

# Breadth-First Search (BFS) function
def bfs(start, goal):
    queue = deque([(start, [])])  # Initialize the queue with the start coordinate and path
    visited = set()               # Create a set to keep track of visited coordinates

    while queue:
        (x, y), path = queue.popleft() # Dequeue the first coordinate and its corresponding path
        

        if (x, y) == goal:
            return path + [(x, y)]  # Return the path to the goal

        for dx, dy in moves: # Iterate through the possible moves defined in the 'moves' list
            new_x, new_y = x + dx, y + dy # Calculate new coordinates by adding the move (dx, dy) to the current coordinates (x, y)

            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                 # Calculate the new coordinates based on the possible moves
                new_path = path + [(x, y)]  # Extend the path
                queue.append(((new_x, new_y), new_path))
                visited.add((new_x, new_y))  # Mark the state as visited

    return []  # If the goal cannot be reached, return an empty path

def calculateHeuristic(node, goal):
    return abs(node[0]-goal[0]) + abs(node[1]-goal[1])

def calculatePath(end_node):
    path = []
    current_node = end_node
    while current_node != None:
        path.append(current_node.getPos())
        current_node = current_node.parent
    path.reverse()
    return path

def calculateTotalCost(end_node):
    total_cost = 0
    current_node = end_node
    while current_node != None:
        total_cost += current_node.cost
        current_node = current_node.parent
    return total_cost

def astar(start, goal):
    start_time = time.time()
    queue = []
    start_node = Node(start[0], start[1], None, grid[start[0]][start[1]])
    heapq.heappush(queue, (start_node.cost, id(start_node), start_node))
    nodes_expanded = 0
    visited = set()
    end_time = 0
    max_nodes_held_in_memory = 0

    while queue:
        max_nodes_held_in_memory = max(max_nodes_held_in_memory, len(queue))
        nodes_expanded += 1
        current_node = heapq.heappop(queue)[2]
        
        visited.add(current_node.getPos())

        if current_node.getPos() == goal:
            end_time = time.time()
            runtime_ms = (end_time-start_time)*1000
            return calculatePath(current_node), calculateTotalCost(current_node), nodes_expanded, runtime_ms, max_nodes_held_in_memory
        
        for dx, dy in moves:
            new_x, new_y = current_node.x + dx, current_node.y + dy
            
            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                new_node = Node(new_x, new_y, current_node, 0)
                new_node.cost = grid[new_x][new_y] + calculateHeuristic(current_node.getPos(), (new_x, new_y))

                if (new_node.cost, (new_x, new_y)) not in queue:
                    heapq.heappush(queue, (new_node.cost, id(new_node), new_node))
    end_time = time.time()
    runtime_ms = (end_time-start_time)*1000
    return [], 0, nodes_expanded, runtime_ms, max_nodes_held_in_memory



# Call the BFS function and get the result
path, cost_of_path, nodes_expanded, runtime_ms, max_nodes_held_in_memory = astar(start, goal)

if path:
    print(f"The path from {start} to {goal} is:")
    for coordinate in path:
        print(coordinate)
    print(f"The total cost was: {cost_of_path}, the number of nodes expanded was: {nodes_expanded}, the max nodes held in memory was: {max_nodes_held_in_memory}, and the runtime was: {runtime_ms} milliseconds.")
else:
    print(f"There is no path from {start} to {goal}.")
