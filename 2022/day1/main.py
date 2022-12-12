class Solution(object):
    def maxCalorie(self,filename):
        f = open(filename, "r")
        
        maxCalorie = 0
        flagCalorie = 0
        for line in f:
            if (line.strip() != ''):
                number = int(line.strip())
                flagCalorie += number
            else:
                maxCalorie = max(maxCalorie, flagCalorie)
                flagCalorie = 0
        print(maxCalorie)
        f.close()

    def topThreeCalories(self,filename):
        f = open(filename, "r")
        
        flagCalorie = 0
        calories = []
        for line in f:
            if (line.strip() != ''):
                number = int(line.strip())
                flagCalorie += number
            else:
                calories.append(flagCalorie)
                flagCalorie = 0
        
        calories.sort()
        print(calories[-1]+calories[-2]+calories[-3])
        f.close()

sol = Solution()
print(sol.countCalorie('input.txt'))
