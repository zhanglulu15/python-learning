#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:53:19 2018

@author: lulu
怎样建照一个完整的神经网络，包括添加神经层，计算误差，判断是否学习

"""
#导入模块
import tensorflow as tf
import numpy as np

#构造添加一个神经层的函数
def add_layer(inputs,in_size,out_size,activation_function = None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs,Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

#导入数据:构造所需的数据：这里的x_data和y_data并不是严格的一元二次函数的关系，因为这里多加了一个噪音noise
#这样看起来更像真实情况
"""
补充知识1:
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
在指定的间隔内返回均匀间隔的数字。
返回num均匀分布的样本，在[start, stop]，这个区间的端点可以任意的被排除在外。

补充知识2:
 [:,np.newaxis]：作用是增加一个纬度   
"""
x_data = np.linspace(-1,1,300)[:,np.newaxis]   #np.newaxis是为了增加一个纬度
noise = np.random.normal(0,0.05,x_data.shape).astype(np.float32)  #增加一个噪音
y_data = np.square(x_data)-0.5 + noise



#利用占位符定义我们需要的神经网络的输入，tf.placeholder()就表示占位符，这里的None代表无论输入无论
#有多少都可以，因为输入只有一个特征，所以这里是 1
"""
补充知识3:
tf.placeholder(dtype, shape=None, name=None)

此函数可以理解为形参，用于定义过程，在执行的时候再赋具体的值

参数说明：
dtype：数据类型。常用的是tf.float32,tf.float64等数值类型
shape：数据形状。默认是None，就是一维值，也可以是多维，比如[2,3], [None, 3]表示列是3，行不定
name：名称。
"""
ys = tf.placeholder(tf.float32,[None,1])   #列是1，行不定
xs = tf.placeholder(tf.float32,[None,1])

"""
接下来要开始定义神经层了，通常神经层包括输入层/隐藏层/输出层。这里的输入层只有一个属性，所以我们就只有一个输入
隐藏层我们可以自己假设，这里我们假设隐藏层有10个神经元，输出层和输入层的结构是一样的，所以我们的输出层也是
只有一层，我们构建的神经网络是--输入层1层，隐藏层10层，输出层1层

下面开始定义隐藏层，利用之前的add_layer函数，这里使用tensorflow自带的激励函数：tf.nn.relu
"""
l1 = add_layer(xs,1,10,activation_function = tf.nn.relu)


#接着，定义输出层，此时的输入就是隐藏层的输出-l1,输入有10层（隐藏层的输出层），输出有1层
prediction = add_layer(l1,10,1,activation_function = None)

#计算预测值prediction和真实值的误差，对二者的平方求和在取平均值
"""
补充知识4:
reduction_indices=[1]表示在行的纬度上对数组进行压缩
reduction_indices=[0]表示在列的纬度上对数组进行压缩

在tensorflow的使用中，经常会使用tf.reduce_mean,tf.reduce_sum等函数，在函数中，
有一个reduction_indices参数，表示函数的处理维度.
需要注意的一点，在很多的时候，我们看到别人的代码中并没有reduction_indices这个参数，
此时该参数取默认值None，将把input_tensor降到0维，也就是一个数。
"""
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices = [1]))

#接下来很关键的一步，如何让机器学习提升他的准确度，tf.train.GradientDescentOptimizer()中的学习率
#通常都小于1，这里取0.1，代表以0.1的效率来最小化误差loss
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#使用变量时，都需要对他进行初始化，这是必不可少的
init = tf.global_variables_initializer()

#定义Session来执行init初始化步骤
sess = tf.Session()
sess.run(init)

#训练
"""
下面让机器学恶习1000次，机器学习的内容是train_step,用Session来run每一次training的数据，逐步提升神经网络
预测的准确性（注意：当运算要用到placeholder时，就需要feed_dict这个字典来指定输入
"""
for i in range(1000):
    #training
    sess.run(train_step,feed_dict = {xs:x_data,ys:y_data})
    
#每50步我们输出一下机器学习的误差
    if i % 50 == 0:
        print(sess.run(loss,feed_dict = {xs:x_data,ys:y_data}))



















