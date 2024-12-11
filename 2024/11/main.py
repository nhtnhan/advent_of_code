text = '125 17'
input = '5 127 680267 39260 0 26 3553 5851995'
import sys

def trim_trailing_zero(num_str):
    start = 0
    for i in range(len(num_str)):
        if num_str[i] != '0':
            break
        start+=1

    if start == len(num_str):
        return '0'
    
    return num_str[start:]            


def main(input):
    blink = int(sys.argv[1])
    nums = input.split(" ")

    counter = {}
    for num in nums:
        counter[num] = counter.get(num,0)+1
    
    for i in range(blink):
        new_counter = {}
        
        for key in counter:
            count = counter[key]
            
            if len(key)%2 == 0:
                left = trim_trailing_zero(key[:len(key)//2])
                if left:
                    new_counter[left] = new_counter.get(left,0) + count
                
                right = trim_trailing_zero(key[len(key)//2:])
                if right:
                    new_counter[right] = new_counter.get(right,0) + count
            elif key == '0':
                new_counter['1'] = new_counter.get('1',0) + count
            else:
                new_counter[str(int(key)*2024)] =  new_counter.get(str(int(key)*2024),0) + count 
        
        counter = new_counter
    
    # print(counter)
    print(sum(counter.values()))
    # print(nums)
    

main(input)
    