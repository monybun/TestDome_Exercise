#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A hospital patient tracking system is restructuring its patient records. The current format is fragmented, 
each patient is represented as a list of namedtuple. 
Each element contains a different piece of information about the patient.

Your task is to write a function that merges all of the information into one namedtuple, 
named Patient, in the order that it's provided to the function.
For example:
    PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
    personal_details = PersonalDetails(date_of_birth = '06-04-1972')
                                       
    Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
    complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')

    print(merge(personal_details, complexion))
    
Should display: Patient(date_of_birth='06-04-1972', eye_color='Blue', hair_color='Black')
"""
from functools import reduce
from itertools import chain
from operator import add
from collections import namedtuple

def merge(*records):
    #cls = namedtuple('_'.join(arg.__class__.__name__ for arg in records), reduce(add, (arg._fields for arg in records)))
    cls = namedtuple('Patient', reduce(add, (arg._fields for arg in records)))
    return cls(*chain(*records))
    
PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
personal_details = PersonalDetails(date_of_birth = '06-04-1972')
                                   
Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')
  
print(merge(personal_details, complexion))

'''
>>> from collections import namedtuple
>>> A = namedtuple("A", "a b c")
>>> B = namedtuple("B", "d e")
>>> a = A(10, 20, 30)
>>> b = B(40, 50)
>>> C = namedtuple("C", A._fields + B._fields)
>>> C(*(a + b))
C(a=10, b=20, c=30, d=40, e=50)
>>> #Available in Python 3.5+
>>> C(*a, *b)
C(a=10, b=20, c=30, d=40, e=50)
'''