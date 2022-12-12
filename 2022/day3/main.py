class Solution():
    def getPriority(self, letter):
        point = ord(letter.lower()) - 96
        if letter.isupper():
            point += 26
        return point


    def prioritySumOfSharedItems1(self,filename):
        f = open(filename,'r')

        priorities = []
        for line in f:
            clean_line = line.strip()
            first = clean_line[0:int((len(clean_line)/2))]
            second = clean_line[int((len(clean_line)/2)):len(clean_line)]
            common = set(first).intersection(set(second))
            priorities.append(self.getPriority(common.pop()))

        return sum(priorities)
        f.close()

    def prioritySumOfSharedItems3(self,filename):
        with open(filename, "r") as f:
            lines = f.readlines()
            priorities = []
            for i in range(0,len(lines),3):
                common = set.intersection(set(lines[i].strip()),set(lines[i+1].strip()),set(lines[i+2].strip()))
                priorities.append(self.getPriority(common.pop()))

        return sum(priorities)
        f.close()

sol = Solution()
print(sol.prioritySumOfSharedItems3('input.txt'))
