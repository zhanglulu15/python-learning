#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 20:46:47 2018

@author: lulu
"""

#模型：分析时间和功率的关系
import pandas as pd
import numpy as np
import time
import sklearn
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import StandarScaler

#读取文件，将代码和文件放在来同一个目录
path = 'household_power_consumption_1000.txt'

#
names = ['Date','Time','Global_active_power','Global_reactive_power','Voltage;Global_intensity',
         'Sub_metering_1','Sub_metering_2','Sub_metering_3']

#线性模型
df = pd.read_csv(path,sep = ';')

#读取前五行
print(df.head())

#看所有的变量值,即分布
for i in df.columns:
    a = df[i].value_counts()

#处理空缺值:以替代空缺值
new_df = df.replace('?',np.nan)  
datas = new_df.dropna(how = 'any')

#创建一个时间字符串格式化
def date_format(dt):
    t = time.strptime(' '.join(dt),'%d/%m/%Y %H:%M:%S')
    return (t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min,t.tm_sec)

#获取X，Y变量，将时间转换为数值型的连续变量
X = datas[names[0:2]]
X = X.apply(lambda x : pd.Series(date_format(x)),axis = 1)  
Y = datas[names[2]]  #功率
#读取前五行
print(X.head(5))
print(Y.head(5))

#对数据进行训练集和测试集的划分:训练样本：80%，测试样本：20%
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 0)

#数据标准化
ss = StandarScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

#训练模型:线性回归
lr = LinearRegression() 
lr.fit = (X_train,Y_train)

#模型检验
print('准确率:',lr.score(X_train,Y_train))

#预测Y值
y_predict = lr.predict(X_test)

from sklearn.externals import joblib
#模型保存
joblib.dump(ss,"data_ss.model")
joblib.dump(lr,"data_lr.model")
#加载模型:一元模型
joblib.load("data_ss.model")
joblib.load("data_lr.model")

#设置字符集，防止中文乱码
mpl.rcParams['font.sans-serif'] = [u'simHei']
mpl.rcParams['axes.unicode_minus'] = False

#预测值与实际值画图比较
t = np.arange(len(X_test))
plt.figure(facecolor = 'w')
plt.plot(t,Y_test,'r-',linewidth = 2,label = u'真实值')
plt.plot(t,y_predict,'g-',linewidth = 2,label = u'预测值')
plt.legend(loc = 'lower right')
plt.title(u'线性回归预测时间与功率之间的关系',fontsize = 20)
plt.grid(b = True)
plt.show






















