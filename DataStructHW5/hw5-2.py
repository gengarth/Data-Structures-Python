"""
Charles Denney
U9676-2161
Jashen Sambon
U2010-8775
Group 15
"""

## Can read from file and store contents in unsorted list
## Could not get mergesort function to merge correctly

class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, newNode):
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

def getMid(head, length):
    check = length / 2
    currNode = head.head
    while (check > 0):
        mid = currNode
        currNode = currNode.next
        check -= 1
    return mid

def makeList(fileName):
    file = open(fileName, "r")
    line = file.readline()
    file.close()
    list = LinkedList()
    for i in line.split(' '):
        newNode = Node(int(i))
        list.append(newNode)

    return list

def getLength(head):
    count = 0
    currNode = head.head
    while(currNode!= None):
        currNode = currNode.next
        count += 1
    return count

def mergeSort(head, length):
    currNode = head.head
    if (currNode == None or currNode.next == None):
        return currNode
    else:
        mid = getMid(head, length)

        bigHead = LinkedList()
        bigHead.head = mid.next
        bigHead.tail = head.tail

        mid.next = None

        littleHead = LinkedList()
        littleHead.head = currNode
        littleHead.tail = mid
    
        newLittleHead = mergeSort(littleHead, getLength(littleHead))
        newBigHead = mergeSort(bigHead, getLength(bigHead))

    

def main():
    list = makeList("hw5-2.txt")
    # list = LinkedList()
    # for i in range(1,4):
    #    list.append(Node(i))

    #sortedList = mergeSort(list, getLength(list))
    print(list)

if __name__ == "__main__":
    main()
