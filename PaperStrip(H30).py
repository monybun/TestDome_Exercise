#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
You are given two paper strips. On each strip, numbers (1, 2, ... N) are written in random order. 
Cut the original paper strip into several pieces and rearrange those pieces to form the desired sequence.

Write a function that, efficiently with respect to time used, 
returns the minimum number of cut pieces needed to perform the described operation.

For example, the following code should display 3 because the pieces used should be (1), (4, 3), and (2):
    original = [1, 4, 3, 2]
    desired = [1, 2, 4, 3]
    print(min_pieces(original, desired))
"""
def min_pieces(original, desired):
    sub = []; count = 0
    for i in range(len(desired)):
        #sub[desired[i]] = i
        sub.append(i)
    
    for i in range(len(original)):
        original[i] = sub[original[i]]
        
    for j in range(1,len(original)):
        if original[j-1]+1 != original[j]:
            count += 1
    return count + 1

original = [1, 4, 3, 2]
desired = [1, 2, 4, 3]
print(min_pieces(original, desired))

'''
# Function for finding maximum pieces 
# with n cuts. 
def findMaximumPieces(n): 
  
    # to maximize number of pieces 
    # x is the horizontal cuts 
    x = n // 2
   
    # Now (x) is the horizontal cuts 
    # and (n-x) is vertical cuts, then 
    # maximum number of pieces = (x+1)*(n-x+1) 
    return ((x + 1) * (n - x + 1)) 
   
# Driver code 
if __name__ == "__main__": 
   
    #Taking the maximum number of cuts allowed as 3 
    n = 3
   
    # Finding and printing the max number of pieces 
    print("Max number of pieces for n = " +str( n) 
         +" is " + str(findMaximumPieces(3))) 
'''