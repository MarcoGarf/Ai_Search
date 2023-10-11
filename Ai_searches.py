import time
from collections import deque
import sys
import heapq

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
algorithm = sys.argv[2].lower()

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
    start_time = time.time()  # Record the start time
    queue = deque([(start, [])])  # Initialize the queue with the start coordinate and path
    visited = set()               # Create a set to keep track of visited coordinates
    nodes_expanded = 0            # Initialize the number of nodes expanded
    max_nodes_held_in_memory = 0  # Initialize the maximum number of nodes held in memory

    while queue:
        # Update the maximum number of nodes held in memory
        max_nodes_held_in_memory = max(max_nodes_held_in_memory, len(queue))

        (x, y), path = queue.popleft()  # Dequeue the first coordinate and its corresponding path
        nodes_expanded += 1

        if (x, y) == goal:
            end_time = time.time()  # Record the end time
            runtime_ms = (end_time - start_time) * 1000  # Calculate runtime in milliseconds
            return path + [(x, y)], nodes_expanded, max_nodes_held_in_memory, runtime_ms  # Return the path, nodes expanded, max nodes held, and runtime

        for dx, dy in moves:  # Iterate through the possible moves defined in the 'moves' list
            new_x, new_y = x + dx, y + dy  # Calculate new coordinates by adding the move (dx, dy) to the current coordinates (x, y)

            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                # Calculate the new coordinates based on the possible moves
                new_path = path + [(x, y)]  # Extend the path
                queue.append(((new_x, new_y), new_path))
                visited.add((new_x, new_y))  # Mark the state as visited

    return [], nodes_expanded, max_nodes_held_in_memory, None  # If the goal cannot be reached, return appropriate values

# Perform BFS search



def iddfs(start, goal):
    depth_limit = 0
    
    while True:
        result = dls(start, goal, depth_limit)
        if result is not None:
            return result  # Goal found
        depth_limit += 1  # Increase depth limit if goal not found at current depth

def dls(node, goal, depth_limit):
    start_time = time.time()
    stack = [(node, [])]
    nodes_expanded = 0
    max_nodes_held_in_memory = 0
    
    while stack:

        max_nodes_held_in_memory = max(max_nodes_held_in_memory, len(stack))

        (x, y), path = stack.pop()  # Pop the last coordinate and its corresponding path
        nodes_expanded += 1

        if (x, y) == goal:
            end_time = time.time()
            runtime_ms = (end_time - start_time) * 1000
            return path + [(x, y)], nodes_expanded, max_nodes_held_in_memory, runtime_ms  # Return the path to the goal

        if len(path) < depth_limit:
            for dx, dy in moves:
                new_x, new_y = x + dx, y + dy  # Calculate new coordinates by adding the move (dx, dy) to the current coordinates (x, y)

                if is_valid(new_x, new_y):
                    # Calculate the new coordinates based on the possible moves
                    new_path = path + [(x, y)]  # Extend the path
                    stack.append(((new_x, new_y), new_path))

    return [], nodes_expanded, max_nodes_held_in_memory, None  # Goal not found at this depth

# Node class for storing parent, cost, and coordinates
class Node:
    def __init__(self, x, y, parent, cost):
        self.x = x
        self.y = y
        self.parent = parent
        self.cost = cost
    
    def getPos(self):
        return (self.x, self.y)
    
# Calculate Heuristic for A* Search
def calculateHeuristic(node, goal):
    return abs(node[0]-goal[0]) + abs(node[1]-goal[1])

# Calculate path from last Node found
def calculatePath(end_node):
    path = []
    current_node = end_node
    while current_node != None:
        path.append(current_node.getPos())
        current_node = current_node.parent
    path.reverse()
    return path

# Calculate cost of path from last Node found
def calculateTotalCost(end_node):
    total_cost = 0
    current_node = end_node
    while current_node != None:
        total_cost += current_node.cost
        current_node = current_node.parent
    return total_cost

# A* Search Function
def astar(start, goal):
    start_time = time.time()
    queue = []
    start_node = Node(start[0], start[1], None, grid[start[0]][start[1]]) # Create start node from start coordinates
    heapq.heappush(queue, (start_node.cost, id(start_node), start_node)) # Push start node into priority queue with its cost
    nodes_expanded = 0
    visited = set() # Set of visited coordinates to avoid visiting again
    end_time = 0
    max_nodes_held_in_memory = 0

    while queue:
        max_nodes_held_in_memory = max(max_nodes_held_in_memory, len(queue)) # Update the maximum number of nodes held in memory
        nodes_expanded += 1
        current_node = heapq.heappop(queue)[2] # Get the node from priority queue with least cost
        
        visited.add(current_node.getPos()) # Add node's coordinates to visited set

        # Return when current node coordinates match the goal coordinates
        if current_node.getPos() == goal:
            end_time = time.time()
            runtime_ms = (end_time-start_time)*1000 # Calculate runtime in milliseconds
            return calculatePath(current_node), calculateTotalCost(current_node), nodes_expanded, runtime_ms, max_nodes_held_in_memory
        
        # Iterate through possible moves
        for dx, dy in moves:
            new_x, new_y = current_node.x + dx, current_node.y + dy # Calculate the neighbor coordinates
            
            # Check that coordinates are valid and not yet visited
            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                new_node = Node(new_x, new_y, current_node, 0) # Create node using the neighbor coordinates
                new_node.cost = grid[new_x][new_y] + calculateHeuristic(current_node.getPos(), (new_x, new_y)) # Calculate cost of node traversal

                # If node is not in queue already, add it with the cost
                if (new_node.cost, id(new_node), new_node) not in queue:
                    heapq.heappush(queue, (new_node.cost, id(new_node), new_node))

    # Return if search failed
    end_time = time.time()
    runtime_ms = (end_time-start_time)*1000
    return [], 0, nodes_expanded, runtime_ms, max_nodes_held_in_memory

#declaring different functions to call
function_dict = {'bfs': bfs, 'iddfs': iddfs, 'astar': astar}

path, nodes_expanded, max_nodes_held_in_memory, runtime_ms = function_dict[algorithm](start, goal)

# Print the results
if not path:
    print("No path found.")
else:
    cost_of_path = len(path) - 1
    print("Cost of the path found:", cost_of_path)
    print("Number of nodes expanded:", nodes_expanded)
    print("Max nodes held in memory:", max_nodes_held_in_memory)
    print("Runtime in milliseconds:", runtime_ms)
    print("The path from %s to %s is" %(start, goal))
    for coordinate in path:
        print(coordinate)

# Check for the 3-minute time cutoff
if runtime_ms is not None and runtime_ms > 180000:
    print("Time cutoff reached (3 minutes).")

