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
    
    print(display)

    end = len(display)-1
    for start in range(len(display)-1,-1,-1):        
        if display[start] != display[end]:            
            if display[end] != '.':
                # move display[start+1:end+1] to furthest left same-length of contiguous '.' 
                print(display[start+1:end+1])    

            # start new
            end = start
        

    checksum = calculate_checksum(display)
    
    return checksum


if __name__ == '__main__':
    main()
