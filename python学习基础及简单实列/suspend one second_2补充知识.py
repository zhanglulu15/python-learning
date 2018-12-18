#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 17:07:30 2018

@author: lulu
"""
"""
time 有四种类型（time,datetime,sting,timestamp)
"""
#1、sting 是最简单的表示time的方式，如下代码生成即为：string.生成实时的时间
import time
print(time.ctime())  #生成现在的年月日，时分秒

#2、datetime tuple是datetime.datetime对象类型
import datetime
print(datetime.datetime.now())

#3、time tuple 是time.struct_time对象类型
date_str = datetime.datetime.now()
print(date_str.strftime("%Y-%m-%d %H:%M:%S"))