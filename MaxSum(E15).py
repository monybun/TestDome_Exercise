#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement the find_max_sum method that, efficiently with respect to time used, 
returns the largest sum of any two elements in the given list of positive numbers.

For example, the largest sum of the list [5, 9, 7, 11] is the sum of the elements 9 and 11, which is 20.
"""
def find_max_sum(numbers):
    max_1 = max(numbers)
    if len(numbers):
         numbers.remove(max_1)
         max_2 = max(numbers)
         max_sum = max_1 + max_2
    else: max_sum = numbers[0]
    return max_sum
    
if __name__ == "__main__":
    print(find_max_sum([5, 9, 7, 11]))
