#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement the find_all_hobbyists function that takes a hobby, 
and an object consisting of peoples names mapped to their respective hobbies. 
The function should return a List containing the names of the people (in any order) that enjoy the hobby.

For example, the following code should display the name 'Chad'.
hobbies = { 
    "Steve": ['Fashion', 'Piano', 'Reading'],
    "Patty": ['Drama', 'Magic', 'Pets'],
    "Chad": ['Puzzles', 'Pets', 'Yoga']
}

print(find_all_hobbyists('Yoga', hobbies));
"""
def find_all_hobbyists(hobby, hobbies):

    names_list = [key  for (key, value) in hobbies.items() if hobby in value]
   
    return names_list

if __name__ == "__main__":
    hobbies = { 
        "Steve": ['Fashion', 'Piano', 'Reading'],
        "Patty": ['Drama', 'Magic', 'Pets'],
        "Chad": ['Puzzles', 'Pets', 'Yoga']
    }
    
    print(find_all_hobbyists('Yoga', hobbies));
