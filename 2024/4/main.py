def main(input):
    WORD = "XMAS"
    BACKWARD = "SAMX"
    lines = input.split('\n')
    row_count = len(lines)
    col_count = len(lines[0])
    count = 0    
    for i in range(row_count):
        for j in range(col_count):
            if lines[i][j] == 'X':
                # check horizontally forward:
                if j + len(WORD)-1 < col_count and lines[i][j:j+len(WORD)] == WORD:
                    print(i, j)
                    count+=1

                # check horizontally backward:
                if j - (len(WORD)-1) >= 0 and lines[i][j-(len(WORD)-1):j+1] == BACKWARD:
                    print(i, j)
                    count+=1
                    
                # check vertically downward:
                if i + len(WORD)-1 < row_count:
                    word = ""
                    for k in range(len(WORD)):
                        word += lines[i+k][j]
                    if word == WORD:
                        print(i, j)
                        count+=1
                
                # check vertically upward:
                if i - (len(WORD)-1) >= 0:
                    word = ""
                    for k in range(len(WORD)):
                        word += lines[i-k][j]
                    if word == WORD:
                        print(i, j)
                        count+=1
                
                # check diagonally downward left:
                if i + len(WORD)-1 < row_count and j - (len(WORD)-1) >= 0:
                    word = ""
                    for k in range(len(WORD)):
                        word += lines[i+k][j-k]
                    if word == WORD:
                        print(i, j)
                        count+=1
                
                # check diagonally downward right:
                if i + len(WORD)-1 < row_count and j + len(WORD)-1 < col_count:
                    word = ""
                    for k in range(len(WORD)):
                        word += lines[i+k][j+k]
                    if word == WORD:
                        print(i, j)
                        count+=1
                
                # check diagonally upward left:
                if i - (len(WORD)-1) >= 0 and j - (len(WORD)-1) >= 0:
                    word = ""
                    for k in range(len(WORD)):
                        word += lines[i-k][j-k]
                    if word == WORD:
                        print(i, j)
                        count+=1
                
                # check diagonally upward right:
                if i - (len(WORD)-1) >= 0 and j + len(WORD)-1 < col_count:
                    word = ""
                    for k in range(len(WORD)):
                        word += lines[i-k][j+k]
                    if word == WORD:
                        print(i, j)
                        count+=1
    
    print(count)

def two(input):
    lines = input.split('\n')
    row_count = len(lines)
    col_count = len(lines[0])
    count = 0    
    for i in range(row_count):
        for j in range(col_count):
            if lines[i][j] == 'A':
                if i + 1 < row_count and i - 1 >= 0 and j + 1 < col_count and j - 1 >= 0:
                    ltr = lines[i-1][j-1]+'A'+lines[i+1][j+1]
                    rtl = lines[i+1][j-1]+'A'+lines[i-1][j+1]
                    
                    if (ltr == "MAS" or ltr == "SAM") and (rtl == "MAS" or rtl == "SAM"):
                        count+=1
    
    print(count)



two(input)
