#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:13:12 2018

@author: lulu
"""

"""
step1:获取数据集--sklearn中包含列大量优质的数据集，篇使用其内置数组集，导入模块
"""
#from __future__ import print_function  #使得python2的print()和python3中的print一样
from sklearn import datasets
from sklearn.cross_validation import train_test_split  #随机划分训练集和测试集
from sklearn.neighbors import KNeighborsClassifier   #利用KN算法进行分类
from sklearn.metrics import accuracy_score  #误差分析

#创建数据集:加载iris数据，把属性存在x中，类别标签存在y中
iris = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target
#观察数据集，x有四个属性，y有三个标签：0，1，2
#print(iris_x[:2,:])  #查看前两行的数据
#print(iris_y)

#把数据集分为训练集和测试集，其中test_size = 0.3,即测试集占总数据的30%
x_train,x_test,y_train,y_test = train_test_split(iris_x,iris_y,test_size = 0.3)
#可以看到分开后的数据集顺序都是打乱的，这样更有利于学习模型
#print(y_train)

#定义模型——训练模型——预测
"""
定义模块方式 KNeighborsClassifiter()
用fit来训练 training data 这一步就完成来训练的所有步骤
后面的knn就已经是训练好的模型，可以直接用predict测试集的数据
对比模型的预测值和真实值，可以看到大概模拟出来数据，但是有误差
"""
knn = KNeighborsClassifier()  #直接调用knn分类即可
knn.fit(x_train,y_train)  #将调用的模型应用与训练集
y_pred = knn.predict(x_test)
#print(knn.predict(x_test))  #对测试集进行预测
#print(y_test)  #真实的训练集

#误差分析
score = accuracy_score(y_test,y_pred)
print(score)  #预测的准确率

true_count = accuracy_score(y_test,y_pred,normalize = False)
print(true_count)  #预测正确的个数









