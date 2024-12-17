import sys

def main():
    '''
    The cheapest way to win the prize is by pushing the A button 80 times and the B button 40 times. 
    This would line up the claw along the X axis (because 80*94 + 40*22 = 8400) and along the Y axis (because 80*34 + 40*67 = 5400). 
    Doing this would cost 80*3 tokens for the A presses and 40*1 for the B presses, a total of 280 tokens.
    
    80*94+40*22 = 8400
    80*34+40*67 = 5400
    
    80*(94+34)+40*(22+67) = 8400+5400
    
    [(94, 34), (22, 67), (8400, 5400)]
      (A, B), (C,D), (E,F)
      
      A*i + C*j = E
      B*i + D*j = F
      
      (A+B)*i + (C+D)*j = E+F
      => i = [(E+F) - (C+D)*j] / (A+B)
    
    [(26, 66), (67, 21), (12748, 12176)]
    [(17, 86), (84, 37), (7870, 6450)]
    [(69, 23), (27, 71), (18641, 10279)]
    '''
    
    
    filename = sys.argv[1]
    machines = [] # array of 3 tuples, first two is claw, last is prize coord

    with open(filename,'r') as f:
        content = f.read().split("\n\n")
        for group in content:
            a, b, prize = group.split("\n")
            
            left_a, right_a = a.split(", ")
            x_a = left_a.split("+")[-1]
            y_a = right_a.split("+")[-1]
            
            left_b, right_b = b.split(", ")
            x_b = left_b.split("+")[-1]
            y_b = right_b.split("+")[-1]
            
            left_prize, right_prize = prize.split(", ")
            x_prize = left_prize.split("=")[-1]
            y_prize = right_prize.split("=")[-1]
                            
            machines.append([(int(x_a),int(y_a)), (int(x_b),int(y_b)), (int(x_prize), int(y_prize))])
    
    #  i = [(E+F) - (C+D)*j] / (A+B)
    token = 0
    for a_moves, b_moves, prize_pos in machines:
        minimum = float('inf')
        for i in range(101):
            j = (sum(prize_pos) - sum(b_moves)*i)/sum(a_moves)
            if (sum(prize_pos) - sum(b_moves)*i)%sum(a_moves) == 0 and 0 <=j<=100:
                minimum = min(minimum,int(3*j+1*i))
        if isinstance(minimum, int):
            token+=minimum
    print(token)

def sol():
    def find_solution(claw, incr=0):
        a,b,prize = claw
        ax, ay = a
        bx, by = b
        px, py = prize
        px += incr  # For part 2
        py += incr
        solution_a, solution_b = None, None  # If the solution isn't an integer, it will stay "None"

        # This nasty equation was worked out using algebra. If you're curious, see my comment on reddit here:
        # https://www.reddit.com/r/adventofcode/comments/1hd7irq/comment/m1xtxxc/
        if (bx * py - by * px) / (bx * ay - by * ax) == (bx * py - by * px) // (bx * ay - by * ax):
            # If statement compares regular division with integer division to make sure solution is an integer
            # If it's an integer, store it in solution_a
            solution_a = (bx * py - by * px) // (bx * ay - by * ax)
            if (py - solution_a * ay) / by == (py - solution_a * ay) // by:
                # We also want solution_b to be an integer
                solution_b = (py - solution_a * ay) // by
        if solution_a is not None and solution_b is not None:
            # If both solutions are integers, return the cost
            return solution_a * 3 + solution_b
        else:
            return 0

    filename = sys.argv[1]
    machines = [] # array of 3 tuples, first two is claw, last is prize coord

    with open(filename,'r') as f:
        content = f.read().split("\n\n")
        for group in content:
            a, b, prize = group.split("\n")
            
            left_a, right_a = a.split(", ")
            x_a = left_a.split("+")[-1]
            y_a = right_a.split("+")[-1]
            
            left_b, right_b = b.split(", ")
            x_b = left_b.split("+")[-1]
            y_b = right_b.split("+")[-1]
            
            left_prize, right_prize = prize.split(", ")
            x_prize = left_prize.split("=")[-1]
            y_prize = right_prize.split("=")[-1]
                            
            machines.append([(int(x_a),int(y_a)), (int(x_b),int(y_b)), (int(x_prize), int(y_prize))])

    total_cost_1 = 0
    total_cost_2 = 0

    for this_claw in machines:
        total_cost_1 += find_solution(this_claw)
        total_cost_2 += find_solution(this_claw, 10000000000000)
    
    print(total_cost_1)
    print(total_cost_2)


main()         
sol()
                
        