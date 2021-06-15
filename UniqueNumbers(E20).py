#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a method that finds, efficiently with respect to time used, all numbers that occur exactly once in the input list.

For example, for a list of numbers containing [1, 2, 1, 3], 
find_unique_numbers(numbers) should return a list containing [2, 3].
"""
from collections import Counter
def find_unique_numbers(numbers):
    unique_list = []
    counter_dict = Counter(numbers)
    for x in counter_dict.keys():
        if counter_dict[x] == 1:
            unique_list.append(x)
    return unique_list

if __name__ == "__main__":
    print(find_unique_numbers([1, 2, 1, 3]))
