#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:12:41 2018

@author: lulu
"""

"""
sklearn 学习1:
sklearn 是python重要的机器学习库，里面封装列大量的机器学习算法，如：分类、回归、降纬以及聚类
还包含列无监督学习，非监督学习，数据变换三大模块。sklear拥有完善的文档，使得它具有容易上手的优势，并内置列
大量的数据集，节省列获取和整理数据集的时间
"""
import sklearn
#近邻算法
sklearn.neighbors 

#支持向量机
sklearn.svm

#核-岭回归
#sklearn.kernel_ridge

#广义线性模型
sklearn.linear_model

#集成学习
#sklearn.ensemble

#决策树
#sklearn.tree

#朴素贝叶斯
#sklearn.naive_bayes

#交叉分解
sklearn.cross_decomposition

#高斯过程
sklearn.gaussian_process

#神经网络
sklearn.neural_network

#概率校准
sklearn.calibration

#保守回归
sklearn.isotonic

#特征选择
sklearn.feature_selection

#多类多标签算法
sklearn.multiclass

"""
以上的每个模型都包含多个算法，在调用时直接import即可
"""
from sklearn.linear_model import LogisticRefression
lr_model = LogisticRefression()

"""
无监督学习
"""
#矩阵因子分解
sklearn.decomposition

#聚类
sklearn.cluster

#流行学习
sklearn.manifold

#高斯混合模型
sklearn.mixture

#无监督神经网络
sklearn.neural_network

#协方差估计
sklearn.covariance

#数据变换
sklearn.feature_extraction

#特征选择
sklearn.feature_selection

#随机投影
sklearn.random_projection

#核逼近
sklearn.kernel_approximation

"""
sklearn 有统一的API接口，通常可以通过使用完全相同的接口来实现不同的机器学习算法，一般实现流程如下：
step1、数据加载核预处理  
step2、定义分类起  -- lr_model = LogisticRegression
step3、使用训练集核测试机 -- lr_model.fit(X,Y)
step4、使用训练好的模型进行预测 -- y_pred = lr_model.predict(X_test)
step5、对模型进行性能评估 -- lr_model.score(X_test,Y_test)
"""


#数据分割：常用命令
#作用：将数据集划分为 训练集核测试集
#格式：train_test_split(*arrays,** options)

from sklearn.model_selection import train_test_split
import numpy as np
x,y = np.arange(10).reshape((5,2))
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.33,random_state = 42)


#自己创建数据集
"""
n_samples:指定样本数
n_features:指定特征数
n_classes:指定分类数
random_state:随机种子，使得随机状可重
"""
from sklearn.datasets.samples_generator import make_classification
x1,y1 = make_classification(n_samples = 6,n_features = 5,n_informative = 2,
                            n_redundant = 2,n_classes = 2,n_clusters_per_class =2,
                            scale = 1.0,random_state = 20)

for x1_,y1_ in zip(x1,y1):
    print(y1_,end = ':')
    print(x1_)























