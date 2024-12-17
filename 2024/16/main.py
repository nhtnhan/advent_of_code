def parse_input(filename):
    map = []
    with open(filename, 'r') as f:
        content = f.read().strip().split("\n")
        map = [list(line) for line in content]
    
    return map

def rotate_with_cost(direction, current):
    match current:
        case 'E':
            match direction:
                case (1,0):
                    return 'S', 1000
                case (-1,0):
                    return 'N', 1000 
                case (0,1):
                    return 'E', 0
                case (0,-1):
                    return 'W', 2000
        case 'W':
            match direction:
                case (1,0):
                    return 'S', 1000
                case (-1,0):
                    return 'N', 1000 
                case (0,1):
                    return 'W', 0
                case (0,-1):
                    return 'E', 2000
        case 'N':
            match direction:
                case (1,0):
                    return 'S', 2000
                case (-1,0):
                    return 'N', 0 
                case (0,1):
                    return 'W', 1000
                case (0,-1):
                    return 'E', 1000
        case 'S':
            match direction:
                case (1,0):
                    return 'S', 0
                case (-1,0):
                    return 'N', 2000
                case (0,1):
                    return 'W', 1000
                case (0,-1):
                    return 'E', 1000 

def find_pos(letter, map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == letter:
                return i,j

class Cell:
    def __init__(self):
        # parent cell's row index
        self.parent_i = 0
        # parent cell's col index
        self.parent_j = 0
        # total cost of the cell (g+h)
        self.f = float('inf')
        # cost from start to this cell
        self.g = float('inf')
        # heuristic cost from this cell to destination
        self.h = 0
        # current facing at this cell
        self.facing = 'E'
        

def cal_h(i,j, dst_i, dst_j):
    return ((i-dst_i)**2 + (j-dst_j)**2)** 0.5

def astar(paths, start_i, start_j, dst_i, dst_j, start_facing):
    import math
    import heapq
    
    closed_list = [[False for _ in range(len(paths[0]))] for _ in range(len(paths))] # contains visited cell
    cell_details = [[Cell() for _ in range(len(paths[0]))] for _ in range(len(paths))] # contains detail of a cell at i,j

    cell_details[start_i][start_j].f = 0
    cell_details[start_i][start_j].h = 0
    cell_details[start_i][start_j].g = 0
    cell_details[start_i][start_j].parent_i = start_i
    cell_details[start_i][start_j].parent_j = start_j
    cell_details[start_i][start_j].facing = start_facing
    
    open_list = [] # contain cells to visit
    heapq.heappush(open_list, (0.0,start_i,start_j))

    found_dst = False
    
    while len(open_list) > 0:
        p = heapq.heappop(open_list)
        
        i = p[1]
        j = p[2]
        closed_list[i][j] = True
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj

            if 0 <= ni < len(paths) and 0 <= nj < len(paths[0]) and paths[ni][nj] != '#' and not closed_list[ni][nj]:
                if paths[ni][nj] == 'E':
                    cell_details[ni][nj].parent_i = i
                    cell_details[ni][nj].parent_j = j
                    n_facing, turn_pts = rotate_with_cost((di, dj), cell_details[i][j].facing)
                    g_new = cell_details[i][j].g + 1.0 + turn_pts
                    found_dst =  True
                    return g_new
                else:
                    n_facing, turn_pts = rotate_with_cost((di, dj), cell_details[i][j].facing)
                    g_new = cell_details[i][j].g + 1 + turn_pts
                    h_new = cal_h(ni, nj, dst_i, dst_j)
                    f_new = g_new+h_new

                    if cell_details[ni][nj].f == float('inf') or cell_details[ni][nj].f > f_new:
                        heapq.heappush(open_list, (f_new, ni, nj))
                        cell_details[ni][nj].f = f_new
                        cell_details[ni][nj].g = g_new
                        cell_details[ni][nj].h = h_new
                        cell_details[ni][nj].parent_i = i
                        cell_details[ni][nj].parent_j = j
                        cell_details[ni][nj].facing = n_facing
        
    if not found_dst:
        print("not found")


def main(filename):
    map = parse_input(filename)
    
    '''
    min path finding algo: a* search
    '''
    
    start_i, start_j = find_pos('S', map)
    end_i, end_j = find_pos('E', map)
                    

    result = astar(map, start_i, start_j, end_i, end_j, 'E')
    print(result)
         
    

main('one.txt')
main('two.txt')
main('input.txt')