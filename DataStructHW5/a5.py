"""
File: a5.py
Assignment 5

Define a length function.
Define a printStructure function.
Define an insert function.
Test the above functions and the Node class.

Charles Denney
U9676-2161
Jashen Sambon
U2010-8775
Group 15
"""

from node import Node

def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0
    if(probe != None):
        count = length(probe.next)
        count += 1

    return count
    
def insert(newItem, head):
    """Inserts newItem at the correct position (ascending order) in
    the linked structure referred to by head.
    Returns a reference to the new structure."""
    if head == None:
        newNode = Node(newItem)
        head = newNode
    else:
        if(newItem > head.data):
            if(head.next == None):
                head.next = Node(newItem)
            else:
                insert(newItem, head.next)
        else:
            newNode = Node(newItem)
            tempHead = head.next
            head.next = newNode
            newNode.next = tempHead
            tempHead = head.data
            head.data = newNode.data
            newNode.data = tempHead
    return head


def printStructure(head):
    """Prints the items in the structure referred to by head."""
    if(head.next == None):
        print(head.data)
    else:
        print(head.data, end = " ")
    if(head.next != None):
        printStructure(head.next)
    return

def main():
    """Gets words from the user and inserts in the
    structure referred to by head."""
    head = None
    while True:
        userInput = input('Please enter a word (or just hit enter to end): ')
        if userInput == '':
            break
        head = insert(userInput, head)
        
    print('The structure contains', length(head), 'items:')
    printStructure(head)

if __name__ == "__main__": main()
