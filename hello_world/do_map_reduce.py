#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------------学习python中map函数和reduce函数的用法--------------------
#map函数有两个参数，一个参数是函数，另一个参数是Iterable，map函数的作用是让函数作用于Iterable的每一个变量
def f(x):
    return x*x
    
num=list(range(5))
print('num:',num)
num2=map(f,num)
print('num2:',list(num2))   #map函数返回的是一个

#将num转化成字符串
s=map(str,num)
print('str:',list(s))

#例用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    return name.capitalize()
    
L1 = ['adam', 'LISA', 'barT'] 
L2 = list(map(normalize, L1))
print(L2)

#--------------reduce函数的用法------------------
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#例：对一个数列求和
from functools import reduce
def f_sum(x,y):
    return x+y
l_sum=reduce(f_sum,num)
print(l_sum)
