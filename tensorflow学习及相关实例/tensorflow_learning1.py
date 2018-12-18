#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:59:01 2018

@author: lulu

tensorflow学习

补充学习1:
np.random.rand(与np.random.randn用法相同)：
通过该函数返回一组服从（0，1）的正态分布随机样本值，且随机样本的取值为0到1，且不包括1

补充学习2:
tf.random.read()函数
参数如下：
random_uniform(shape,minval=0,maxval=None,dtype=tf.float32,seed=None,name=None)
返回值：返回一个shape大小的数组，且值位于low和high之间
参数说明 
shape：一维整数张量或 Python 数组。输出张量的形状。
minval：dtype 类型的 0-D 张量或 Python 值；生成的随机值范围的下限；默认为0。
maxval：dtype 类型的 0-D 张量或 Python 值。要生成的随机值范围的上限。如果 dtype 是浮点，则默认为1 。
dtype：输出的类型：float16、float32、float64、int32、orint64。
seed：一个 Python 整数。用于为分布创建一个随机种子。查看 tf.set_random_seed 行为。
name：操作的名称（可选）。
"""
#创建数据集
import numpy as np
import tensorflow as tf
x_data = np.random.rand(100).astype(np.float)  #生成一个服从0，1的正态分布的100个数组
y_data = x_data * 0.1 + 0.3   
#print(len(x_data))
#print(y_data)

#用tf.Variable来创建描述y的参数，可以把 y_data = x_data * 0.1 + 0.3想象成 y = w * 0.1 +b
w = tf.Variable(tf.random_uniform([1],-1.0,1.0))  #开始随机生成的一个w值

#print(w)
b = tf.Variable(tf.zeros([1]))  #开始随机生成的b值为0
y = w * x_data + b


#计算误差y和y_data的误差
loss = tf.reduce_mean(tf.square(y - y_data))


#传播误差，反向传播误差的构造就教给optimizer量了，我们使用的误差传递方法是提督下降法：Gradient Descent
#然后我们用optimizer进行参数更新
optimizer = tf.train.GradientDescentOptimizer(0.5)   #学习率为0.5
train = optimizer.minimize(loss)  #在梯度下降法的基础上将误差最小化

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

#print(sess.run(b))
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step,sess.run(w),sess.run(b))













































