#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:36:10 2018

@author: lulu
"""
    
"""
用字典记录学生的名字核分数
"""

student = {}  #设置一个空的字典，存放输入的键和值
write = 1
while write:  #当输入为1时，继续输入姓名和成绩信息
    name = str(input('输入姓名:'))
    grade = int(input('输入分数:'))
    student[str(name)]= grade   #将姓名和成绩存放到student中，组成字典student
    write = int(input('继续输入?\n 1/继续 0/退出'))
print('name rate'.center(20,'-'))  #总共20个字符，name 和rate放在中间
for key,value in student.items():  
    if value >= 90:
        print('%s %d A'.center(20,'-'))
    elif 90 > value >= 60:
        print('%s %d B'.center(20,'-'))
    else:
        print('%s %d C'.center(20,'-'))
