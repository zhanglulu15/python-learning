#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:51:48 2018

@author: lulu
"""

"""
暂停一秒输出，并格式化当前输出时间
"""
import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(1)  #暂停一秒输出
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


import datetime
time.sleep(1)
time_now = datetime.datetime.now()
print(time_now.strftime('%Y-%m-%d %H:%M:%S'))