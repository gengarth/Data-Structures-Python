'''
    Description:  Sorts myList in ascending order using an selection sort.
    File:  selectionSort.py
'''

import random
import time

def selectionSort(aList):
    for lastUnsortedIndex in range(len(aList)-1, 0, -1):
        # look for maximum item in unsorted part of list
        # Assume maximum is the first item in the unsorted part
        maxIndex = 0

        # scan the unsorted part of the list to correct the assumption
        for testIndex in range(1, lastUnsortedIndex+1):
            if aList[testIndex] > aList[maxIndex]:
                maxIndex = testIndex

        # exchange the items at maxIndex and firstUnsortedIndex
        temp = aList[lastUnsortedIndex]
        aList[lastUnsortedIndex] = aList[maxIndex]
        aList[maxIndex] = temp
        

def shuffle(myList):
    for fromIndex in range(len(myList)):
        toIndex = random.randint(0,len(myList)-1)
        temp = myList[fromIndex]
        myList[fromIndex] = myList[toIndex]
        myList[toIndex] = temp
    

def main():            
    print("selectionSort Timings")            
    aList = list(range(10000,0,-1))
    print( "\nBefore sorting list: ",end="")
    print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
    start = time.time()
    selectionSort(aList)
    end = time.time()
    print( "sorted list:", end="")
    print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
    print( "Time to sort",end - start,"seconds")
    
    print( "\nBefore sorting list: ", end="")
    print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
    start = time.time()
    selectionSort(aList)
    end = time.time()
    print( "sorted list:", end="")
    print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
    print( "Time to sort",end - start,"seconds")
    
    aList = list(range(10000,0,-1))
    shuffle(aList)
    print( "\nBefore sorting (random) list: ",end="")
    print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
    start = time.time()
    selectionSort(aList)
    end = time.time()
    print( "sorted list:",end="")
    print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
    print( "Time to sort",end - start,"seconds")
    
    aList = list(range(10000,0,-1))
    shuffle(aList)
    print( "\nBefore sorting (random) list: ",end='')
    print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
    start = time.time()
    selectionSort(aList)
    end = time.time()
    print( "sorted list:",end="")
    print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
    print( "Time to sort",end - start,"seconds")
    
    input("Hit <Enter>-key to end")

if __name__ == "__main__": main()