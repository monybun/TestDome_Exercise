#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert a string of numbers to a sentence. 
Each number represents a letter. 
Numbers in the string are separated by a space and words in the sentence are separated by a plus character.

Conversion table:

1 = A
2 = B
...
26 = Z

Example: numbers_to_letters('20 5 19 20+4 15 13 5') should return 'TEST DOME'.
"""
#chr(ord('@')+number): Capital letters (1-26: A-Z)
#chr(ord('`')+number): lower case (1-26:a-z)
'''
for x, y in zip(range(1, 27), string.ascii_lowercase):
    print(x, y)
'''
#or
'''
for x, y in ((x + 1, chr(ord('a') + x)) for x in range(26)):
    print(x, y)
'''

import string
import re

def numbers_to_letters(s):
    
    list_num = [str(c) for c in range(1,27)]
    di = dict(zip(list_num, string.ascii_uppercase))
    di['+'] = ' '
    find = re.findall('[+-/*//()]+|\d+',s)
    
    output_list = []
    
    for i in find:
        for num,value in di.items():
            if num == i:
                output_list.append(value)
                
    return ''.join(output_list)

if __name__ == "__main__":
    print(numbers_to_letters('20 5 19 20+4 15 13 5'))

