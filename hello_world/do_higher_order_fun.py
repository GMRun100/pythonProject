#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------学习高阶函数-----------------
#高阶函数：一个函数可以接受另外一个函数作为参数，这个函数就称之为高阶函数
def add(x,y,f):
    return f(x)+f(y)

print(add(10,-20,abs))

#在python当中，函数名可以理解为指向函数的一个变量
