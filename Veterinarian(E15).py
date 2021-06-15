#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement a class Veterinarian that will be used as a part of a larger simulation of a veterinarian office.
The class Veterinarian needs to be efficient with respect to time used and contain the following methods:

accept(petName) - puts the specified pet at the end of the line.
heal() - removes the pet's name from the queue and returns it. 
If no pets are in the queue, an IndexError exception should be raised.

For example, the following code snippet should write "Barkley", "Mittens":
veterinarian = Veterinarian()
veterinarian.accept("Barkley")
veterinarian.accept("Mittens")
print(veterinarian.heal())
print(veterinarian.heal())
"""
#creating a weak reference for an object is that you can include a callback when the object is deleted.

'''
class Veterinarian:
    pets = []
    healed = []
    def accept(self, petName):
        self.pets.append(petName)
        deque().extendleft(self.pets)

    def heal(self):
        try:
            for i in self.pets:
                self.healed.append(i)
            #self.healed.append(self.pets[-1])
                self.pets.remove(i)
        except IndexError as er:
            print("Index Error: {0}".format(er))
            raise
        return self.healed
'''
class Veterinarian:
    def __init__(self):
        self.pets = []
        
   # def isEmpty(self):	        
    #    return self.pets == []

    def accept(self, petName):
        self.pets.insert(0,petName)

    def heal(self):
            return self.pets.pop()
    #def size(self):
     #   return len(self.pets)
        
    
if __name__ == "__main__":
    veterinarian = Veterinarian()
    veterinarian.accept("Barkley")
    veterinarian.accept("Mittens")
    print(veterinarian.heal())
    print(veterinarian.heal())
