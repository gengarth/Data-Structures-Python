def read():
    file = open("HanoiTower.txt", "r")
    lines = file.readlines()
    linesNew = [int(x) for x in lines]
    return linesNew