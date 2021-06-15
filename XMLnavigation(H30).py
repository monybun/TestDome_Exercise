#!/usr/bin/env python
# -*- coding: utf-8 -*
# author: SAI
import os,sys,time,traceback,pdb,datetime
from types import SimpleNamespace
from xml.etree import ElementTree as ET 
class XmlNavigator(SimpleNamespace):
    def __init__(self, content):
        tree=ET.fromstring(content)
        self.text = ET.tostring(tree).decode('utf-8')
        self.set_child(self, tree)
        return
    
    def set_child(self, parent, tree):
        tag = tree.tag
        obj = SimpleNamespace()
        setattr(parent, tag, obj) 
        children = list(tree)
        if len(children): 
            all_text = '' 
            for i in children:
                self.set_child(obj, i)
                all_text += ET.tostring(i).decode('utf-8')
            obj.text = all_text
        else:
            obj.text = tree.text 
        return

def main():
    content ='''<?xml version="1.0" encoding="UTF-8"?>
<State><City>New York</City><City2>Los Angeles</City2></State>
'''
    # content=open('test.xml','r').read() 
    obj = XmlNavigator(content)
    print(obj.text)
    print(obj.State.text)
    print(hasattr(obj.State,'City'))
    print(obj.State.City.text)
    return

if __name__=='__main__':
    main()

