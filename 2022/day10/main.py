import math

class Solution: 
    def main(self,filename):
        output=0
        with open(filename,"r") as f:
            cycle = 0
            x_total = 1
            lst = [20,60,100,140,180,220]

            lines = f.read().splitlines()
            for line in lines:
                if len(lst)==0:
                    print(output)
                    return
                
                if line.strip() == "noop":
                    cycle+=1
                else:
                    x = int(line.strip().split(" ")[1])
                    
                    cycle += 1
                    if cycle in lst:
                        signal = cycle * x_total
                        print(cycle,x_total)
                        lst.remove(cycle)
                        output+=signal

                    cycle += 1
                    if cycle in lst:
                        signal = cycle * x_total
                        print(cycle,x_total)
                        lst.remove(cycle)
                        output+=signal
                    
                    x_total+=int(x)
        return

    def print_CRT(self,CRT):
        for i in range(0,len(CRT),40):
            print(''.join(CRT[i:i+40]))

    def draw(self,sprite_pos,current_CRT,cycle):
        row = math.floor(cycle/40)
        index = cycle - 40 * row
        if sprite_pos <= index <= sprite_pos + 2:
            current_CRT[cycle-1] = "#"
        else:
            current_CRT[cycle-1] = "."
        return current_CRT

    def main2(self,filename):
        CRT = [str(i) for i in range(240)]

        with open(filename,"r") as f:
            cycle = 0
            sprite_pos = 1

            lines = f.read().splitlines()
            for line in lines:
                print(line,cycle,sprite_pos)
                if line.strip() == "noop":
                    cycle+=1
                    CRT = self.draw(sprite_pos,CRT,cycle)
                else:
                    x = int(line.strip().split(" ")[1])
                    
                    cycle += 1
                    CRT = self.draw(sprite_pos,CRT,cycle)

                    cycle += 1
                    CRT = self.draw(sprite_pos,CRT,cycle)

                    sprite_pos+=int(x)

        self.print_CRT(CRT)

sol = Solution()
sol.main2("input.txt")