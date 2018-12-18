#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:36:23 2018

@author: lulu
"""

#python实列2
#输入两个数字并对其进行求和在本列中，使用input来获取用户的输入，input()返回一个字符串，所以需要使用
#float()将字符串转换为数字
a = input('输入的数字为：')
b = input('输入的数字为：')
c = float(a) + float(b)
print('输入的数字分别为{0}和{1}，输出的和为:{2}'.format(a,b,c))
#备注：sum只能对列表，集合，元组求和

