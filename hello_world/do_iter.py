#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------学习python中迭代的用法-------------
#在python中任何可以迭代的对象都可以用于迭代
from collections import Iterable
str='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in str:
    print(s)

classmates={'benliu':100,'yuan':90,'bo':80,'GM':100}
for kw in classmates:
    print(kw)     #在默认的情况下迭代dict类型的key

for key,value in classmates.items():    #遍历dict中的key和value
    print(key,value)

#只遍历dict的value类型
for value in classmates.values():
    print(value)
	
#有时候在迭代之前我们需要判断是否可以迭代
res_flag=isinstance(classmates,Iterable)   #判断一个对象是否可以迭代
print(res_flag)    #如果可以迭代返回true

classmates_str=['benliu','yuan','bo','GM']
#Python内置的enumerate函数可以把一个list变成索引-元素对
for i,value in enumerate(classmates_str):
    print(i,value)

#-------学习心得----------------
#python中的迭代用法比C++要灵活很多