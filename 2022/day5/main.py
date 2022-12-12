class Solution:
    def topCrates9000(self,filename):
        crates = {
            '1': ['D', 'H', 'R', 'Z', 'S', 'P', 'W','Q'],
            '2': ['F', 'H', 'Q', 'W','R', 'B','V'],
            '3': ['H','S', 'V','C'],
            '4': ['G', 'F','H'],
            '5': ['Z', 'B', 'J', 'G', 'P'],
            '6': ['L', 'F', 'W', 'H', 'J', 'T', 'Q'],
            '7': ['N', 'J', 'V', 'L', 'D', 'W', 'T', 'Z'],
            '8': ['F','H','G','J','C','Z','T','D'],
            '9': ['H','B','M','V','P','W']
        }
        with open(filename, "r") as f:
            for line in f:
                a, amount, b, src, c, dest = line.strip().split(' ')
                for i in range(int(amount)):
                    crates[dest] = [crates[src].pop(0)] + crates[dest]
        for key,val in crates.items():
            print(crate)
    def topCrates9001(self,filename):
        crates = {
            '1': ['D', 'H', 'R', 'Z', 'S', 'P', 'W','Q'],
            '2': ['F', 'H', 'Q', 'W','R', 'B','V'],
            '3': ['H','S', 'V','C'],
            '4': ['G', 'F','H'],
            '5': ['Z', 'B', 'J', 'G', 'P'],
            '6': ['L', 'F', 'W', 'H', 'J', 'T', 'Q'],
            '7': ['N', 'J', 'V', 'L', 'D', 'W', 'T', 'Z'],
            '8': ['F','H','G','J','C','Z','T','D'],
            '9': ['H','B','M','V','P','W']
        }
        with open(filename, "r") as f:
            for line in f:
                a, amount, b, src, c, dest = line.strip().split(' ')
                if int(amount) > 1:
                    move = crates[src][:int(amount)]
                    crates[src] = crates[src][int(amount):]
                    crates[dest] = move + crates[dest]
                else:
                    crates[dest] = [crates[src].pop(0)] + crates[dest]
                print(line.strip())
            for key,val in crates.items():
                print(val[0])

sol = Solution()
sol.topCrates9001('input.txt')