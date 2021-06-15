#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
An insurance company has decided to change the format of its policy numbers from 
XXX-YY-ZZZZ to XXX/ZZZZ/YY (where X, Y and Z each represent the digits 0-9). 
Write a method that re-formats all policy numbers in a well-formatted paragraph ('-' may appear elsewhere in the text).

For example, change_format("Please quote your policy number: 112-39-8552.") 
should return "Please quote your policy number: 112/8552/39.".
"""
#phonenumber= "(516)111-2222"
#regex= "\(\w{3}\)\w{3}-\w{4}"
#112-39-8552
#regex = r"\d{3}-\d{2}-\d{4}"
#regexing: https://dev.to/samcodesign/phone-number-email-extractor-with-python-12g2
'''
line = re.sub(r"""
  (?x) # Use free-spacing mode.
  <    # Match a literal '<'
  /?   # Optionally match a '/'
  \[   # Match a literal '['
  \d+  # Match one or more digits
  >    # Match a literal '>'
  """, "", line)
'''
#joining the strings to be replaced with | to a regex and delimiting it with \b word boundary characters, 
#e.g. \b(a|b|c)\b in your case, and use a dictionary to look up the proper replacements.
  
import re 

def change_format(paragraph):
    original_format = re.findall("\d{3}-\d{2}-\d{4}", paragraph)
    repalce_lst = []
    for j in original_format:
        number = re.findall(r'\d+', j)
        regex_digits = '/'.join([number[0],number[2],number[1]])
        repalce_lst.append(regex_digits)
        
    d = dict(zip(original_format, repalce_lst))
    p = r'\b(' + '|'.join(original_format) + r')\b'
    reformed = re.sub(p, lambda m: d.get(m.group()), paragraph)
    
    return reformed

print(change_format('Please quote your policy number: 112-39-8552 116-60-7623.'))
