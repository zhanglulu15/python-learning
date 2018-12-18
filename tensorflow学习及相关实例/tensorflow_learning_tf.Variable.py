#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:38:20 2018

@author: lulu

tensorflow中的tf.Variable学习:
在tensorflow中变量的定义和初始化是分开的，所有关于图变量的赋值和计算都要通过tf.Session的run来进行,
想要将所有图变量进行集体初始化时应该使用tf.global_variables_initializer。
"""
import tensorflow as tf
x = tf.Variable(3,name = 'x')
y = x * 3
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
sess.run(y)




