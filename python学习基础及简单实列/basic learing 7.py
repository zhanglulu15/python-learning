#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 11:01:38 2018

@author: lulu
"""

#for 循环：
for letter in 'python':
    print("当前字母：",letter)
    
fruits = ["香蕉","苹果","桃子"]
for fruit in fruits:
    print("当前水果:",fruit)
print('good bye')

#通过索引迭代
fruits = ["香蕉","苹果","桃子"]
for index in range(len(fruits)):
    print("当前水果：",fruits[index])
    
#if...elese...
for num in range(10,20):
    for i in range(2,num):
        if num % i == 0:
            j = num/i
            print("%d 等于 %d * %d:"%(num,i,j))
            break   #循环一次后要跳出循环，因为一个数可能有好几个数相乘而得
else:
    print("num是一个质数:",num)
    
#输出2到100之间的质数
a = []
for i in range(2,100):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        a.append(i)
print(a)

s = 'ascbnhyukihyt'
for i in range(1,len(s),2):
    print(s[i])

            