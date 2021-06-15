#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A tree is an abstract data structure consisting of nodes. Each node has only one parent node 
and zero or more child nodes. Each tree has one special node, called a root, which has no parent node. 
A node is called an internal node if it has one or more children. 

A tree can be represented by a list P where P[i] is the parent of node i. For the root node r, P[r] equals -1.

Write a function that, efficiently with respect to time used, counts the number of internal nodes in a given tree.
For example, 
the tree represented by the list [1, 3, 1, -1, 3] has 5 nodes, 
0 to 4, of which 2 nodes are internal nodes (only nodes 1 and 3 have children).
"""
from collections import Counter

def count_internal_nodes(tree):
    C = 0; i = 0
    counter_tree = Counter(tree)  # Returning a dictionary of counting number of occurance
    
    for i in counter_tree:
        if counter_tree[tree[i]] >=2:
             C = C+1
        elif counter_tree[tree[i]] == 1:
            pass
    return C

tree = [1, 3, 1, -1, 3]
print (count_internal_nodes(tree)) # should print 2
