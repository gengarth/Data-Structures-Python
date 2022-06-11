##Homework 2
##Charles Denney
##U9676-2161
##Jashen Sambon
##U2010-8775
##Group 15

#added parameter "fileName"
def read(fileName):
    #This is the read() from the first homework
    file = open(fileName, "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values

# added paranmeter "fileName"
# Changed function name to put it in this file
def readLine(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    linesNew = [int(x) for x in lines]
    return linesNew

def linearSearch(list, item):
    count = 0
    for num in list:
        count +=1
        if num == item:
            return count
    return count  
    

def binarySearch(list, item):
    low = 0
    high = len(list)
    mid = int((low + high) / 2)
    count = 0
    while True:
        count += 1
        if list[mid] == item:
            return count
        elif mid == low or mid == high:
            return count
        elif list[mid] > item:
            high = mid
            mid = int((low + high) / 2)
        elif list[mid] < item:
            low = mid
            mid = int((low + high) / 2)
        



def main():
    #Read long lists
    linearList = readLine("sortedLinearInput.txt")
    binaryList = readLine("sortedBinaryInput.txt")
    
    #Read short list keys
    linearKey = read("keyLinear.txt")
    binaryKey = read("keyBinary.txt")

    linearFoundTotal = 0
    for item in linearKey:
       linearFound = linearSearch(linearList, item)
       print("Linear search steps for: ",item)
       print(linearFound)
       linearFoundTotal += linearFound
    linearFoundAverage = linearFoundTotal / len(linearKey)

    binaryFoundTotal = 0
    for item in binaryKey:
        binaryFound = binarySearch(binaryList, item)
        print("Binary search steps for: ",item)
        print(binaryFound)
        binaryFoundTotal += binaryFound
    binaryFoundAverage = binaryFoundTotal / len(binaryKey)

    print("Linear Average Steps: ", linearFoundAverage)
    print("Binary Average Steps: ", binaryFoundAverage)

  


if __name__ == "__main__":
    main()