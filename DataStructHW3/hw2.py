##Homework 3.2
##Charles Denney
##U9676-2161

def readm1():
    file = open("hw2-m1.txt", "r")
    lines = file.readlines()
    a=[]
    for line in lines:
        b=[]
        for x in line.strip('\n').split(' '):
            b.append(int(x))
        a.append(b)                
    return a

def readm2():
    file = open("hw2-m2.txt", "r")
    lines = file.readlines()
    a=[]
    for line in lines:
        b=[]
        for x in line.strip('\n').split(' '):
            b.append(int(x))
        a.append(b)                
    return a

def main():
    matrixOne = readm1()
    matrixTwo = readm2()

    if len(matrixOne) != len(matrixTwo) or len(matrixOne[0]) != len(matrixTwo[0]):
        raise Exception("Matrix dimensions do not match")

    matrixSum = readm1()
    x = 0
    y = 0
    for row in matrixOne:
        for col in row:
            matrixSum[x][y] = (matrixOne[x][y] + matrixTwo[x][y])
            y += 1
        y = 0
        x += 1

    y = 0
    x = 0
    # print(matrixOne)
    # print(matrixTwo)
    print("The result is:")
    for row in matrixSum:
        for col in row:
            print(matrixSum[x][y], end = " ")
            y += 1
        print()
        y = 0
        x +=1

if __name__ == "__main__":
    main()