#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:18:32 2018

@author: lulu
"""
#continue 和 break 的用法
i = 0
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print(i)
    
    
i = 2
while 30:   #循环条件为一个具体的数字，表明循环条件肯定成立
    print(i)
    i += 1
    if i >10:
        break
 
#这是一个无限循环，可以使用CTRL+C 来中断循环。
var = 1
while var ==2 :  #该循环条件为TRUE，循环将一直无限执行下去
    num = input("please input a number:")
    print("the number is:",num)
print("good bye")
