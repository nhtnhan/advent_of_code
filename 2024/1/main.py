def one(input):
    left, right = [], []
    for line in input.split('\n'):
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))
    
    left.sort()
    right.sort()
    
    output = 0
    for l, r in zip(left, right):
        output+= abs(l-r)
    
    print(output)

def two(input):
    left, right_counter = [], {}
    for line in input.split('\n'):
        l, r = line.split("   ")

        left.append(int(l))

        right_counter[int(r)] = right_counter.get(int(r),0)+1
        
    output = 0
    for num in left:
        output+= num*right_counter.get(num,0) 
    
    print(output) 

two(input)   