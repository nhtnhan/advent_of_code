class Solution():
    def processInput(self,filename):
        array = []
        with open(filename, "r") as f:
            for line in f:
                row = [int(char) for char in line.strip()]
                array.append(row)
        return array

    def isVisible(self,row,col,array):
        row_count = len(array)
        col_count = len(array[0])
        tree = array[row][col]
        
        left = array[row][:col]
        if tree > max(left): return True

        right = array[row][col+1:]
        if tree > max(right): return True

        top = [array[i][col] for i in range(0,row)]
        if tree > max(top): return True

        bottom = [array[i][col] for i in range(row+1,row_count)]
        if tree > max(bottom): return True

        return False

    def scenicScore(self,row,col,array):
        row_count = len(array)
        col_count = len(array[0])
        tree = array[row][col]
        
        left_count = 0
        left = array[row][:col]
        for item in left[::-1]:
            if item < tree: left_count+=1
            else: 
                left_count+=1 
                break
        if left_count == 0 : left_count = 1

        right_count = 0
        right = array[row][col+1:]
        for item in right:
            if item < tree: right_count+=1
            else: 
                right_count+=1 
                break
        if right_count == 0 : right_count = 1

        top_count = 0
        top = [array[i][col] for i in range(0,row)]
        for item in top[::-1]:
            if item < tree: top_count+=1
            else: 
                top_count+=1 
                break
        if top_count==0: top_count = 1 

        bottom_count = 0   
        bottom = [array[i][col] for i in range(row+1,row_count)]
        for item in bottom:
            if item < tree: bottom_count+=1
            else: 
                bottom_count+=1 
                break
        if bottom_count==0: bottom_count = 1 
        
        return left_count*right_count*top_count*bottom_count

    def main(self,filename):
        array = self.processInput(filename)

        row_count = len(array)
        col_count = len(array[0])
        output = 0

        for i in range(row_count):
            for j in range(col_count):
                if i in [0, row_count-1]: output+=1
                elif j in [0, col_count-1]: output+=1
                else: 
                    if (self.isVisible(i,j,array)): output+=1

        print(output)
        return

    def main2(self,filename):
        array = self.processInput(filename)

        row_count = len(array)
        col_count = len(array[0])
        output = []

        for i in range(row_count):
            for j in range(col_count):
                if i not in [0, row_count-1] and j not in [0, col_count-1]:
                    output.append(self.scenicScore(i,j,array))

        print(max(output))
        return

sol = Solution()
sol.main2("input.txt")        