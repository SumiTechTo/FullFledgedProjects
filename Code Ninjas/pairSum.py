from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, s):
    # Write your code here.
    for i in N:
        for j in i+1:
            if arr[i]+arr[j]==s:
                print(i,j)
            
    
    
    
ARR=[]
N=int(input("Enter the size of array"))
S=int(input("Enter an integer"))
print(N,S)
for i in N:
    a=int(input("Enter a number"))
    ARR.append(a)
pairSum(ARR,S)