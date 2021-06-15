#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement the symbolic_to_octal function so that it converts a permission's symbolic notation into its octal notation.

The string consists of 3 blocks of 3 characters each. The returned number will have three digits, one for each block. 
Each digit is the sum of all permissions present in the block:
    CHARACTER                     VALUE                                          BLOCK                     VALUE
            r                                     4                                                  rwx                     4+2+1=7
           w                                    2                                                  r-x                      4+0+1=5
           x                                    1                                                  -w-                      0+2+0=2
           -                                    0
So the returned number would be 752.
"""
from numpy import cumsum

def symbolic_to_octal(perm_string):

    string_list = [char for char in str(perm_string)]
    list = []
    for i in string_list:
        if i == 'r': 
            i = 4
            list.append(i)
        elif i == 'w':
            i =2
            list.append(i)
        elif i == 'x':
            i=1
            list.append(i)
        elif i == '-':
            i =0
            list.append(i)
        else: pass
    
    sublist = []
    sum_of_3 = ''
    sum3_list = []
    final_num = ''
    for x in range(0,len(list),3):
        sublist = list[x:x+3]
        sum_of_3 = cumsum(sublist)[-1]
        sum3_list.append(sum_of_3)
    final_num = 100*sum3_list[0]+10*sum3_list[1]+sum3_list[-1]
    return final_num

        
print(symbolic_to_octal('rwxr-x-w-'))
