#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a method that, efficiently with respect to time used, 
finds the first product in a list that occurs only once in that list. If there are no unique products in the list, 
None should be returned.

For example, first_unique_product(["Apple", "Computer", "Apple", "Bag"]) should return "Computer".
"""
'''
def first_unique_product(products):
    #To preserve the order:
    seen = set()
    setlist = [x for x in products if x not in seen and not seen.add(x)]
    
    return setlist[0]
'''

from collections import Counter
def first_unique_product(products):
    counter_dict = Counter(products)
    unique_list = []
    
    for x in counter_dict.keys():
        if counter_dict[x] == 1:
            unique_list.append(x)
    
    if len(unique_list) != 0:
        return unique_list[0]
    else:
        return None
    
if __name__ == "__main__":
    print(first_unique_product(["Apple", "Computer", "Apple", "Bag"])) #should print "Computer"
