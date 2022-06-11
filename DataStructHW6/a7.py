"""
File: a7.py

Charles Denney
U9676-2161
Jashen Sambon
U2010-8775
Group 15
"""

from stack import Stack

def isPalindrome(sentence):          
    """Returns True if sentence is a palindrome
    or False otherwise."""
    stk = Stack() # Creates a stack called stk.

    # *** Write your code here ***
    stk2 = Stack()

    #Punctuation list since we can't use functions
    #If there are unforseen punctuation in the test cases, please add here
    notAllowedList = [" ", ".", ",", "?", ":", ";", "'", "\"","/","\\", "!"]

    #Creates stack, pops spaces and punctuation
    for i in sentence:
        stk.push(i)
        for j in notAllowedList:
            if j == stk.peek():
                stk.pop()
   
   #Creates second stack, pops unneeded middle letter
    midStk = stk.size() / 2
    while midStk > 0:
        stk2.push(stk.pop())
        midStk -= 1
    if midStk < 0:
        stk2.pop()

    #Checks if the two stacks are identical
    while not stk.isEmpty():
        palindrome = True
        checkStk = stk.pop()
        checkStk2 = stk2.pop()
        palindrome = checkStk == checkStk2
        if not palindrome:
            return False

    return True

# *** Do not modify main() ***
def main():
    while True:
        sentence = input("Enter some text or just hit Enter to quit: ")
        if sentence == "":
            break
        elif isPalindrome(sentence):
            print("It's a palindrome.")
        else:
            print("It's not a palindrome.")

main()
