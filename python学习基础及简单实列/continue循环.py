#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:22:28 2018

@author: lulu
"""

#continue跳出本次循环，break跳出整个循环
#continue是一个删除效果，目的是为了删除循环中某些不需要的部分
list = 'python'
for i in list:
    if i == 't':
        continue   #跳出本次循环开始另一次循环
    print(i)
    
var = 10
while var > 0:
    var = var -1
    if var == 5:    
        continue   #当var等于5时跳出循环，因此整个循环中不包含5
    print(var)
 
#输出0到10之间的质数
a = 10
while a > 0:
    a = a - 1
    if a % 2 == 0:
        continue
    print(a)
    
#pass 是空语句，是为了保持程序结构的完整性
a = 10
while a > 0:
    a = a - 1
    if a == 5:
        pass   #不做任何事情，一般只做占位
    print(a)