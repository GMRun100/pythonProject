#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------学习python中的生成器---------------
#创建一个generator
L=(x*x for x in list(range(10)))   #生成器与生成式列表定义的区别就是用[]还是()
for n in L:
    print(n)

def fib(max):
    n,a,b=0,0,1
    while n<max:
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        yield b  
        a,b=b,a+b
        n=n+1
    return 'done'
    
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
#最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。