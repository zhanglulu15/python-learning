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
x_train,x_test,y_train,y_test = train_test_split(boast_x,boast_y,test_size = 0.3)  #将数据分为训练集和测试集
model.fit(x_train,y_train)  #将模型应用于训练集
pred = model.predict(x_test)
#print(pred)  #输出测试数据
#print(y_test) #输出真实数据

#误差分析:对线性模型进行打分
#print(model.score(boast_x,boast_y))
#print(model.predict(boast_x[:4,:]))
#print(boast_y[:4])

#保存模型
import pickle
with open('model','wb') as f:
    pickle.dump(model,f)
    
#读取模型
with open('model','rb') as f:
    model = pickle.load(f)
model.predict(x_test)

#利用sklearn自带的方法joblib
from sklearn.externals import joblib
#保存模型
joblib.dump(model,'LinearRegression_model')

#载入模型
model = joblib.load('LinearRegression_model')

import matplotlib.pyplot as plt  #画图的包
"""
n_sample:指定样本数量
n_feature:指定特征数
n_classes:指定分类数
random_state:随机种子，使得随机状可重
"""
#随机生成分类变量（离散）
from sklearn.datasets.samples_generator import make_classification
x1,y1 = make_classification(n_samples = 6,n_features = 5,n_informative = 2,
                            n_redundant = 2,n_classes = 2,n_clusters_per_class = 2,
                            scale = 1.0,random_state = 20)

#随机生成连续变量（回归）
x,y = datasets.make_regression(n_samples = 100,n_features = 1,n_targets =1,noise = 1)

#plt.scatter(x,y)  #以点的形式输出















