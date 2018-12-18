#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:36:59 2018

@author: lulu
"""

"""
用字典记录学生的名字和分数补充知识
"""
#可以看到items()方法把dict对象转换成列包含tuple的list，我们对这个list进行迭代，可以同时获得key和value
d = {'Adam':95,'Lisa':90,'Bart':58}
print(d.items())

for key,value in d.items():
    print(key,':',value)
 
#创建一个字典students
students = {}
name = str(input('输入姓名:'))
age = int(input('输入年龄:'))
#将姓名和年龄以字典的形式储存
students[str(name)] = age
print(students)

#重复打印某个字符
name = 'xiaomi'
print(name.center(10,'-'))  #总共有10个字符，把‘xiaomi'放在中间

