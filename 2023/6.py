input1= {
    7:9,
    15:40,
    30:200
}
input= {
    61:430,
    67:1036,
    75:1307,
    71:1150
}

two1={
    71530:940200
}

two={
    61677571:430103613071150
}

def one(dict):
    ways = 1
    for time, dist in dict.items():
        beat = 0
        for hold in range(1,time):
            if (time-hold)*hold > dist:
                beat+=1
        if beat!=0:
            ways*=beat
    print(ways)

one(two)