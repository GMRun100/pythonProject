#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------学习python中的列表生成式---------------
import os
L=[x*x for x in list(range(10))]
print(L)

L=[x*x for x in list(range(10)) if x%2==0]  #通过if语句可以对for循环进行筛选
print(L)

#可以利用2个for循环
L=[x+y for x in 'ABC' for y in 'EDF']
print(L)

L=[x+y for x in list(range(10)) for y in list(range(10))]
print(L)    #这种情况下可以理解为两个for循环嵌套

#列出当前目录下的所有文件和目录名
L=[d for d in os.listdir('.')]
print(L)

#对dict类型进行列表生成式
classmates={'benliu':100,'yuan':90,'bo':80,'GM':100}
L=[k+'='+str(v) for k,v in classmates.items()]
print(L)


#-----------学习心得---------
#觉得这个列表生成式有点类似于字符串的初始化操作
#通过列表生成式可以快速的从一个list生成另一个list
