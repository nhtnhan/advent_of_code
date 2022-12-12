class Solution():
    def fullyContainPairs(self,filename):
        count = 0
        with open(filename, 'r') as f:            
            for line in f:
                # extract
                first,second = line.strip().split(',')
                first_s, first_e = first.strip().split('-')
                second_s, second_e = second.strip().split('-')

                # for a pair to be fully contain by the other: 
                # 6-6 2-6: (start1 > start2 && end1 <= end2) || (reverse)
                # 2-4 2-6: (start1 = start2 && end1 <= end2) || (reverse)
                # 2-4 1-7: (start1 > start2 && end1 < end2) || (reverse) 
                # 27-62 9-26: 
                # 1-7 2-4: (start2 > start1 && end2 < end1) 
                if ((int(first_s) >= int(second_s) and int(first_e) <= int(second_e)) or (int(second_s) >= int(first_s) and int(second_e) <= int(first_e))):
                    count+=1
        return count
    def overlapPairs(self,filename):
        count = 0
        with open(filename, 'r') as f:            
            for line in f:
                # extract
                first,second = line.strip().split(',')
                first_s, first_e = first.strip().split('-')
                second_s, second_e = second.strip().split('-')
                # for a pair to be overlap: 
                # 6-6 2-6: (start1 > start2 && end1 <= end2) || (reverse)
                # 2-4 2-6: (start1 = start2 && end1 <= end2) || (reverse)
                # 2-4 1-6: (start1 > start2 && end1 < end2) || (reverse) 
                # 27-62 9-27:
                # 2-4 6-8
                # 2-6,4-8: start2 >= start1 && end1 > start2
                # 4-8,2-6: start1 >= start2 && end2 > start1
                fullyContain1 = int(first_s) >= int(second_s) and int(first_e) <= int(second_e)
                fullyContain2 = int(second_s) >= int(first_s) and int(second_e) <= int(first_e)
                overlap1 = int(first_s) == int(second_e) or int(first_e) == int(second_s)
                overlap2 = int(second_s) >= int(first_s) and int(first_e) > int(second_s)
                overlap3 = int(first_s) >= int(second_s) and int(second_e) > int(first_s)
                if (fullyContain1 or fullyContain2 or overlap1 or overlap2 or overlap3):
                    count+=1
        return count
sol = Solution()
print(sol.overlapPairs('input.txt'))