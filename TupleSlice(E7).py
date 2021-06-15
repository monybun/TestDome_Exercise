#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write the function to slice the tuple between the given start (inclusive) and end (exclusive) indexes, 
and join the resulting range of values as a comma delimited string.

For example, tuple_slice(1, 4, (76, 34, 13, 64, 12)) should return "34,13,64".
"""
#Use itertools.chain_fromiterable() to flatten your nested tuples first, then map() to string and join(). 
from itertools import chain

def tuple_slice(startIndex, endIndex, tup):
    string_output = ''
    s = tup[startIndex : endIndex]
    string_output = ','.join(map(str,chain(s)))
    
    return string_output

if __name__ == "__main__":
    print(tuple_slice(1, 4, (76, 34, 13, 64, 12)))
