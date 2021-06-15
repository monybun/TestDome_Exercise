#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script you are writing uses logarithmic functions from the math module.
Implement the add_patch function that should add a log100 function to the math module. 
The log100 function should wrap the existing math.log function so that it calculates a logarithm with a base of 100.

For example, math.log100(10) is equivalent to math.log(10, 100) and should return 0.5.
"""
import math

def add_patch():
    math.log100 = lambda x: math.log(x, 100)
    return

# Example case.
add_patch()      
print(math.log100(10))
