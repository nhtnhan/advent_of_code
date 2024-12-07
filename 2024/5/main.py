def one(rules, orders):
    pre_to_posts = {}
    for rule in rules.split('\n'):
        pre, post = rule.split('|')
        pre, post = int(pre), int(post)
        if pre not in pre_to_posts:
            pre_to_posts[pre] = [post]
        else:
            pre_to_posts[pre].append(post)
        
        if post not in pre_to_posts:
            pre_to_posts[post] = []

    
    total = 0
    
    print(pre_to_posts)
    for line in orders.split('\n'):
        order = line.split(',')
        eligible = True
        
        for i in range(len(order)-1):
            num_i = int(order[i])

            for j in range(i+1, len(order)):
                num_j = int(order[j])

                if num_j not in pre_to_posts[num_i]:
                    eligible = False
                    break
            
            if not eligible:
                break

        if eligible:
            print(order, len(order)//2, order[len(order)//2])
            total += int(order[len(order)//2])

                
    
    print(total)

def two(rules, orders):
    from functools import cmp_to_key

    pre_to_posts = {}
    for rule in rules.split('\n'):
        pre, post = rule.split('|')
        pre, post = int(pre), int(post)
        if pre not in pre_to_posts:
            pre_to_posts[pre] = [post]
        else:
            pre_to_posts[pre].append(post)
        
        if post not in pre_to_posts:
            pre_to_posts[post] = []

    # create one full order
    total = 0
    for line in orders.split('\n'):
        order = line.split(',')
        line_int = []
        eligible = True

        for i in range(len(order)-1):
            num_i = int(order[i])
            line_int.append(num_i)

            for j in range(i+1, len(order)):
                num_j = int(order[j])

                if num_j not in pre_to_posts[num_i]:
                    eligible = False

        line_int.append(int(order[len(order)-1]))

        if not eligible:            
            # print("before: ", line_int)
            line_int.sort(key=cmp_to_key(lambda i1, i2: -1 if i2 not in pre_to_posts[i1] else 1 if i1 in pre_to_posts[i2] else 0))

            print("after: ", line_int)
            total += int(line_int[len(line_int)//2])
        
    print(total)


two(input_a, input_b)