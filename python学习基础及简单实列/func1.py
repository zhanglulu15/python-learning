#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:52:26 2018

@author: lulu
"""

#定义函数字符串是不可变的
def func1(str):
    print('func recived sring: ', str)
    str = 'my func'
    print('func new string: ', str)
    
str = 'lulu'
# call func
print('string: ', str)
func1(str)
print('string: ', str)

#列表是可变的
def funcl(l):
    print('func recived list: ', l)
    l[2] = 8
    print('func new list: ', l)
    

l = [1, 2, 3, 4]
print('list: ', l)
funcl(l)
print('list: ', l)
