#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 21:03:09 2018

@author: lulu
"""

a = [1,2,3,4,56,78,9]
b = []
c = []
while len(a) > 0:
    d = a.pop()
    if d % 2 == 0:
        b.append(d)
    else:
        c.append(d)
print(len(b),b)
print(len(c),c)
        
count = 0
while count < 9:
    print('the count is:',count)
    count = count + 1
print("good bye")
    