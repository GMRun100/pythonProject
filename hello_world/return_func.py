#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#---------------学习python中返回函数的用法-----------------
def lazy_sum(args):
    def sum():
        ax=0
        for n in args:
            #print('n=',n)
            ax=ax+int(n)
        return ax
    return sum      #这里我们返回的是函数名
    
l=list(range(5))
print(l)
f=lazy_sum(l)       #这里我们返回的是一个函数，相关的变量和参数也保存在这个返回的函数中
print(f())          #再次执行这个函数，才会得到返回结果

def count():
    def f(j):    #用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3=count()
print('f1:',f1())
print('f2:',f2())
print('f3:',f3())
#感觉对返回函数理解的还不是太深刻，在后续的学习中再加深理解吧