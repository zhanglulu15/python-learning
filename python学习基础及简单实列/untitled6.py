#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:15:13 2018

@author: lulu
"""

import math
result = []
for i in range(101,201):
    flag = True
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            flag = False
            continue
    if flag == True:
        result.append(i)
print(result)
print(len(result))
        
        
    