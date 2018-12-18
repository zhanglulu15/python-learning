#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:47:06 2018

@author: lulu
"""

#平方根
a = float(input('请输入一个数字:'))
b = a ** 3
print('输入数字{0}的3次方为{1}'.format(a,b))

c = float(input('请输入一个数字:'))
d = c ** 2
print('输入数字%d的平方根为%0.2f' % (c,d))
#第一个%后的0表示占位为0，2表示小数点后保留两位小数，第二个%后的内容为显示内容
