#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:33:39 2018

@author: lulu

tensorflow学习之-tf.Variable
在tensorflow中，定义了某字符串是变量，它才是真正的变量，定义语法：
state = tf.Varibale()
"""
import tensorflow as tf
state = tf.Variable(0,name = 'counter')

#定义常量1
one = tf.constant(1)

#定义加法步骤（注：此步并没有直接进行计算)
new_value = tf.add(state,one)
#也可以写成 new_value = tf.add(state,1)

#将state更新成new_state
update = tf.assign(state,new_value)

#如果在tensorflow中设定了变量，那么初始化变量是最重要的，所以在定义了变量之后，一定要定义init = tf.initialize_all_variables()
init = tf.global_variables_initializer()

#使用sess
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):   #循环的东西不需要用到，只是为了让程序循环3次即可，所以用for _ in range(3)
        sess.run(update)
        print(sess.run(state))

