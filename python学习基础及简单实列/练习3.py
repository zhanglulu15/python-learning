#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:06:11 2018

@author: lulu
"""

#计算二次方程
import cmath
a = float(input('输入a:'))
b = float(input('输入b:'))
c = float(input('输入c:'))
d = (b ** 2) - (4 * a * c)
sol1 = (-b - cmath.sqrt(d))/(2 * a)
sol2 = (-b + cmath.sqrt(d))/(2 * a)
print('方程的解为{0}和{1}'.format(sol1,sol2))