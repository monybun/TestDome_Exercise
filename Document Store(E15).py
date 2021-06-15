#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The DocumentStore class is used to model a document store. It needs to satisfy the following conditions:

The documents property should return a list containing the contents of the store. 
There should be no way to modify the contents of the document store through it.
The add_document(document) method should add a new document to the store. 
If the document store is full, an exception should be raised.
The __repr__ method should return the document store's description in the format 
"Document store: number of documents/capacity". 

For example, if the capacity of the document store is 2 and one document is added to it, 
it should return: "Document store: 1/2".
Fix the bugs!
"""

class DocumentStore(object):
       
    def __init__(self, capacity):
        self._capacity = capacity  #a leading underscore is to make sure the attribute is private (non-public), so other developers cannot modify it directly 
        self._documents = []
    '''
    The @property is a built-in decorator for the property() function in Python. 
    It is used to give "special" functionality to certain methods to make them act as getters, setters, 
    or deleters when we define properties in a class.
    ''' 
    @property
    def capacity(self):
        return self._capacity

    @property #the Getter
    def documents(self):
        return self._documents

    @documents.setter
    def documents(self, list_val):
        self._documents = list_val
    def add_document(self, *document):
        for arg in document:
            self._documents.append(arg)

        if(len(self._documents) > self._capacity):
            raise Exception('Document store is full')
            self._documents.remove(document)
    
    def __repr__(self):
        return '{}{!r}/{!r}'.format("Document store: ", len(self._documents), self._capacity)
#  str:  "Document store: {}" + len(self._documents)+ "/" + self._capacity

#To see the output, uncomment the lines belows:
document_store = DocumentStore(2)
document_store.add_document("document")
print(document_store)