#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:23:28 2018

@author: lulu
"""

#计算三角形面积
a = float(input('输入边长a:'))
b = float(input('输入边长b:'))
c = float(input('输入边长c:'))
if a+b < c or a+c <b or b+c <a:
    print('三角形不合法')
else:
    s = (a + b + c)/2
    area = s*(s-a)*(s-b)*(s-c)*0.5
    print('三角形的面积为%0.3f'%area)