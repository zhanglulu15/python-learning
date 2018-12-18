#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 19:36:58 2018

@author: lulu
"""

a = 10
tmp = 5
a = tmp
a = 5
print(a)

apple = 100
def fun(a):
    a = a + 10
    return a 
print(fun(1))

a = 3
def fun1(a):
    a = a +9
    return a
print(fun1(a))
print(a)

def fun2(mylist):
    mylist.append([1,2,3,4])
    print('函数内部：',mylist)
mylist = [2,3,4,5]
fun2(mylist)
print('函数外部：',mylist)


