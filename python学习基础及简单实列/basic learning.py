#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:46:30 2018

@author: lulu
"""
a = 10
b = 2
c = [1,2,3,4]
if a in c:
    print("a在c中")
else:
    print("a不在c中")

#字典
tinydict = {'name':'xiaoming','code':'95','sex':'famale'}
print(tinydict)    #输出整个字典
print(tinydict.keys())    #输出字典的s所有键
print(tinydict.values())  #输出字典的所有值

dict = {}
dict['one'] = "this is one"
dict['2'] = "this is two"
print(dict)