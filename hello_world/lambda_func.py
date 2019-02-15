#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#---------学习python 匿名函数的用法---------------
#在python中，lambda表示匿名函数,冒号前面的表示参数
l=map(lambda x: x*x,list(range(5)))
print('l:',list(l))

#也可以把匿名函数作为返回值返回
def build(x,y):
    return lambda:x*x+y*y    #匿名函数只能有一个表达式，不用写return

f=build(1,3)    #返回参数是一个函数
print('f:',f())   #对函数再次执行才得到结果


l=list(filter(lambda x: x%2==1,range(1,20)))
print('l:',l)