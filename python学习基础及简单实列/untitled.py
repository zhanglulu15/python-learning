#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 17:35:19 2018

@author: lulu
"""

"""
p判断101-201之间有多少个素数（质数），并输出所有素数
质数：只能被1和它本身除
"""

count = []
for i in range(101,201):
    #print(i)
    for j in range(2,i):
        #print(j)
        if i % j == 0:
            break
    else:   
        count.append(i)
print(len(count))        
print(count)


#方法2
import math
m = range(101,201)
p = list(m) #将101到201范围内的数字按列表输出
#print(list(m))
for i in range(101,201):
    for j in range(2,int(math.sqrt(i)+1)):  #用这个数分别请除2到这个数的平方根，如果能被整除，则不为素数
        if i % j == 0:
            p.remove(i)
            break
print(p)

#方法3:
import math
def sushu():
    result = []
    for i in range(100,201):
        for j in range(i,int(math.sqrt(i)+1)):
            if i % j == 0:
                flag = True
                continue
            else:
                flag = False
            if flag == False:
                result.append(i)
                print(result)
sushu()

















