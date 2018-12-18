#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:02:10 2018

@author: lulu
"""

"""
字典是另一种可变容器模型，且可以存储任意类型的对象
字典的每个键值 key => value对用冒号:分割，每个键值对之间用逗号分割，整个字典包含在{}内
"""
dict1 = {'a':1,'b':2,'c':3}
print(dict1['b'])  #将键 b 所对应的值 2 查找出来
#键一般是唯一的，如果重复最后一个键值会替换前面的，值不需要唯一
print(dict1)  

#值可以取任何数据类型，但键必须不可变，如字符串，数字或元组
dict2 = {'Alice':'2341','Beth':'9010','Ceci':'3490'}
dict3 = {'abc':345}
#可以如此创建字典
dict4 = {'abc':123,98.6:37}
print(dict4[98.6])

#访问字典里的值
dict5 = {'name':'Zara','Age':7,'Class':'First'}
print('姓名为:',dict5['name'])
print('年龄为:',dict5['Age'])

#修改字典
dict6 = {'Name':'Zara','Age':8,'Class':'First'}
dict6['Age'] = 9 #对年龄进行更新
dict6['School'] = 'Runoo8'  #添加信息
print(dict6['Age'])
print(dict6)

"""
删除单一元素也能清空字典，清空只需一项操作
"""
del dict6['Name']  #删除键是 ’Name'的条目
dict6.clear()       #清空词典所有条目
del dict6           #删除字典

"""
字典的特性：字典值可以没有限制的取任何python对象，既可以是标准的对象，也可以是广义的对象，但键不像
两个重要的点：
step1:不允许同一个键出现两次，创建时如果同一个键被赋值两次，只有后一个键会被记住
setp2:键必须是不可变的，所以可以用数字，字符串或者元组充当，但是列表不可以
"""
#这里的['name']是列表，因为列表是可变的，不能充当键
#dict7 = {['Name']:'Zara','Age':7}
#print(dict7)

"""
字典可以通过以下方式调换 key和value的值，当然要注意原始value的类型，必须是不可变类型
"""
dict8 = {'a':1,'b':2,'c':3}
reverse = {v:k for k,v in dict8.items()}
print(dict8)
print(reverse)

"""
循环显示字典的key和value
"""
b = {'a':'runoob','b':'google'}
for i in b.values():
    print(i)
for j in b.keys():
    print(j)
    
"""
字典字段的比较：获取字典中的最大值及其键值
"""
prices = {'A':123,'B':450.1,'C':12,'E':444}
max_prices = max(zip(prices.values(),prices.keys()))
print(max_prices)

"""
仅输出字典中的键值
"""
dict9 = {'runoog':'runoob.com','google':'google.com'}
dict9s = dict9.keys()  #键
dict9a = dict9.values() #值
print(list(dict9s))  #输出键
print(list(dict9a))  #输出值


























