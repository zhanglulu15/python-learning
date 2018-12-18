#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:42:58 2018

@author: lulu
"""

"""
python对文件的读写
读取文件:首先找到文件所在的目录，文件与代码的执行文件在相同路径下，直接用文件名字就可以打开文件，
文件与代码不在同一个目录下面，则需要通过绝对路径找到文件。
文件的路径：需要用取消转义的方式来表示，如：
f = open(r'C:\\User\\Administrator\\Destop\\test.txt','w',enconding = 'utf-8')
利用pandas读取文件
"""
#pandas读取文件
import pandas as pd
path = ('household_power_consumption_1000.txt')
df = pd.read_csv(path,sep = ';')
print(df.head())  #读取前五行

#读取文件第一行
data = pd.read_csv('household_power_consumption_1000.txt',nrows = 0)
print(data.columns)

#读取某一列
print(df['Date'])

#读取某一行(第2行)
print(df.ix[1]) 


