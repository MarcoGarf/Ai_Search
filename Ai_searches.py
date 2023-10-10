from collections import deque
import sys

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

def iddfs(start, goal):
    depth_limit = 0
    
    while True:
        result = dls(start, goal, depth_limit)
        if result is not None:
            return result  # Goal found
        depth_limit += 1  # Increase depth limit if goal not found at current depth

def dls(node, goal, depth_limit):
    stack = [(node, [])]
    
    while stack:
        (x, y), path = stack.pop()  # Pop the last coordinate and its corresponding path

        if (x, y) == goal:
            return path + [(x, y)]  # Return the path to the goal

        if len(path) < depth_limit:
            for dx, dy in moves:
                new_x, new_y = x + dx, y + dy  # Calculate new coordinates by adding the move (dx, dy) to the current coordinates (x, y)

                if is_valid(new_x, new_y):
                    # Calculate the new coordinates based on the possible moves
                    new_path = path + [(x, y)]  # Extend the path
                    stack.append(((new_x, new_y), new_path))

    return None  # Goal not found at this depth


#declaring different functions to call
function_dict = {'bfs': bfs, 'iddfs': iddfs}


# Call the BFS function and get the result

#Testing code for the user to choose their algorithm of choice to search
path = function_dict[algorithm](start, goal)

if path:
    print("The path from %s to %s is" %(start, goal))
    for coordinate in path:
        print(coordinate)
else:
    print("There is no path from %s to %s." %(start, goal))
