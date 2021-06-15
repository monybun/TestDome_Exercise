#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A large package can hold 5 items, while the small package can hold only 1 item. 
The available number of both large and small packages is limited. 
All items must be placed in packages and used packages have to be filled up completely.
Write a function that calculates the minimum number of packages needed to hold a given number of items. 
If it's not possible to meet the requirements, return -1.

For example, if we have 16 items, 2 large and 10 small packages, 
the function should return 8 (2 large packages + 6 small packages).
"""
def minimal_number_of_packages(items, available_large_packages, available_small_packages):
    min_load = 0; large = 0; small = 0
    
    if (5*available_large_packages+available_small_packages) >= items:
        
        if items != 0:
            
            if items % 5 == 0:
                if items/5 <= available_large_packages:
                    large = items/5
                    small = 0
                    min_load = large + small
                elif items/5 > available_large_packages and (items- 5*available_large_packages) <= available_small_packages: # available_large_packages not enough 
                    small = items - 5*available_large_packages
                    large = available_large_packages
                    min_load = large + small
                else: min_load = -1
            
            else: #items % 5 != 0
                if items > 5 and (items-5*available_large_packages) <= available_small_packages:
                    large = available_large_packages
                    small = items - 5*large
                    min_load = large + small
                elif items > 5 and (items-5*available_large_packages) > available_small_packages:
                    min_load = -1
                elif items ==5:
                    large = 1
                    small = 0
                    min_load = large + small
                elif items < 5:
                    large = 0
                    small = items
                    min_load = large + small
                    
        else:    #items == 0
            min_load = 0
    
    else:
        min_load = -1

    return min_load
    
print(minimal_number_of_packages(16, 2, 10))
