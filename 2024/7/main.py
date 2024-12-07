def generate_combinations(elements, n):
    # Base case: if n is 1, return each element as a single-item list
    if n == 1:
        return [[el] for el in elements]

    # Recursive case: append each element to combinations of size (n-1)
    combinations = []
    for comb in generate_combinations(elements, n - 1):
        for el in elements:
            combinations.append(comb + [el])
    
    return combinations


def one(input):
    output = 0
    operations = ["*","+"]

    for line in input.split("\n"):
        total, right = line.split(":")
        total = int(total)

        nums = right.strip().split(" ")        
        combinations = generate_combinations(operations, len(nums)-1)
        
        # different combinations of nums and combinations, always start with num and end with num 
        exp = ""
        for comb in combinations:
            for i in range(len(nums)):
                exp+=nums[i]
                
                if i>0:
                    exp = str(eval(exp))

                if i < len(comb):
                    exp+=comb[i]

            if eval(exp) == total:
                output+=total
                break
            exp = ""

    print(output)


def two(input):
    output = 0
    operations = ["*","+", "||"]

    for line in input.split("\n"):
        total, right = line.split(":")
        total = int(total)

        nums = right.strip().split(" ")        
        combinations = generate_combinations(operations, len(nums)-1)
        
        # different combinations of nums and combinations, always start with num and end with num 
        for comb in combinations:
            last = ""
            current = []

            for i in range(len(nums)):
                current.append(int(nums[i]))
                
                if i>0:
                    if last == "*":
                        new = current[0] * current[1]
                        current = [new]
                    elif last == "+":
                        new = current[0] + current[1]
                        current = [new]
                    else:
                        new = int(str(current[0])+str(current[1]))
                        current = [new]

                if i < len(comb):
                    last = comb[i]

            if current[0] == total:
                output+=total
                break

    print(output)


two(input)