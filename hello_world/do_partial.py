#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#---------学习python 偏函数的用法---------------
#在函数使用过程中，如果函数的某些参数是固定的，我们可以用偏函数的方法来定义一个新函数，使某些参数固定住
import functools
#例：int函数默认情况下是以10为底，这里我们重定义一个函数以2为底
int2=functools.partial(int,base=2)   
print('二进制:',int2('1000101'))

#当然我们还是可以在调用的时候传入其他值
print('十进制:',int2('1000101',base=10))

#在创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
#在上面的例子固定了int()函数的关键字参数base
#相当于：
kw={'base':2}
print('二进制:',int2('1000101',**kw))

max2=functools.partial(max,100) 
print('max2:',max2(5,6,7))   #用法相当于args=(10,5,6,7) max(*args)

#另外一个例子
def m_add(*args):
    sum=0
    for n in args:
        sum=sum+n
    return sum
m_add2=functools.partial(m_add,100) 
print('m_add2:',m_add2(1,2,3))  

l=[1,2,3,4]
print('m_add2:',m_add2(*l))   #应为m_add定义的是一个可变参数，所以需要在l前面加上*