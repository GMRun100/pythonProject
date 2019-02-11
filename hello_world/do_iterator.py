#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------学习python中的迭代器---------------
#能够被for循环作用的对象，都认为是可迭代对象
#可以使用isinstance()判断一个对象是否是Iterable对象
from collections import Iterable
from collections import Iterator
print('判断是否是可迭代：',isinstance([],Iterable))

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#可以使用isinstance()判断一个对象是否是Iterator对象：
print('判断是否是迭代器：',isinstance((x for x in range(10)),Iterator))

#把list、dict、str等Iterable变成Iterator可以使用iter()函数
classmates=['benliu','yuan','bo','GM']
g=iter(classmates)
#通过两种方式打印迭代器中的所有元素
#方法一
for x in g:
    print(x)
#方法二
l=iter(classmates)
print('判断是否是迭代器：',isinstance(l,Iterator))
x=l
while True:
    try:
        print(x)
        x=next(l)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break