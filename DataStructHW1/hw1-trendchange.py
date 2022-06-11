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

def trendChange():
    newList = read()
    newListLen = 0
    currentTrend= ""
    newTrend = ""

    ## Print intial output
    print("Trend change points:", end = " ")
    
    ## get length of list since we can't use len()
    for i in newList:
        newListLen +=1

    ## intial trend values
    if (newList[0] - newList[1]) < 0:
            currentTrend = "inc"
    if (newList[0] - newList[1]) > 0:
            currentTrend = "dec"
    if (newList[0] - newList[1]) == 0:
            currentTrend = newTrend
        
    count = 0
    while count < (newListLen - 1):
        if (newList[count] - newList[count + 1]) < 0:
            newTrend = "inc"
        if (newList[count] - newList[count + 1]) > 0:
            newTrend = "dec"
        if (newList[count] - newList[count + 1]) == 0:
            currentTrend = newTrend
        if currentTrend != newTrend:
            print(newList[count], newList[count + 1], end = " ")

        currentTrend = newTrend
        count +=1


    

def main():
    trendChange()


if __name__ == "__main__":
    main()