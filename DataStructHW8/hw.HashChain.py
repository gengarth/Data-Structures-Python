"""
Homework 8
Charles Denney
U9676-2161
"""

import hashlib
import math

class Node(object):
   def __init__(self, data, next = None):
       self.data = data
       self.next = next

#Takes seed and length, returns the data contents of each node
def H(k,L):
   kb=str.encode(k)
   value=hashlib.sha256(kb).hexdigest()
   size=math.ceil(len(value)/L)
   return [value[i:i+size] for i in range(0,len(value),size)]

#Creates a new hash chain
def createHashChain(seed,L):
   values=H(seed,L)
   head=Node(values[0])
   temp=head
   for i in range(1,L):
       temp.next=Node(values[i])
       temp=temp.next
   printHashChain(head)

#Prints the hash chain
def printHashChain(head):
   temp=head
   while temp:
       if temp.next !=None:
           print(temp.data," | ",end="")
       else:
           print(temp.data)
       temp=temp.next

def main():
    seed = input("Enter seed: ")
    L = int(input("Enter length: "))
    createHashChain(seed, L)

if __name__=="__main__":
   main()