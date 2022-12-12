class Solution:
    def sameCol(self,h_pos,t_pos):
        return int(h_pos.split(" ")[0]) == int(t_pos.split(" ")[0])
    
    def sameRow(self,h_pos,t_pos):
        return int(h_pos.split(" ")[1]) == int(t_pos.split(" ")[1])
    
    def moveTail(self,h_pos,t_pos):
        h_x, h_y = h_pos.split(" ")
        t_x, t_y = t_pos.split(" ")

        if self.sameRow(h_pos,t_pos) and int(h_x)-int(t_x) == 2:
            return f'{int(t_x)+1} {int(t_y)}'

        if self.sameRow(h_pos,t_pos) and int(h_x)-int(t_x) == -2:
            return f'{int(t_x)-1} {int(t_y)}'

        if self.sameCol(h_pos,t_pos) and int(h_y)-int(t_y)==2:
            return f'{int(t_x)} {int(t_y)+1}'

        if self.sameCol(h_pos,t_pos) and int(h_y)-int(t_y)==-2:
            return f'{int(t_x)} {int(t_y)-1}'

        if not self.sameCol(h_pos,t_pos) and not self.sameCol(h_pos,t_pos) and int(h_y)-int(t_y) == 2:
            return f'{int(h_x)} {int(t_y)+1}'

        if not self.sameCol(h_pos,t_pos) and not self.sameCol(h_pos,t_pos) and int(h_y)-int(t_y) == -2:
            return f'{int(h_x)} {int(t_y)-1}'

        if not self.sameCol(h_pos,t_pos) and not self.sameCol(h_pos,t_pos) and int(h_x)-int(t_x) == 2:
            return f'{int(t_x)+1} {int(h_y)}'

        if not self.sameCol(h_pos,t_pos) and not self.sameCol(h_pos,t_pos) and int(h_x)-int(t_x) == -2:
            return f'{int(t_x)-1} {int(h_y)}'

        return t_pos

    def moveHead(self,pos,direction,step):
        match direction.upper():
            case "U":
                x,y = pos.split(" ")
                return f'{int(x)} {int(y)+1}'
            case "D":
                x,y = pos.split(" ")
                return f'{int(x)} {int(y)-1}'
            case "L":
                x,y = pos.split(" ")
                return f'{int(x)-1} {int(y)}'
            case "R":
                x,y = pos.split(" ")
                return f'{int(x)+1} {int(y)}'
            case _:
                return pos
                
    def main(self,filename):
        with open(filename,"r") as f:
            lines = f.read().splitlines()
            h_pos = "0 0"
            t_pos = "0 0"
            t_pos_set = {t_pos}
            for line in lines:
                direction, amount = line.strip().split(" ")
                for i in range(int(amount)):
                    h_pos = self.moveHead(h_pos,direction,i)
                    t_pos = self.moveTail(h_pos,t_pos)
                    t_pos_set.add(t_pos)
            print(len(t_pos_set))

    def inferDirectionAndStep(self,old_pos,new_pos):
        old_x, old_y = old_pos.split(" ")
        new_x, new_y = new_pos.split(" ")
        if int(new_x) - int(old_x) == 1:
            return "R"
        
        if int(new_x) - int(old_x) == -1:
            return "L"

        if int(new_y) - int(old_y) == 1:
            return "U"

        if int(new_y) - int(old_y) == -1:
            return "D"
        
        return "STAY"

    def moveHeadAndTail(self,h_pos,direction,i,t_pos):
        new_h_pos = self.moveHead(h_pos,direction,i)
        direction = self.inferDirectionAndStep(new_h_pos,h_pos)
        new_t_pos = self.moveTail(h_pos,t_pos)
        return new_h_pos,new_t_pos,direction 

    def main2(self,filename):
        with open(filename,"r") as f:
            lines = f.read().splitlines()
            h_pos = "0 0"
            pos_2 = "0 0"
            pos_3 = "0 0"
            pos_4 = "0 0"
            pos_5 = "0 0"
            pos_6 = "0 0"
            pos_7 = "0 0"
            pos_8 = "0 0"
            t_pos = "0 0"

            t_pos_set = {t_pos}
            for line in lines:
                direction, amount = line.strip().split(" ")
                for i in range(int(amount)):
                    h_pos, pos_2, new_direction1 = self.moveHeadAndTail(h_pos,direction,i,pos_2)
                    pos_2, pos_3, new_direction2 = self.moveHeadAndTail(pos_2,new_direction1,i,pos_3)
                    pos_3, pos_4, new_direction3 = self.moveHeadAndTail(pos_3,new_direction2,i,pos_4)
                    pos_4, pos_5, new_direction4 = self.moveHeadAndTail(pos_4,new_direction3,i,pos_5)
                    pos_5, pos_6, new_direction5 = self.moveHeadAndTail(pos_5,new_direction4,i,pos_6)
                    pos_6, pos_7, new_direction6 = self.moveHeadAndTail(pos_6,new_direction5,i,pos_7)
                    pos_7, pos_8, new_direction7 = self.moveHeadAndTail(pos_7,new_direction6,i,pos_8)
                    pos_8, t_pos, new_direction8 = self.moveHeadAndTail(pos_8,new_direction7,i,t_pos)
                    t_pos_set.add(t_pos)
            print(len(t_pos_set))
                

sol = Solution()
sol.main2('input.txt')