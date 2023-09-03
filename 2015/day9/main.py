input = '''Faerun to Norrath = 129
Faerun to Tristram = 58
Faerun to AlphaCentauri = 13
Faerun to Arbre = 24
Faerun to Snowdin = 60
Faerun to Tambi = 71
Faerun to Straylight = 67
Norrath to Tristram = 142
Norrath to AlphaCentauri = 15
Norrath to Arbre = 135
Norrath to Snowdin = 75
Norrath to Tambi = 82
Norrath to Straylight = 54
Tristram to AlphaCentauri = 118
Tristram to Arbre = 122
Tristram to Snowdin = 103
Tristram to Tambi = 49
Tristram to Straylight = 97
AlphaCentauri to Arbre = 116
AlphaCentauri to Snowdin = 12
AlphaCentauri to Tambi = 18
AlphaCentauri to Straylight = 91
Arbre to Snowdin = 129
Arbre to Tambi = 53
Arbre to Straylight = 40
Snowdin to Tambi = 15
Snowdin to Straylight = 99
Tambi to Straylight = 70
'''

# parse input to graph for tsp problem
def toGraph(input):
    graph = {}
    for line in input.strip().split('\n'):
        locations, distance = line.split(' = ')   
        origin, destination = locations.split(' to ')
        if origin not in graph:
            graph[origin] = {destination: int(distance)}
        else:
            graph[origin][destination] = int(distance)
        if destination not in graph:
            graph[destination] = {origin: int(distance)}
        else:
            graph[destination][origin] = int(distance)
    return graph

def shortestPath(input):
    distances = parseInput(input)
    graph = toGraph(input)
    
    for key, value in graph.items():
        print(key, value)

shortestPath(input)