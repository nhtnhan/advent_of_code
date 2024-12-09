import sys

def calculate_checksum(display):
    output = 0
    
    for i in range(len(display)):
        if display[i] != '.':
            output+= i * int(display[i])    
    
    return output

def one(display):
    left = 0
    right = len(display)-1
    
    while left < right:
        while display[left] != '.':
            left+=1

        if left >= right:
            break
        
        display[left] = display[right]
        display[right] = '.'
        
        right-=1

    checksum = calculate_checksum(display)
    
    return checksum

def two(display):
    group_display = []
    key_to_count = {}

    current = display[0]
    count = 1
    
    
    for i in range(1, len(display)):
        if display[i] == current:
            count+=1
        else:
            group_display.append((current, count))
            if current != '.':
                key_to_count[current] = count 
            
            current = display[i]
            count = 1

    group_display.append((current, count))
    key_to_count[current] = count 
    max_number = int(max(key_to_count.keys()))

    for num in range(max_number, 0, -1):
        num = str(num)
        num_len = key_to_count[num]
        num_pos = group_display.index((num, num_len))
        
        for index, values in enumerate(group_display[:num_pos]):
            key, length = values
            
            if key == '.' and length >= num_len:
                group_display[num_pos] = ('.', num_len)
                group_display[index] = (num, num_len)

                remain_num = length - num_len
                
                if remain_num > 0:
                    group_display.insert(index+1, ('.', remain_num))
                    
                break
    
    
    output = ''
    for element, count in group_display:
        output+= element*count
    

    total = 0
    position = 0

    for item, size in group_display:
        if item is '.':
            position += size
        else:
            for n in range(size):
                total += int(item) * position
                position += 1
    
    print(total)
    

def main():
    filename = sys.argv[1]
    display = []
    
    with open(filename, 'r') as f:
        line = f.readline().strip()

        id = 0
        for i in range(len(line)):
            if i%2 == 0:
                for j in range(int(line[i])):
                    display.append(str(id))
                id+=1
            else:
                for j in range(int(line[i])):
                    display.append('.')
        
    # print(one(display))
    # print(two(display))

if __name__ == '__main__':
    main()
