#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:31:54 2018

@author: lulu
"""

"""
数据预处理：
一、数据归一化
"""
from sklearn import preprocessing
import numpy as np
a = np.array([[10,2.7,3.6],
              [-100,5,-2],
              [120,20,40]])
#print(a)  #未做标准化处理
#print(preprocessing.scale(a))  #标准化处理结果

from sklearn.cross_validation import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt


#生成一个data
x,y = make_classification(n_samples = 300,n_features = 2,n_redundant = 0,n_informative = 2,
                          random_state = 22,n_clusters_per_class = 1,scale = 100)
plt.scatter(x[:,0],x[:,1],c = y)  #画出图形
plt.show()