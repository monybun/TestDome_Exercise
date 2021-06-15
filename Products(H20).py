#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement the function sort_by_price_ascending, which:
*Accepts a string in JSON format, as in the example below.
*Orders items by price in ascending order. 
*If two products have the same price, it orders them by their name in alphabetical order.
*Returns a string in JSON format that is equivalent to the one in the input format.

For example, the call:
sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]');

should return:
'[{"name":"eggs","price":1},{"name":"rice","price":4.04},{"name":"coffee","price":9.99}]'
"""
import json
def sort_by_price_ascending(json_string):
    #parse the JSON string to a list of dictionary
    json_list = json.loads(json_string)
    
    #sort firstly by 'price' (ascending--reverse:False), then by 'name'
    json_list_SortedByPrice = sorted(json_list, key=lambda x : (x['price'],x['name']), reverse=False)
    
    #convert the sorted JSON list to string
    string_JSON_output = json.dumps(json_list_SortedByPrice)

    return string_JSON_output

print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))
