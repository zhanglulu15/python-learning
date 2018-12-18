#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:30:47 2018

@author: lulu
"""

"""
打印出1到1000所有的水仙花数，所谓水仙花数是指一个三位数，其各位数字立方等于该数本身，列如：153就是一个水仙花数
"""
num = [] #用一个空列表来存放数据
for i in range(100,1001):
    l = list(str(i))   #将字符串转换为列表的形式
    numbers = [int(x) for x in l]  #将列表中的元素转换为整数型
    #print(numbers)
    
#print(numbers)
    
    if (int(numbers[0]) ** 3) + (int(numbers[1]) ** 3) + int((numbers[2] ** 3)) == i:
        print(i,'该数为水仙花数')

    
    

    