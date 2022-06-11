##Homework 3.Extra
##Charles Denney
##U9676-2161

def read():
    file = open("hw3-ExtraCredit.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values

def checkDupes(newList):
    dupeList = []
    listLength = len(newList)
    for i in range(0, listLength):
        for k in range(i+1, listLength):
            if(newList[i] == newList[k]):
                dupeList.append(newList[k])
    return dupeList



def main():
    newList = read()
    print(newList)
    print("The duplicate Number:", end = " ")
    print(checkDupes(newList))

if __name__ == "__main__":
    main()