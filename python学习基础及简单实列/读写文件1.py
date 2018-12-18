#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:07:49 2018

@author: lulu
"""


#逐行读取
file = open('test1.txt','r')
first_content = file.readline()  #读取第一行的内容
second_content = file.readline() #读取第二行的内容
print(first_content,second_content)
all_content = file.readlines()   #读取所有的内容，如果前面已经读取了前前面的内容，这里只会读取剩下的内容
                                 #并且是以列表的形式表现出来
print(all_content)