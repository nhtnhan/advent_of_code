def one(input):
    output = 0    

    first = ''
    second = ''    
    current = ''

    for l in input:
        if current == '' and l == 'm':
            current+=l
        elif current == 'm' and l == 'u':
            current+=l
        elif current == 'mu' and l == 'l':
            current+=l
        elif current == 'mul' and l == '(':
            current+=l
        elif current == 'mul(' and l.isdigit():
            first+=l
        elif current == 'mul(' and first.isdigit() and l == ',':
            current+=l
        elif current == 'mul(,' and first.isdigit() and l.isdigit():
            second+=l
        elif current == 'mul(,' and first.isdigit() and second.isdigit() and l == ')':
            print("hereee:", first, second)
            output += int(first) * int(second)
            
            current = ''
            first = ''
            second = ''
        else:
            current = ''
            first = ''
            second = ''    

    return(output)

def two(input):
    output = 0
    
    parts = input.split("don't()")
    
    output+=one(parts[0])
    
    for i in range(1, len(parts)):
        # print(parts[i])
        enabled_part = parts[i].split("do()")        

        if len(enabled_part) > 1:
            for j in range(1, len(enabled_part)):
                output+=one(enabled_part[j])

        # print("===============================")
    
    print(output)

two(input)