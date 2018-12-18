#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:39:03 2018

@author: lulu
"""

import tensorflow as tf
matrix1 = tf.constant([[3,3]])   #生成一个一行两列的矩阵
print(matrix1)

matrix2 = tf.constant([[2],
                       [2]])    #生成一个两行一列的矩阵
print(matrix2)
result = tf.matmul(matrix1,matrix2)   #矩阵相乘，np中矩阵相乘为:np.dpt(matrix1,matrix2)
sess = tf.Session()
result1 = sess.run(result)
print(result1)
sess.close()

#方法二,不用在关闭sess
with tf.Session() as sess:
    result2 = sess.run(result)
    print(result2)