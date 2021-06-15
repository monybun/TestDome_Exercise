#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
match and check dates formats

@author: Mony
"""
txt='''\
Jan 19, 1990
January 19, 1990
Jan 19,1990
01/19/1990
01/19/90
1990
Jan 1990
January1990'''

import datetime as dt

fmts = ('%Y','%b %d, %Y','%b %d, %Y','%B %d, %Y','%B %d %Y','%m/%d/%Y','%m/%d/%y','%b %Y','%B%Y','%b %d,%Y')

parsed=[]
for e in txt.splitlines():
    for fmt in fmts:
        try:
           t = dt.datetime.strptime(e, fmt)
           parsed.append((e, fmt, t)) 
           break
        except ValueError:
           pass

# check that all the cases are handled        
success={t[0] for t in parsed}
for e in txt.splitlines():
    if e not in success:
        print (e)    

for t in parsed:
    print ('"{:20}" => "{:20}" => {}'.format(*t) )