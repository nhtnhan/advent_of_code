import sys

def within_valid_range(value, maximum, minimum):
    return minimum<=value<=maximum

def one(antenna_to_pos, max_col, max_row):
    antinode_pos = set()
    
    for key in antenna_to_pos:
        if len(antenna_to_pos[key]) <= 1:
            continue
        
        values = antenna_to_pos[key]
        for i in range(len(values)-1):
            first_y, first_x = values[i]
    
            for j in range(i+1, len(values)):

                second_y, second_x = values[j]
                
                diff_x, diff_y = abs(first_x-second_x), abs(first_y-second_y)
                
                antinode_second_pos_y = second_y+diff_y if second_y > first_y else second_y-diff_y
                antinode_second_pos_x = second_x+diff_x if second_x > first_x else second_x-diff_x

                if within_valid_range(antinode_second_pos_x, max_col, 0) and within_valid_range(antinode_second_pos_y, max_row, 0):
                    antinode_pos.add((antinode_second_pos_x, antinode_second_pos_y))

                antinode_first_pos_y = first_y+diff_y if first_y > second_y else first_y-diff_y
                antinode_first_pos_x = first_x+diff_x if first_x > second_x else first_x-diff_x
                
                if within_valid_range(antinode_first_pos_x, max_col, 0) and within_valid_range(antinode_first_pos_y, max_row, 0):
                    antinode_pos.add((antinode_first_pos_x, antinode_first_pos_y))
    return antinode_pos
    
def two(antenna_to_pos, max_col, max_row):
    antinode_pos = set()
    for key in antenna_to_pos:
        if len(antenna_to_pos[key]) <= 1:
            continue
        
        values = antenna_to_pos[key]
        for i in range(len(values)-1):
            first_y, first_x = values[i]
    
            for j in range(i+1, len(values)):
                second_y, second_x = values[j]
                
                diff_x, diff_y = abs(first_x-second_x), abs(first_y-second_y)
 
                antinode_second_pos_y = second_y
                antinode_second_pos_x = second_x
                second_diff_y = diff_y if second_y > first_y else -diff_y
                second_diff_x = diff_x if second_x > first_x else -diff_x                                

                while within_valid_range(antinode_second_pos_x, max_col, 0) and within_valid_range(antinode_second_pos_y, max_row, 0):
                    antinode_pos.add((antinode_second_pos_x, antinode_second_pos_y))
                    antinode_second_pos_y+=second_diff_y
                    antinode_second_pos_x+=second_diff_x 

                antinode_first_pos_y = first_y
                antinode_first_pos_x = first_x
                first_diff_y = diff_y if first_y > second_y else -diff_y
                first_diff_x = diff_x if first_x > second_x else -diff_x
                while within_valid_range(antinode_first_pos_x, max_col, 0) and within_valid_range(antinode_first_pos_y, max_row, 0):
                    antinode_pos.add((antinode_first_pos_x, antinode_first_pos_y))
                    antinode_first_pos_y+=first_diff_y
                    antinode_first_pos_x+=first_diff_x    
    
    return antinode_pos
    
def main():
    filename = sys.argv[1]
    antenna_to_pos = {}
    max_row, max_col = 0,0
        
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            line =  line.strip()
            for j in range(len(line)):
                if line[j] != '.':
                    if line[j] not in antenna_to_pos:
                        antenna_to_pos[line[j]] = []
                    antenna_to_pos[line[j]].append((i,j))
        
        max_row, max_col = i, len(line)-1

    # print(len(one(antenna_to_pos, max_col, max_row)))
    print(len(two(antenna_to_pos, max_col, max_row)))
                
if __name__ == '__main__':
    main()