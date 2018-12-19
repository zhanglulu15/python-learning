#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 17:46:54 2018

@author: lulu

tensorflow中的placeholder学习，placeholder是tensorflow中的占位符，暂时储存变量
tensorflow如果想要从外部传入data,那就需要用到tf.placeholder(),然后以这种字典的形式传输数据
sess.run(***,feed_dict{input:**})  
"""
import tensorflow as tf

#在tensorflow中需要定义placeholder的type,一般为float32的形式
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

#mul = multiply是将input1和input2相乘
output = tf.multiply(input1,input2)

#接下来，传值的工作交给了sess.run()，需要传入的值放在feed_dict = {}并意义对应每一个input.placeholder
#与feed_dict{}是绑定一起出现的
with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:7,input2:6}))
