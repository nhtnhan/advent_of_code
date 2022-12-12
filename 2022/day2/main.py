class Solution():
    def totalScoreFromYourGuess(self, filename):
        f = open(filename,"r")

        points = {
            'X': {
                'A': 3+1,
                'B': 0+1,
                'C': 6+1
            },
            'Y': {
                'A': 6+2,
                'B': 3+2,
                'C': 0+2,
            },
            'Z': {
                'A': 0+3,
                'B': 6+3,
                'C': 3+3,
            }
        }
        total = 0
        for line in f:
            they, you = line.strip().split(' ')
            total+=points[you][they]
        f.close()
        return total

    def totalScoreFromElfStrategy(self, filename):
        f = open(filename,"r")

        points = {
            'X': {
                'A': 0+3,
                'B': 0+1,
                'C': 0+2
            },
            'Y': {
                'A': 3+1,
                'B': 3+2,
                'C': 3+3,
            },
            'Z': {
                'A': 6+2,
                'B': 6+3,
                'C': 6+1,
            }
        }
        total = 0
        for line in f:
            they, you = line.strip().split(' ')
            total+=points[you][they]
        f.close()
        return total

sol = Solution()
print(sol.totalScoreFromElfStrategy('input.txt'))