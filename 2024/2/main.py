def one(input):
    count = 0
    for line in input.split("\n"):
        numbers = list(map(int, line.split()))
        safe = True
        diff = numbers[1] - numbers[0]
        for i in range(1, len(numbers)):
            if not (1 <= abs(numbers[i] - numbers[i-1]) <= 3 and (numbers[i] - numbers[i-1])*diff > 0):
                safe = False
                break 
        
        if safe:
            count += 1
    print(count) 

def is_safe(numbers):
    diff = numbers[1] - numbers[0]
    for i in range(1, len(numbers)):
        if not (abs(numbers[i] - numbers[i-1]) != 0 and 1 <= abs(numbers[i] - numbers[i-1]) <= 3 and (numbers[i] - numbers[i-1])*diff > 0):
            return False
    return True

def two(input):
    count = 0
    for line in input.split("\n"):        
        removed = 0
        safe = False 
        numbers = list(map(int, line.split()))

        if is_safe(numbers):
            safe = True
            removed = 0
        else:
            for i in range(len(numbers)):
                if is_safe(numbers[:i] + numbers[i+1:]):
                    removed += 1


        if safe or removed > 0:
            count += 1
    print(count)

two(input)