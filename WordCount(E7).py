#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Return True if the substrings 'John' and 'Mary' appear the same number of times in the given string; 
otherwise return False.

String comparison should be case insensitive.
"""
def john_mary(str):
    a = str.lower()
    if a.count("john") == a.count("mary"):
        return True
    else:
        return False

print(john_mary('John&Mary'))
