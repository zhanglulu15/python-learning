#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 12:14:15 2018

@author: lulu
"""

#输出1到100中的素数
a = []
for i in range(2,100):
    for j in range(2,i):
        if i%j == 0:
            break    #如果满足i除以j余数为0 ，则跳出此次循环，进行下次循环
    else:
        a.append(i)
        print(i)
print('素数的个数为:',len(a))

#break实列
list = 'python'
for i in list:
    if i == 'h':
        break
    print(i)
    
var = 10
while var > 0:
    var = var-1
    if var == 5:   #当var等于5时跳出循环
        break
    print(var)