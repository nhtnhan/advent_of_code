def parse_input(filename):
    map = []
    moves = []
    with open(filename) as f:
        map_txt, moves_txt = f.read().split("\n\n")
        map = [list(line) for line in map_txt.split("\n")]
        moves = list(''.join(line for line in moves_txt.split("\n")))
    
    return map, moves

def main(filename):
    map, moves = parse_input(filename)
    
    
main('small.txt')