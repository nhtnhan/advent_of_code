import sys


def dfs(map, i, j, flag, group):
    if map[i][j] != flag:
        return
    
    if flag == map[i][j]:
        group.append((i,j))

    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for di, dj in directions:
        if 0<=i+di<=len(map)-1 and 0<=j+dj<=len(map[i])-1 and (i+di, j+dj) not in group:
            dfs(map, i+di, j+dj, flag, group)

    return group

def calculate_perimeter_one(coords, map):
    if len(coords) == 1:
        return 4
    if len(coords) == 2:
        return 6
    if len(coords) == 3:
        return 8
    
    perimeter = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for i, j in coords:
        for di, dj in directions:
            ni, nj = i+di, j+dj
            
            if not(0<=ni<=len(map)-1 and 0<=nj<=len(map[0])-1) or (0<=ni<=len(map)-1 and 0<=nj<=len(map[0])-1 and map[ni][nj] != map[i][j]):
                perimeter+=1
    
    return perimeter        
    
    
def main():
    filename = sys.argv[1]
    map = []

    with open(filename, 'r') as f:
        for line in f.readlines():
            map.append(list(line.strip()))
    
    '''
    {'A': [(set containing added coords),[(1,1),(1,2)], [(1,3),(2,2)]],
     'B': []
    }
    '''
    key_to_island_group = {} # key:2d array
    key_to_added = {} # key:set


    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i,j) not in key_to_added.get(map[i][j], set()):
                if map[i][j] not in key_to_island_group:
                    group = dfs(map, i,j,map[i][j], [])
                    key_to_island_group[map[i][j]]=[group]
                    key_to_added[map[i][j]] = set(group)
                elif (i,j) not in key_to_added[map[i][j]]:
                    group = dfs(map, i,j,map[i][j], [])
                    key_to_island_group[map[i][j]].append(group)
                    key_to_added[map[i][j]].update(group)


    fence = 0
    for key in key_to_island_group:
        for group in key_to_island_group[key]:
            area = len(group)
            perimeter = calculate_perimeter_one(group, map)
            fence += area*perimeter
    
    print(fence)
    
if __name__ == '__main__':
    main()
    

        
        