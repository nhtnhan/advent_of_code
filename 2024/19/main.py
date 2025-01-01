def can_construct(options, word):
    dp = [False for i in range(len(word)+1)]
    dp[0] = True # empty string can always be constructed
    
    for i in range(1, len(word) + 1):
        for option in options:
            if i >= len(option) and word[i-len(option):i] == option:
                dp[i] = dp[i] or dp[i - len(option)]
                
                if dp[i] == True:
                    break
    
    return dp[-1]

def count_construct_ways(options, target):
    n = len(target)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: 1 way to construct an empty string
    
    for i in range(1, n + 1):
        for option in options:
            if i >= len(option) and target[i-len(option):i] == option:
                dp[i] += dp[i - len(option)]
    
    return dp[n]

def main(filename):
    patterns = set()
    designs = [] 
    
    with open(filename, 'r') as f:
        patterns_txt, designs_txt = f.read().split("\n\n")
        patterns = set(patterns_txt.split(", "))
        designs = designs_txt.split("\n")
    
    count = 0
    
    # part 1:
    # for design in designs:
    #     if can_construct(patterns, design):
    #         count+=1
    
    # part 2:
    for design in designs:
        count += count_construct_ways(patterns, design)

    print(count)

main('test.txt')
# main('input.txt')
        