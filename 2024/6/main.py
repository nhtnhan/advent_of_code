def one(input):
    input = input.split("\n")
    coord = set()
    
    pos_row, pos_col = 0,0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '^':
                pos_row, pos_col = i,j

    row_increment = [-1,0,1,0]
    col_increment = [0,1,0,-1] 
    increment_pos = 0 # %4

    while 0 <= pos_row <= len(input)-1 and 0<=pos_col<=len(input[0])-1:
        if input[pos_row][pos_col] != '#':
            coord.add(f'{pos_row},{pos_col}')
        else:
            pos_row-=row_increment[increment_pos]
            pos_col-=col_increment[increment_pos]
            increment_pos = (increment_pos+1)%4
        
        pos_row+=row_increment[increment_pos]
        pos_col+=col_increment[increment_pos]

    return coord



# UP, RIGHT, DOWN, LEFT
ROW_INCREMENT = [-1, 0, 1, 0]  # for UP, RIGHT, DOWN, LEFT
COL_INCREMENT = [0, 1, 0, -1]  # for UP, RIGHT, DOWN, LEFT

def simulate_guard(input_map, start_row, start_col):
    visited = set()  # Track visited positions (row, col, direction)
    path = []  # To record the path for debugging

    # Directions: 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT
    directions = ['^', '>', 'v', '<']
    direction = 0  # The guard starts facing up
    
    row, col = start_row, start_col
    while 0 <= row < len(input_map) and 0 <= col < len(input_map[0]):
        # If the position and direction have already been visited, we are in a loop
        if (row, col, direction) in visited:
            return True  # The guard is stuck in a loop

        visited.add((row, col, direction))  # Mark the current position and direction as visited
        path.append((row, col, directions[direction]))  # Optional: For debugging

        # Check the next move
        next_row = row + ROW_INCREMENT[direction]
        next_col = col + COL_INCREMENT[direction]

        if 0 <= next_row < len(input_map) and 0 <= next_col < len(input_map[0]) and input_map[next_row][next_col] == '#':
            # If there's an obstacle, turn right (clockwise)
            direction = (direction + 1) % 4
        else:
            # Move forward
            row, col = next_row, next_col
    
    return False  # The guard doesn't loop and goes out of bounds

def part_two(input_map):
    input_map = [list(row) for row in input_map.split("\n")]  # Convert to list of lists for easier manipulation
    possible_positions = set()  # To store the positions where we could place the obstruction
    
    # Find the guard's starting position
    start_row, start_col = None, None
    for i in range(len(input_map)):
        for j in range(len(input_map[i])):
            if input_map[i][j] == '^':
                start_row, start_col = i, j
                input_map[i][j] = '.'  # Clear the starting point (replace '^' with empty space)
                break
        if start_row is not None:
            break
    
    # Check for empty spaces where an obstruction can be placed
    for i in range(len(input_map)):
        for j in range(len(input_map[i])):
            if input_map[i][j] == '.':
                # Try placing the obstruction at this position
                input_map[i][j] = '#'
                
                # Check if this causes the guard to loop
                if simulate_guard(input_map, start_row, start_col):
                    possible_positions.add((i, j))
                
                # Reset the space back to empty
                input_map[i][j] = '.'

    return len(possible_positions)