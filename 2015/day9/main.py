text_input = '''A to B = 1
A to C = 2
A to D = 3
A to E = 5
B to C = 6
B to D = 8
B to E = 9
C to D = 10
C to E = 11
D to E = 12
'''

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
    cities = toGraph(input)
    cities_num = len(cities.keys())
    visited = set()
    result = float('inf') 

    def closestUnvisited(distances):
        city_distance = float('inf')
        city_name = ''
        for city,distance in distances.items():
            if distance < city_distance and city not in visited:
                city_distance = distance
                city_name = city

        return city_distance, city_name
            
 
    # nearest neighbor heauristic algo
    # no returns to origin
    for city in cities.keys():
        print("=====STARTING=====")
        visited.add(city)
        distance = 0

        print(city, distance)
        while len(visited) != cities_num:
            city_dict = cities[city]
            if len(visited) > 1: 
                city_dict = cities[next_city]
                
            next_distance, next_city = closestUnvisited(city_dict)
            visited.add(next_city)
            distance += next_distance
        
            print(next_city, distance)

        print(result)

        result = min(result, distance)
        visited = set()

    print(result)


# cannot do the same but reverse like part 1 (check the first comment here: https://www.reddit.com/r/adventofcode/comments/kdny5h/2015_day_9_part_2_need_some_help/)
# greedy can guarantee largest path at each single iteration but not largest path overall
def longestPathBrute(input):
    cities = toGraph(input)
    cities_num = len(cities.keys())
    output = []

    def visitCities(next_dict, current_distance, visited):
        if len(visited) == cities_num:
            output.append(current_distance)
            return current_distance
        else:
            for city, distance in next_dict.items():
                if city not in visited:
                    local_visited = visited + [city]
                    visitCities(cities[city], current_distance+ next_dict[city], local_visited)

    for city, city_dict in cities.items():
        visitCities(city_dict, 0, [city])
    print(max(output))

longestPathBrute(input)