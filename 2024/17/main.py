def main(filename):
    operand_dict = {0: 0, 1:1, 2:2, 3:3, 4:'A', 5:'B', 6:'C', 7:7}
    opcode_dict = {0: 'adv', 1:'bxl', 2:'bst', 3:'jnz', 4:'bxc', 5:'out', 6:'bdv', 7:'cdv'}
    registers = {7:7}
    programs = []
    
    with open(filename, 'r') as f:
        registers_txt, programs_txt = f.read().strip().split("\n\n")
        for line in registers_txt.split("\n"):
            content = line.split(' ')
            registers[content[1][0]] = int(content[-1])
        programs = programs_txt.split(" ")[-1].split(',')
        programs = [int(num) for num in programs]
    
    i = 0
    output = []
    while i < len(programs):
        opcode, literal = opcode_dict[programs[i]], int(programs[i+1])
        combo = operand_dict[literal] if literal <=3 else registers[operand_dict[literal]]

        match opcode:
            # performs division. The numerator is the value in the A register. 
            # The denominator is found by raising 2 to the power of the instruction's combo operand. 
            # (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) 
            # The result of the division operation is truncated to an integer and then written to the A register.
            case 'adv':
                result = registers['A'] // 2**combo
                registers['A'] = result
            # bdv works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
            case 'bdv':
                result = registers['A'] // 2**combo
                registers['B'] = result                
            # cdv works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
            case 'cdv':
                result = registers['A'] // 2**combo
                registers['C'] = result                
            # calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
            case 'bxl':
                result = registers['B']^literal
                registers['B'] = result
            # bst calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
            case 'bst':
                result = combo%8
                registers['B'] = result                                
            # jnz does nothing if the A register is 0. 
            # However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; 
            # if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
            case 'jnz':
                if registers['A'] != 0:
                    i = literal-2
            # bxc calculates the bitwise XOR of register B and register C, then stores the result in register B. 
            # (For legacy reasons, this instruction reads an operand but ignores it.)
            case 'bxc':
                result = registers['B']^registers['C']
                registers['B'] = result
            # out calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
            case 'out':
                output.append(combo%8)
            case _:
                print("EXCEPTION")
        
        i+=2
    
    print(','.join(str(x) for x in output))
    
main('test.txt')