#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:10:34 2019

@author: arpanpatel
"""

data = [1,2,3,4,5,6,7,8,9,10]

low = 3
high = 9
while(low<high):
    data[low] = 0
    low+=1


print(data)