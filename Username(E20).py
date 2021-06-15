#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement the validate function, which accepts a username and returns true if it's acceptable and false if it's not.

A username is valid if it satisfies the following rules:

The username must be at least 4 characters long.
The username must contain only letters, numbers and optionally one underscore (_).
The username must start with a letter, and must not end with an underscore.
For example, validate("Mike Standish"); would return false because it contains a space.
"""
import re

def validate(username):
    #if re.match(r'^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$',username) is not None:
    #^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$
    #(?=.{8,20}$):  username is 8-20 characters long
    #(?![_.]): no _ or . at the beginning
    #(?!.*[_.]{2}): no __ or _. or ._ or .. inside
    #(?!.*[_.-]{2}): no __ or _. or ._ or .. or -- inside
    #[a-zA-Z0-9._]+:  allowed characters, atleast one must be present
    #(?<![_.]:  no _ or . at the end
    
    if re.match(r'^(?=[a-zA-Z])(?!.*[_.]{2})[a-zA-Z0-9_]+(?<![_])$', username) and len(username)>=4:
        return True
    else:
        return False

print(validate("Mike_Standish")) #Valid username
print(validate("Mike Standish")) #Invalid username
print(validate("Mike$Standish")) #Invalid username
print(validate("Mik__")) #Invalid username

