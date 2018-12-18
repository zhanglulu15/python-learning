#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:44:41 2018

@author: lulu
"""

"""
sklearn中的数据库
"""
#导入包
from sklearn import datasets  #导入数据集
from sklearn.linear_model import LinearRegression  #导入线性回归的包
from sklearn.cross_validation import train_test_split 
from sklearn.metrics import accuracy_score  #误差分析

 #导入波士顿房价的包
boast = datasets.load_boston()
boast_x = boast.data  
#print(boast_x[:4])  #查看影响波士顿房价的各个属性
boast_y = boast.target  
#print(boast_y[:4])  #查看类别标签

model = LinearRegression()  #载入模型
x_train,x_test,y_train,y_test = train_test_split(boast_x,boast_y,test_size = 0.3)
model.fit(x_train,y_train)  #将模型应用于训练集
pred = model.predict(x_test)

#误差分析:对线性模型进行打分
print(model.score(boast_x,boast_y))
#print(model.predict(boast_x[:4,:]))
#print(boast_y[:4])



import matplotlib.pyplot as plt  #画图的包
#自己建立一个样本
x,y = datasets.make_regression(n_samples = 100,n_features = 1,n_targets =1,noise = 1)
#plt.scatter(x,y)  #以点的形式输出