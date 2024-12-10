import sys

def dfs_two(map, i, j, visited):
    current =  int(map[i][j])

    if current == 9:
        return 1
    
    total = 0

    directions = [(-1,0), (1,0),(0,-1),(0,1)]        
    for di, dj in directions:
        ni, nj = i+di, j+dj
        
        if 0<=ni<len(map) and 0<=nj<len(map[0]) and map[ni][nj] != '.' and (ni,nj) not in visited and int(map[ni][nj])==current+1:
            visited.add((ni,nj))
            
            total+=dfs_two(map,ni,nj, visited)

            visited.remove((ni,nj))
            
    return total

def dfs_one(map, i, j, visited):
    current =  int(map[i][j])

    if current == 9:
        return 1
    
    total = 0

    directions = [(-1,0), (1,0),(0,-1),(0,1)]        
    for di, dj in directions:
        ni, nj = i+di, j+dj
        
        if 0<=ni<len(map) and 0<=nj<len(map[0]) and map[ni][nj] != '.' and (ni,nj) not in visited and int(map[ni][nj])==current+1:
            visited.add((ni,nj))
            total+=dfs_one(map,ni,nj, visited)

            
    return total

def main():
    filename = sys.argv[1]
    map = []

    with open(filename, 'r') as f:
        content = f.read().strip()
        for line in content.split("\n"):
            map.append(list(line))
    
    count =  0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '0':
                # result = dfs_one(map, i,j, set((i,j)))
                result = dfs_two(map, i,j, set((i,j)))
                count+=result
 
    print(count)
if __name__ == '__main__':
    main()