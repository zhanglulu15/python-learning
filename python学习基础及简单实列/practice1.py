#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:31:07 2018

@author: lulu
"""
#practice1
d = []
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a!=b) and (a!=c) and (b!=c):
                d.append([a,b,c])
print("总数量",len(d))
print(d)