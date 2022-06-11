##Charles Denney
##U9676-2161
##Jashen Sambon
##U2010-8775
##Group 15

def read():
    ##Added "Test" to match correct filename
    file = open("TestInputHW1.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values

def maxMin():
    newList = read()
    max = newList[0]
    min = newList[0]
    for i in newList:
        if i < min:
            min = i
        if i > max:
            max = i

    print("Maximum element: ", max)
    print("Minimum element: ", min)


def main():
    maxMin()

if __name__ == "__main__":
    main()