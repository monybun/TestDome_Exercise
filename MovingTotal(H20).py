#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design a data structure that can, efficiently with respect to time used, 
store and check if the total of any three successively added elements is equal to a given total.

For example, MovingTotal() creates an empty container with no existing totals. 
append([1, 2, 3, 4]) appends elements [1, 2, 3, 4], which means that there are two existing totals (1 + 2 + 3 = 6 and 2 + 3 + 4 = 9). 
append([5]) appends element 5 and creates an additional total from [3, 4, 5]. 
There would now be three totals (1 + 2 + 3 = 6, 2 + 3 + 4 = 9, and 3 + 4 + 5 = 12). 
At this point contains(6), contains(9), and contains(12) should return True, while contains(7) should return False.
"""
class MovingTotal:
    lst = []
    def append(self, numbers):
        self.numbers = numbers
        self.lst += self.numbers

    def contains(self, total):
        sublist, rolling_sum_list = [], []
        for j in range(0, len(self.lst)-2,1):
            sublist = self.lst[j:j+3]
            rolling_sum = sum(sublist)
            rolling_sum_list.append(rolling_sum)
           # print(rolling_sum_list)
           
        if total in rolling_sum_list:
            return True
        else:
            return False
            
    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    
    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
    
    movingtotal.append([5,6])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(15))
