#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#---------学习python 装饰器的用法---------------

#decorator本身不需要传入参数
def log(func):   #装饰器的目的是为了增强一个函数的功能，所以以一个函数作为参数
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper
    
@log    #此处@log相当于now=log(now),因此要放在函数的定义处
def now():
    print('2015-3-25')
  
now()
#decorator本身传入参数
def log2(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
    
@log2('execute') 
#此条语句相当于now2=log2('execute')(now2)  
#执行顺序如下：
#1.执行log2('execute'),返回decorator函数
#2.执行decorator(now2),返回wrapper函数
#3.最后相当于now2=wrapper函数,当我们在执行now2()时，就相当于在执行wrapper函数
def now2():
    print('2018-3-25')
  
now2()

print('now2\'s name=',now2.__name__)   #这里面我们发现了一个问题，我们发现now2函数名已经变成了wrapper，我们可能并不希望我们添加的日志信息，改变原有的函数属性，怎么解决呢

#---------哈哈，解决方法看下面
import functools    #需要导入这个模块
def log3(text):
    def decorator(func):
        @functools.wraps(func)     #加了这么句话
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
    
@log3('execute') 
def now3():
    print('2019-3-25')
  
now3()
print('now3\'s name=',now3.__name__)   #哈哈，成功啦


#--------练习：打印任何一个函数的执行时间
import time,functools,datetime
ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S,%f'
def metric(fn):
    print('%s executed in %s ms' % (fn.__name__,datetime.datetime.now().strftime(ISOTIMEFORMAT)))
    return fn
@metric
def fast(x,y):
    time.sleep(0.001)
    return x+y
res_f=fast(11,22)

@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x*y*z
res_s=slow(11,22,33)
print('res_f=',res_f)
print('res_s=',res_s)

#装饰器在打印日志信息的时候非常有用




