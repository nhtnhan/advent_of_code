def astar(grid, start, end):
    from heapq import heappop, heappush
    
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    heap = [(0, *start)]
    visited = set()
    found_dst =  False

    while heap:
        score, i, j = heappop(heap)
        if (i,j) == end:
            found_dst =  True
            break
        if (i,j) in visited:
            continue
        
        visited.add((i,j))
        
        for d in directions:
            x = i+d[0]
            y = j+d[1]
            
            if 0 <= x <= len(grid)-1 and 0 <= y <= len(grid[0])-1:
                if grid[x][y] == '.' and (x,y) not in visited:
                    heappush(heap, (score+1,x,y))
    
    return score,found_dst

def main(filename, dim, stop):
    bytes = []
    with open(filename, 'r') as f:
        bytes = [tuple([int(txt) for txt in line.split(',')]) for line in f.read().splitlines()]
        
    grid = [['.' for i in range(dim)] for j in range(dim)]

    for i in range(stop):
        y, x = bytes[i]
        grid[x][y] = '#'
        
    # part 1:
    # length, _ = astar(grid, (0,0), (dim-1,dim-1))
    # print(f'shortest path after {stop} bytes fell: {length}')
    
    # part 2:
    # test can start at 7-end, input can start at 71 to end (or do bottom up instead)
    for i in range(stop+1, len(bytes)):
        y, x = bytes[i]
        grid[x][y] = '#'

        length, found = astar(grid, (0,0), (dim-1,dim-1))
        if not found:
            print(bytes[i])
            break

# main('test.txt',7, 12)
main('input.txt',71, 1024)