#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement the function areas that when given a circle's radius r and angle of a segment in degrees a, 
returns a list of floats containing both the area inside the segment, 
and the area of the circle that's outside the segment. 

The first list element should contain the area covered by the segment, 
and the second list element should contain the area of the circle outside the segment

The area of a circle can be calculated with the following formula: CircleArea = pi*r^2

The area of a segment can be calculated with the following formula:
    Segment Area = 0.5*r^2*(a*pi/180 - sin(a*pi/180))

For example, areas(10, 90) should return approximately (28.539816, 285.619449),
where 28.539816 is the area inside the segment, and 285.619449 is the area of the circle that's outside the segment.

"""
import math

def areas(r, a):
    
    segment = ()
    pi = math.pi
    
    CircleArea = pi * r ** 2
    SegmentArea = 0.5*r**2 * (a*pi/180 - math.sin(a*pi/180))
    outside_SegmentArea = CircleArea - SegmentArea
    
    segment = (SegmentArea, outside_SegmentArea)
    return segment

print(areas(10, 90))


