# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#多个变量赋值
a,b,c = 1,2,"join"   #join 是字符串只能用冒号引起来
#1和2被赋值给a,b，join被赋值给c
print(a)
print(b)
print(c)

#python基本数据类型
#数字

#while循环
condition = 1
while condition < 3:
    print(condition)
    condition = condition + 1
    
#for 循环
sample_list = [1,2,3,4,566,7]

for i in range(2,len(sample_list)):
    print(i)
    
#if语句
x = 1
y = 2
z = 3
if x<y:
    print("x is less or euqual to y")
else:
    print("x is greater than y")
   
a = 1
b = 2
c =3
if a < 1:
    print("a < 1")
elif a > 1:
    print("a > 1")
else:
    print("a = 1")