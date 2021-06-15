#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
You receive a string that contains an XML log file like the following:

<?xml version="1.0" encoding="UTF-8" ?>
<log>
    <entry id="1">
        <message>Application started</message>
    </entry>
    <entry id="2">
        <message>Application ended</message>
    </entry>
</log>
Implement a function ids_by_message that returns the ids of the entries that contain a specific message. 
The ids should be integer values and the array does not need to be sorted.

For example, ids_by_message for the XML log above and for the message "Application ended" should return [ 2 ].
"""
#help:https://stackoverflow.com/questions/12669404/how-to-get-total-count-in-root-iter-in-elementtree
#https://www.edureka.co/blog/python-xml-parser-tutorial/
'''
for x in treeroot:
    print(x.tag,x.attrib)
[out]:
    entry {'id': '1'}
    entry {'id': '2'}

treeroot[0][0].text
[out]: Application started

treeroot[1][0].text
[out]: Application ended
'''
import xml.etree.ElementTree as ET

def ids_by_message(xml, message):
    treeroot=ET.fromstring(xml)

    id = ''
    ID = []
    
    for i in range(len(treeroot)):
        for x in range(len(treeroot[i])):
            if  message in treeroot[i][x].text:
                id = int(treeroot[i].attrib['id'])
                if id != '':
                    ID.append(id)
    return ID
xml = """<?xml version="1.0" encoding="UTF-8"?>
<log>
    <entry id="1">
        <message>Application started</message>
    </entry>
    <entry id="2">
        <message>Application ended</message>
    </entry>
</log>"""
print(ids_by_message(xml, 'Application ended'))