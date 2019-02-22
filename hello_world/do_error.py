#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 中错误处理的方法-----------------------
#在代码碰到错误时碰到错误是很常见的，所以需要有良好的错误处理方法
#在高级语言当中，一般都内置了一套try...except...finally...的错误处理机制
def divide(num):
    try:
        print('try...')
        r=10/int(num)
        print('result:',r)
    except ValueError as e:
        print('ValueError:',e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:',e)
    else:                       #如果没有错误也可以弹出这条信息
        print('no error!')
    finally:
        print('finally....')    #抛出异常后，finally语句也会被执行
    print('END')

divide(2)

#在实际的编程过程中，不需要在每个可能出错的地方去捕获错误，只需要在合适的层级去捕获错误即可
import logging
def foo(s):
    n=int(s)
    if n==0:
        raise ValueError('invalid value:%s' % s)  #此处可以抛出异常
    return 10/int(s)

def bar(s):
    return foo(s)*2
    
def main():
    try:
        bar('0')    #在后续的函数调用中如果有任何一个函数出现异常，这里都可以捕获到
    except Exception as e:
        logging.exception(e)   #添加此条语句后，程序在输出异常信息后，会继续向下执行
        print('Error:',e)
        #raise
    finally:
        print('finally....')
main() 
print('END')


#--------------记录错误-----------

#出错并不可怕，可怕的是不知道哪里出错了 
#出错时，会分析错误信息并定位错误发生的代码位置才是最关键的

    