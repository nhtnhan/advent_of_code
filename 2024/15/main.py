def part1(map, moves):
    grid = map
    directions = moves
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                robot = (i, j)
                grid[i][j] = '.'

    for d in directions[:]:
        i, j = robot
        
        if d == '<':
            k = j-1
            while grid[i][k] == 'O':
                k -= 1
            if grid[i][k] == '.':
                grid[i][k], grid[i][j-1] = grid[i][j-1], grid[i][k]
                robot = (i, j-1)

        elif d == '>':
            k = j+1
            while grid[i][k] == 'O':
                k += 1
            if grid[i][k] == '.':
                grid[i][k], grid[i][j+1] = grid[i][j+1], grid[i][k]
                robot = (i, j+1)

        elif d == '^':
            k = i-1
            while grid[k][j] == 'O':
                k -= 1
            if grid[k][j] == '.':
                grid[k][j], grid[i-1][j] = grid[i-1][j], grid[k][j]
                robot = (i-1, j)

        elif d== 'v':
            k = i+1
            while grid[k][j] == 'O':
                k += 1
            if grid[k][j] == '.':
                grid[k][j], grid[i+1][j] = grid[i+1][j], grid[k][j]
                robot = (i+1, j)

    print_map(grid)
    total = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'O':
                total += 100*i + j
    
    print(total)
    return total


def parse_input(filename):
    map = []
    moves = []
    with open(filename) as f:
        map_txt, moves_txt = f.read().split("\n\n")
        map = [list(line) for line in map_txt.split("\n")]
        moves = list(''.join(line for line in moves_txt.split("\n")))
    
    return map, moves

def move_robot(grid, x, y, direction):
    rows, cols = len(grid), len(grid[0])
    dx, dy = direction
    
    nx, ny = x + dx, y + dy
    
    if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] == '#':
        return  # Cannot move in this direction

    # If the robot encounters a box
    if grid[nx][ny] == 'O':
        # Calculate the position beyond the box
        box_nx, box_ny = nx + dx, ny + dy
        
        # Check if the box can be pushed
        if (0 <= box_nx < rows and 0 <= box_ny < cols):
            if grid[box_nx][box_ny] == '.':
                # Push the box
                grid[box_nx][box_ny] = 'O'
                grid[nx][ny] = '.'
                
                # Move the robot to the box's original position
                grid[x][y] = '.'
                grid[nx][ny] = '@'
            elif grid[box_nx][box_ny] == 'O':
                # Recursively try to push further boxes in the same direction
                move_robot(grid, box_nx, box_ny, direction)
    elif grid[nx][ny] == '.':
        # Move the robot to the free path
        grid[x][y] = '.'
        grid[nx][ny] = '@'
    else:
        return  # Hit a wall or obstacle

def get_direction(move):
    if move == '^':
        return (-1,0)
    elif move == 'v':
        return (1,0)
    elif move == '>':
        return (0,1)
    elif move == '<':
        return (0,-1)

def print_map(map):
    for row in map:
        print(row)

def main(filename):
    map, moves = parse_input(filename)

    part1(map, moves)
    # for move in moves:
    #     direction = get_direction(move)
    #     for i in range(len(map)):
    #         for j in range(len(map[i])):
    #             if map[i][j] == '@':
    #                 print(move)
    #                 move_robot(map,i,j,direction)
    #                 print_map(map)

    
    # print_map(map)
    
    
main('input.txt')