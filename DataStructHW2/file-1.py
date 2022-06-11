# Used to read a file line by line
def read():
    file = open("sortedLinearInput.txt", "r")
    lines = file.readlines()
    linesNew = [int(x) for x in lines]
    return linesNew
