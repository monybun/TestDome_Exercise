#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CrImplement the CargoShip class so that:

1) 'load' adds all items from new_cargo to the cargo. 
new_cargo and cargo are lists of tuples 
where the first element in the tuple is a port name and the second element is the item weight.

2) 'unload' removes items from cargo that are in the same port and returns them as a list of tuples. 
If there are no items for that port, then an empty list should be returned.

3) can_depart returns True if the sum of all weights in cargo is less than or equal to the capacity, and False if not.

For example, if a new CargoShip is created with capacity 10 
and load is called with [("New York", 1), ("London", 20)], then calling unload("New York") 
should return [("New York", 1)],
cargo should have the value of [("London", 20)] and calling can_depart should return False.
"""

class CargoShip:
    
    def __init__(self, capacity):
        self.cargo = []
        self.capacity = capacity
        
    def unload(self, port):
        unload_tuples = []

        for i in self.cargo:
            if port == i[0]:
                unload_tuples.append(i)
                self.cargo.remove(i)
            else: 
                pass

        return unload_tuples
    
    def can_depart(self):
        current_load = []
        for x in self.cargo:
            current_load.append(x[1])
        total_current = sum(current_load)
        
        if total_current <= self.capacity:
            return True
        else:
            return False
    
    def load(self, new_cargo):
        
        for j in new_cargo:
            self.cargo.append(j)
            
        return self.cargo
    
if __name__ == "__main__":
    ship = CargoShip(10)
    ship.load([("New York", 1), ("London", 20)])
    print(ship.unload("New York")) #should print [("New York", 1)]
    print(ship.cargo) #should print [("London", 20)]
    print(ship.can_depart()) #should print False
