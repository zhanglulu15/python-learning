#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:49:58 2018

@author: lulu
"""

"""
将一个整数分解质因数，例如：输入90，打印出 90 = 2*3*3*5
程序分析：对n进行质因数分解，应先找到一个最小的质数k，然后按下述步骤完成
step1:如果对这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可
step2:如果n小于或者大于k,则说明应该打印出k的值，并用n除以k的商，重复执行第一步
step3:如果n不能被k整除，则用k+1作为k的值，重复执行第一步
"""
x = int(input('是否进入循环？是:1,否:0\n'))  #进入循环，输入一个数字找到其质因数
while x:
    n = int(input('请输入一个正整数:'))
    while n > 1:
        for i in range(2,n+1):
            if n % i == 0:
                n = int(n/i)
                #print(n)
                if n == 1:
                    print('%d'%n,end = "").split('')
                else:
                    print('%d'%n,end = "").split('')
                break
                
    x = int(input('是否进入循环？是:1,否:0\n'))  #最后退出循环
            