#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement the function count, which returns the number of lines from the StringIO that contains text matching the string.

For example, when the string needle is "there" and the StringIO haystack contains:
Hello, there!
How are you today?
Yes, you over there.

The count function should return 2 ("Hello, there!" and "Yes, you over there.").
"""
import io

def count(needle, haystack):

    sentances = haystack.getvalue()
    count = 0
    for i in sentances.split('\n'):
        if needle in i:
            count += 1
    return count
    

if __name__ == "__main__":
    stream = io.StringIO("Hello, there!\nHow are you today?\nYes, you over there.")
    print(count('there', stream))
    stream.close()
