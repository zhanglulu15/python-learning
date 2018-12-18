#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:16:13 2018

@author: lulu
"""

var1 = 'hello word'
var2 = 'python runoob'
print(len(var1[:3]))   #打印出前三个字母,，从0开始，0，1，2三个字母，3不算在里面
print(len(var1[0:3]))  #同上
print('新的字符串:',var1[:6]+ var2[7:13])  #可以对字符串进行组合

a = 'hello '
b = 'python'
print('a + b 的输出结果:',a[:6] + b)
print('a * 2 的输出结果:',a * 2)

if "h" in a:
    print('h in a')
else:
    print('h not in a')