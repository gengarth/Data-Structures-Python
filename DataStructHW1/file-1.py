# The following "read" function reads values from a file named "inputHW1.txt" and returns the values in an array.
def read():
    file = open("inputHW1.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values
