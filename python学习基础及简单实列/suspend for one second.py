#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 09:53:33 2018

@author: lulu
"""

#暂停一秒输出：使用time模块的sleep()函数
import time
myd = {1:'a',2:'b'}
for key,value in dict.items(myd):
    print(key,value)
    time.sleep(5)  #sleep()中的数字是几，就暂停几秒输出