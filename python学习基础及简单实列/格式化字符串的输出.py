#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:07:13 2018

@author: lulu
"""

#格式化字符串的输出

print("my name is %s and my age is %d:" % ('lulu',24))

''' %s 是格式化输出字符串
    %d 是格式化输出整数
    %f 是格式化浮点数的输出，可以指定小数点后面的位数
'''

#\n 表示换行
text = 'this is first text \n this is next text \n this is last text'
print(text)
myfile = open('myfile.txt','w')
myfile.write(text)
myfile.close