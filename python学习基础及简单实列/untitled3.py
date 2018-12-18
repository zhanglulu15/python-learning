#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:00:35 2018

@author: lulu
"""

"""
numpy学习1
"""
#倒入numpy库
import numpy as np
"""
python内置数组结构,list(列表)：list数组中保存的数据类型是不用相同的，可以是字符串,可以是整型数据，甚至可以
是类实列（使用Numpy可以减少内存的使用）
"""
a = [1,2,3,4,5]
#print(type(a))
print('a=',a)
b = np.array(a)  #numpy 数组结构
#print(type(b))
print('b=',b)

#numpy常用操作
#创建一纬数组
a1 = np.array([1,2,3])  
a2 = np.asarray([1,2,3])
print('a1=',a1)
print('a2=',a2)

#创建多维数组
a6 = np.array(([1,2,3],[4,5,6]))
print('a6=',a6)

#3行2列，全0矩阵
a3 = np.zeros((3,2))
print('a3=',a3)

#全1矩阵
a4 = np.ones((3,2))
print('a4=',a4)

#3行2列全部填充5
a5 = np.full((3,2),5)
print('a5=',a5)

"""
numpy常用操作:数值计算
"""
arr1 = np.array(([1,2,3],[4,5,6]))
arr2 = np.array([[6,5],[4,3],[2,1]])

#查看arr的纬度
print('arr1=',arr1)
print(arr1.shape)  #2行3列

print('arr1=',arr2)
print(arr2.shape)  #3行2列

#切片
arr3 = np.array([1,2,3,4,5,6])[:3]  
print('arr3=',arr3)
#二维切片
print(arr1[0:2,0:2])

#乘法:对应元素相乘
arr4 = np.array([1,2,3]) * np.array([2,3,4])
print(arr4)
#矩阵乘法
print(arr1.dot(arr2))  #行=列，列=行

#矩阵求和
print('arr1矩阵所有元素之和:',np.sum(arr1))
print('arr1矩阵列元素之和:',np.sum(arr1,axis = 0))
print('arr1矩阵行元素之和:',np.sum(arr1,axis = 1))

"""
进阶计算
"""
#布尔型数组访问方式
arr = np.array(([1,2],[3,4],[5,6]))
print('布尔值访问:',(arr > 2))
print('输出布尔值为True所对应的元素:',arr[arr > 2])

#修改形状
print('将arr矩阵的形状修改为两行三列，输出:',arr.reshape(2,3))
print('将arr矩阵摊平(一行一列），输出:',arr.flatten())
print('将arr转置，输出:',arr.T)


















