#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:58:45 2018

@author: lulu
"""

text = 'this is first text.\n this is next text.\n this is last text'
print(text)
test1 = open('test1.txt','w')
test1.write(text)  #将text里面的内容写入 test1这个文件名
test1.close  #关掉文件

#增加一行
new_text = '\n this is append text'
print(new_text)
test1 = open('test1.txt','a')  #新增一列
test1.write(new_text)
test1.close 


#读取文件中的内容
file = open('test1.txt','r')  #打开的只是这个文件的名称
content = file.read()   #打开文件中的内容，并将其赋给content
print(content)