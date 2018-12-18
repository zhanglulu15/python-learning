#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:55:25 2018

@author: lulu
"""

"""
sklearn的属性和功能
"""
from sklearn import datasets  #导入数据集
from sklearn.linear_model import LinearRegression  #导入线性回归的包
from sklearn.cross_validation import train_test_split

load_data = datasets.load_boston()
data_x = load_data.data
data_y = load_data.target

model = LinearRegression()
model.fit(data_x,data_y)

#print(model.coef_)  #y = ax + b,这里求的是a
#print(model.intercept_)  #y = ax + b ，这里求的是b

#print(model.intercept_)  #定义的参数（系统默认的也会输出）

print(model.score(data_x,data_y))  #R^2