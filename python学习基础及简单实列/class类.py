#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 18:38:09 2018

@author: lulu
"""
class Calculator:
    name = "good calculator"
    price = 18
    def add(self,x,y):
        result = x + y
        print(result)
    def minus(self,x,y):
        result = x - y
        print(result)
cal = Calculator()
print(cal.add(10,11))

