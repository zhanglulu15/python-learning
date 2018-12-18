#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:21:54 2018

@author: lulu
"""

#迭代器
list = [1,2,3,4]
it = iter(list)  #生成迭代器
print(next(it))  #输出迭代器下一个对象
print(next(it))

#迭代器可以使用for进行遍历
for x in it:
    print(x)
    
def stud(name,age,addr):
    print('I\'m a student')
    print('my name is {0},age is {1},addr is {2}'.format(name,age,addr))

n = 'jingjing'
a = 17
addr = 'nanjing'
stud(n,a,addr)

