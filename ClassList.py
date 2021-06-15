#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class for Python OOP list manipulation
@author: Mony
"""
class List:
    lst = []
    
    def append(self):
        element = input("Enter element to append to the list: ")
        self.lst.append(element)
    
    def delete(self):
        element = input("Enter element to delete from the list: ")
        self.lst.remove(element)
        
    def display(self):
        print("\nList:", self.lst)
        
def main():
    obj = List()
    obj.append()
    obj.append()
    obj.display()
    obj.delete()
    obj.display()
    
if __name__ == "__main__":
    main()