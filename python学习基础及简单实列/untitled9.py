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
"""
#以只读的形式打开一个文件
import pandas as pd
path = ('CodingZhang\household_power_consumption_1000.txt')
df = pd.read_csv(path,sep = ';')
