#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 18:00:57 2018

@author: lulu
添加层：def add_layer()
在tensorflow里定义一个添加层的函数可以很容易的添加神经层，为之后的添加省下不少时间
神经层常见的参数有weight、biases和激励函数

"""
import tensorflow as tf

#定义添加神经层的函数，def add_layer()它有四个参数：输入值、输入值的size、输出值的size、激励函数
def add_layer(inputs,inputs_size,outputs_size,activation_function = None):
    
#接下来定义Weights和biases,因为在生成初始参数时，随机变量会比全部为0 好一些，所以我们这里的
#Weights为一个inputs_size行，outputs_size列的随机变量矩阵
    Weights = tf.Variable(tf.random_normal([inputs_size,outputs_size]))
    
#在机器学习中biases的值不推荐为0 ，因此在此基础上有添加的0.1
    biases = tf.Variable(tf.zeros([1,outputs_size]) + 0.1)

#下面定义Wx_plus_b,即神经忘了未激活的值，其中，tf.matmul()是矩阵乘法
    Wx_plus_b = tf.matmul(inputs,Weights) + biases
    
#当activation_function（激励函数）为None时，输出就是当前的预测值Wx_plus_b,不为None时，
#就把Wx_plus_b传到activation_function中得到输出
    if activation_function == None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

    
